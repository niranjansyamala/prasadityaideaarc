"""Shared pieces for the Prasaditya ARC inner pages.

Every page reuses the home page's <helmet> styles, header and footer verbatim
(read from index.html) so the design system stays in one place.
"""
import re
import sys
from pathlib import Path

SITE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/home/claude/site")
MAIN = (SITE / "index.html").read_text(encoding="utf-8")

# ---------- pieces lifted from the home page ----------
STYLE = re.search(r"<style>(.*?)</style>", MAIN, re.S).group(1)
# Inner pages are long reading pages, not full-screen snaps: drop the snap rules.
STYLE = "\n".join(
    l for l in STYLE.splitlines()
    if not l.startswith(("html{scroll-snap-type", ".screen{", "footer{scroll-snap",
                         "@media (max-width: 900px){html{scroll-snap"))
)
FONTS = re.search(r'<link rel="stylesheet"[^>]+>', MAIN).group(0)
HEADER = re.search(r"<!-- Header -->\s*(<header.*?</header>)", MAIN, re.S).group(1)
FOOTER = re.search(r"<!-- Footer -->\s*(<footer.*?</footer>)", MAIN, re.S).group(1)
SCRIPT = re.search(r'(<script type="text/x-dc".*?</script>)', MAIN, re.S).group(1)

EXTRA_CSS = """
html{scroll-padding-top:140px;scroll-behavior:smooth}
@media (prefers-reduced-motion: reduce){html{scroll-behavior:auto}}
.crumb{color:#C5CAD6;text-decoration:none}.crumb:hover{color:#E3B42A}
.subnav-wrap{position:sticky;top:81px;z-index:15;background:#FFFFFF;border-bottom:1px solid #E3E1D9}
@media (max-width: 900px){.subnav-wrap{position:static}html{scroll-padding-top:90px}}
.subnav{overflow-x:auto;scrollbar-width:none}.subnav::-webkit-scrollbar{display:none}
.card{background:#FFFFFF;border:1px solid #E3E1D9;border-radius:2px}
.ph{color:#8A8A8A}
.mono{display:inline-flex;align-items:center;justify-content:center;width:128px;height:128px;border-radius:50%;background:#152238;color:#E3B42A;font-family:Lora,Georgia,serif;font-weight:600;font-size:38px;flex:none}
.mono-ph{background:#F0EFEA;color:#8A8A8A;border:1px dashed #D6D3C9}
.field{display:flex;flex-direction:column;gap:6px;font-family:Montserrat,'Segoe UI',Helvetica,Arial,sans-serif;font-weight:700;font-size:13px;color:#152238}
.field input,.field select,.field textarea{font-family:'Open Sans','Segoe UI',Helvetica,Arial,sans-serif;font-weight:400;font-size:16px;color:#2A2F3A;padding:12px 14px;border:1px solid #D6D3C9;border-radius:2px;background:#FFFFFF;min-height:48px;box-sizing:border-box;width:100%}
.field select:focus{outline:none;border-color:#E3B42A;box-shadow:0 0 0 3px rgba(227,180,42,0.25)}
.qa{border-bottom:1px solid #D6D3C9}.qa>summary{display:flex;justify-content:space-between;align-items:center;gap:24px;padding:20px 0;font-family:Lora,Georgia,serif;font-weight:600;font-size:20px;color:#152238}
.qa>div{padding:0 0 22px;color:#4B5160;font-size:16px;max-width:820px}
.tl{position:relative;display:grid;grid-template-columns:120px minmax(0,1fr);gap:4px 32px;padding-bottom:32px}
.tl::before{content:"";position:absolute;left:139px;top:10px;bottom:0;width:1px;background:#D6D3C9}
.tl:last-child::before{display:none}
.tl-dot{position:absolute;left:134px;top:6px;width:11px;height:11px;border-radius:50%;background:#E3B42A;box-shadow:0 0 0 4px #F7F5EF}
@media (max-width: 700px){.tl{grid-template-columns:1fr;padding-left:28px}.tl::before{left:5px}.tl-dot{left:0}}
"""

F_SERIF = "Lora, Georgia, 'Times New Roman', serif"
F_SANS = "Montserrat, 'Segoe UI', Helvetica, Arial, sans-serif"
GUTTER = ("max-width: 1200px; margin: 0 auto; padding-left: max(24px, env(safe-area-inset-left, 0px)); "
          "padding-right: max(24px, env(safe-area-inset-right, 0px))")

NAV_ITEMS = {  # file -> nav label it lights up
    "About": "About", "Leadership": "Leadership", "Business": "Business",
    "Investors": "Investor Relations", "Governance": "Investor Relations", "Ipo": "Investor Relations",
    "Auctions": "Auctions", "Financials": "Financials", "Careers": "Careers", "Contact": "Contact us",
}


def header_for(page):
    h = HEADER
    label = NAV_ITEMS[page]
    if page == "Contact":
        h = h.replace('class="btn-g" style="display: inline-flex; align-items: center; min-height: 44px',
                      'class="btn-on" aria-current="page" style="display: inline-flex; align-items: center; min-height: 44px')
    else:
        h = re.sub(r'(<a href="[A-Za-z]+\.dc\.html") class="nav-a">' + re.escape(label) + "</a>",
                   r'\1 class="nav-on" aria-current="page">' + label + "</a>", h, count=1)
    return h


# ---------- small builders ----------
def h2(text, id_=None, color=None, center=False):
    c = f" color: {color};" if color else ""
    cls = "hd hd-c" if center else "hd"
    ta = " text-align: center;" if center else ""
    i = f' id="{id_}"' if id_ else ""
    return (f'<h2{i} class="{cls}" style="margin: 0; font-family: {F_SERIF}; font-weight: 600; '
            f'font-size: clamp(30px, 3.4vw, 42px); line-height: 1.15;{c}{ta}">{text}</h2>')


def h3(text, size=22, color="#152238"):
    return f'<h3 style="margin: 0; font-family: {F_SERIF}; font-weight: 600; font-size: {size}px; line-height: 1.25; color: {color}">{text}</h3>'


def label(text, color="#8A6508", size=12):
    return f'<span style="font-family: {F_SANS}; font-weight: 700; font-size: {size}px; color: {color}">{text}</span>'


def p(text, size=17, color="#4B5160", extra=""):
    return f'<p style="margin: 0; font-size: {size}px; color: {color}; {extra}">{text}</p>'


def more(href, text, extra=""):
    return f'<a href="{href}" class="more" style="align-self: flex-start;{extra}">{text}</a>'


def btn(href, text, cls="btn-g", size=15, h=52):
    return (f'<a href="{href}" class="{cls}" style="display: inline-flex; align-items: center; min-height: {h}px; '
            f'padding-inline: 28px; border-radius: 2px; font-family: {F_SANS}; font-weight: 700; font-size: {size}px">{text}</a>')


def pdf(text, href="#"):
    return f'<a href="{href}" class="pdf">{text}</a>'


def chip(text, kind="on"):
    return f'<span class="chip chip-{kind}">{text}</span>'


def head_block(title, intro, id_=None, link=None, color=None, intro_color=None):
    """Section heading row: h2 + intro paragraph, optional 'more' link at right."""
    ic = intro_color or "#4B5160"
    left = (f'<div style="display: flex; flex-direction: column; gap: 10px; max-width: 760px">{h2(title, id_, color)}'
            + (p(intro, color=ic) if intro else "") + "</div>")
    if not link:
        return left
    return (f'<div style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 12px 40px">'
            f'{left}{more(*link)}</div>')


def section(inner, bg="#FFFFFF", gap=48, label_id=None, id_=None, color=None, pad="72px"):
    a = f' aria-labelledby="{label_id}"' if label_id else ""
    i = f' id="{id_}"' if id_ else ""
    c = f" color: {color};" if color else ""
    return (f'<section{i}{a} class="sec" style="background: {bg};{c}">'
            f'<div class="rv" style="{GUTTER}; padding-block: {pad}; display: flex; flex-direction: column; gap: {gap}px">'
            f'{inner}</div></section>')


def grid(items, min_w=240, gap="40px 40px", align="stretch"):
    return (f'<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min({min_w}px, 100%), 1fr)); '
            f'gap: {gap}; align-items: {align}">' + "".join(items) + "</div>")


def ruled(title, body, extra=""):
    """The home page's gold-rule column: rule, serif h3, paragraph."""
    return (f'<div style="display: flex; flex-direction: column; gap: 12px"><span class="rule" aria-hidden="true"></span>'
            f'{h3(title)}{p(body, 16)}{extra}</div>')


def numbered(items):
    lis = []
    for i, (t, b) in enumerate(items, 1):
        lis.append(f'<li style="display: grid; grid-template-columns: 44px minmax(0, 1fr); gap: 16px; padding-block: 16px; border-bottom: 1px solid #D6D3C9">'
                   f'<span class="num" aria-hidden="true">{i}</span><span><span style="font-weight: 700; color: #152238">{t}</span> '
                   f'<span style="color: #4B5160">{b}</span></span></li>')
    return '<ol style="margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column; border-top: 1px solid #D6D3C9">' + "".join(lis) + "</ol>"


def qa(q, a, open_=False):
    o = " open" if open_ else ""
    return f'<details class="qa"{o}><summary>{q}</summary><div>{a}</div></details>'


def kv(rows):
    """Definition list of label/value pairs (stacks on phones via .kv)."""
    out = []
    for k, v in rows:
        out.append(f'<dt style="font-family: {F_SANS}; font-weight: 700; font-size: 13px; color: #5F6673; padding: 14px 0; border-bottom: 1px solid #ECEAE3">{k}</dt>'
                   f'<dd style="margin: 0; padding: 14px 0; border-bottom: 1px solid #ECEAE3; color: #2A2F3A">{v}</dd>')
    return ('<dl class="kv" style="margin: 0; display: grid; grid-template-columns: minmax(180px, 280px) minmax(0, 1fr); '
            'gap: 0 32px; border-top: 1px solid #ECEAE3">' + "".join(out) + "</dl>")


def table(headers, rows, min_w=720, nowrap_cols=()):
    th = "".join(f'<th scope="col" style="padding: 14px 20px; border-bottom: 1px solid #E3E1D9{"; white-space: nowrap" if i in nowrap_cols else ""}">{h}</th>'
                 for i, h in enumerate(headers))
    body = []
    for ri, r in enumerate(rows):
        last = ri == len(rows) - 1
        bb = "" if last else "; border-bottom: 1px solid #ECEAE3"
        tds = []
        for ci, cell in enumerate(r):
            st = f"padding: 16px 20px{bb}"
            if ci == 0:
                st += "; font-weight: 700; color: #152238"
            if ci in nowrap_cols:
                st += "; white-space: nowrap; font-variant-numeric: tabular-nums"
            tds.append(f'<td style="{st}">{cell}</td>')
        body.append('<tr class="row">' + "".join(tds) + "</tr>")
    return (f'<div style="overflow-x: auto; border: 1px solid #E3E1D9; border-radius: 2px; background: #FFFFFF">'
            f'<table style="width: 100%; min-width: {min_w}px; border-collapse: collapse; font-size: 15px">'
            f'<thead><tr style="text-align: left; background: #F7F5EF; font-family: {F_SANS}; font-size: 12px; font-weight: 700">{th}</tr></thead>'
            f'<tbody>{"".join(body)}</tbody></table></div>')


def hero(crumb, title, lead, aside=""):
    """Navy page-title band with breadcrumb; shorter cousin of the home hero."""
    return f'''<section style="position: relative; background: #152238; color: #FFFFFF; overflow: hidden">
<div aria-hidden="true" style="position: absolute; left: 0; right: 0; bottom: 0; height: 100%; overflow: hidden; pointer-events: none">
<img src="./assets/9be665a12a29b2cf5b623cc5c3f690e2.jpg" alt="" class="kb" style="position: absolute; left: 0; top: 0; width: 100%; height: 100%; object-fit: cover; object-position: center bottom; opacity: 0.16; transform-origin: center bottom">
<div style="position: absolute; inset: 0; background: linear-gradient(180deg, #152238 0%, #152238 30%, rgba(21,34,56,0.55) 100%)"></div>
</div>
<div class="hero-pad" style="position: relative; {GUTTER}; padding-block: 56px 60px; display: flex; flex-direction: column; gap: 20px">
<nav aria-label="Breadcrumb" class="in" style="font-family: {F_SANS}; font-weight: 600; font-size: 13px; color: #C5CAD6"><a href="index.html" class="crumb">Home</a>{crumb}</nav>
<h1 class="in in-2" style="margin: 0; font-family: {F_SERIF}; font-weight: 600; font-size: clamp(34px, 4vw, 52px); line-height: 1.12; text-wrap: balance; max-width: 860px">{title}</h1>
<p class="in in-3" style="margin: 0; font-size: 19px; color: #D7DBE3; max-width: 760px; text-wrap: pretty">{lead}</p>
{aside}
</div>
</section>'''


def crumbs(*parts):
    """parts: (label, href|None) after Home."""
    out = ""
    for lab, href in parts:
        out += ' <span aria-hidden="true" style="color: #E3B42A; padding-inline: 6px">/</span> '
        out += f'<a href="{href}" class="crumb">{lab}</a>' if href else f'<span aria-current="page" style="color: #FFFFFF">{lab}</span>'
    return out


def subnav(links):
    a = "".join(f'<a href="#{i}" class="sub">{t}</a>' for i, t in links)
    return (f'<div class="subnav-wrap"><nav aria-label="On this page" class="subnav" style="{GUTTER}; display: flex; flex-wrap: wrap; gap: 0 28px">{a}</nav></div>')


def note(text, dark=False):
    c = "#C5CAD6" if dark else "#5F6673"
    return f'<p style="margin: 0; font-size: 13px; color: {c}">{text}</p>'


def page(name, title, body):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Prasaditya ARC — {title}</title>
<script src="./vendor/react.js"></script>
<script src="./vendor/react-dom.js"></script>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
<style>{STYLE}
{EXTRA_CSS}</style>
</helmet>
<div style="background: #FFFFFF; color: #2A2F3A; font-family: 'Open Sans', 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 17px; line-height: 1.65; min-width: 0; overflow-x: hidden">

<!-- Header -->
{header_for(name)}

<main>
{body}
</main>

<!-- Footer -->
{FOOTER}

</div>
</x-dc>
{SCRIPT}
</body>
</html>
'''


def write(name, title, body):
    (SITE / f"{name}.dc.html").write_text(page(name, title, body), encoding="utf-8")
    print("wrote", name)
