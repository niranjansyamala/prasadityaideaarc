from common import *

PH = '<span class="ph">{}</span>'.format  # placeholder text, greyed like the home page's [—] figures

# =====================================================================
# ABOUT
# =====================================================================
timeline = [
    ("March 2007", "Incorporated in Hyderabad",
     "Pridhvi Asset Reconstruction and Securitisation Company Limited (PARAS) is incorporated, CIN U67120TG2007PLC053327."),
    ("9 April 2008", "Registered with the Reserve Bank of India",
     "Registered as an asset reconstruction company under Section 3 of the SARFAESI Act, 2002."),
    ("2008-09", "First annual report",
     "The first full year of acquisitions from banks and financial institutions. An annual report has been published every year since."),
    (PH("[Year]"), "Partners in equity",
     "Union Bank of India, Punjab National Bank, UCO Bank and Zen Money join as shareholders."),
    (PH("[Date]"), "Renamed Prasaditya ARC Limited",
     "The company takes the name of its promoter group."),
    ("24 April 2026", "Fresh Certificate of Registration",
     "The Reserve Bank of India issues a fresh Certificate of Registration in the new name."),
]
tl_html = "".join(
    f'<li class="tl"><span class="tl-dot" aria-hidden="true"></span>'
    f'<span style="font-family: {F_SANS}; font-weight: 700; font-size: 14px; color: #8A6508; font-variant-numeric: tabular-nums">{d}</span>'
    f'<span style="display: flex; flex-direction: column; gap: 4px">{h3(t, 20)}{p(b, 16)}</span></li>'
    for d, t, b in timeline)

partners = "".join(
    f'<li style="display: flex; align-items: center; justify-content: center; min-height: 80px; padding: 8px 16px"><img src="./assets/{f}" alt="{a}" style="height: 52px; width: auto"></li>'
    for f, a in [("a8cff6ec222514fde897901cc09d8fd5.png", "Union Bank of India"), ("71061c75357d62245137e7492e27a379.png", "Punjab National Bank"),
                 ("17c87ac57c49afd229130b5ad67e6d46.png", "UCO Bank"), ("cfbdea6c98d53cfee8d386550cb27748.png", "Zen Money")])

about = (
    hero(crumbs(("About", None)), "About Prasaditya ARC",
         "Prasaditya ARC Limited, formerly Pridhvi Asset Reconstruction and Securitisation Company Limited (PARAS), "
         "is an asset reconstruction company registered with the Reserve Bank of India. We buy non-performing loans from banks and "
         "financial institutions and work each one to resolution.")
    + subnav([("who", "Who we are"), ("history", "History"), ("group", "Prasaditya Group"), ("partners", "Partners in equity"), ("registration", "Registration")])
    + section(
        f'<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(400px, 100%), 1fr)); gap: 32px 72px; align-items: start">'
        f'<div style="display: flex; flex-direction: column; gap: 16px">{h2("Who we are", "who-h")}'
        + p("An asset reconstruction company exists so that lenders do not have to become specialists in recovery. We take non-performing "
            "loans off the books of banks and financial institutions, hold them in trusts funded by security receipts, and do the work "
            "of restructuring, settlement, revival or, where it is the only route, enforcement and sale.")
        + p("We are headquartered in Hyderabad and regulated by the Reserve Bank of India.")
        + more("Business.dc.html", "How our business works") + "</div>"
        + grid([ruled("Our purpose", "Creating value through the revival and reconstruction of impaired assets."),
                ruled("How we work", "Accounts are resolved through restructuring, settlement, revival or enforcement, and secured assets are sold through public e-auctions."),
                ruled("Who we answer to", "Holders of security receipts, our shareholders, and the Reserve Bank of India, under the SARFAESI Act, 2002.")], 220, "32px 32px")
        + "</div>", id_="who", label_id="who-h")
    + section(head_block("History", "From incorporation in 2007 to a fresh registration in a new name in 2026.", "history-h")
              + f'<ol style="margin: 0; padding: 0; list-style: none; max-width: 900px">{tl_html}</ol>'
              + note("Bracketed items are to be confirmed from the company's records."),
              bg="#F7F5EF", id_="history", label_id="history-h")
    + section(
        f'<div style="display: flex; flex-wrap: wrap; gap: 32px 64px; align-items: center">'
        f'<img src="./assets/7dcde562336d4a72872a647d4a2b5a9d.png" alt="Prasaditya Group" style="height: 170px; width: auto; max-width: 100%; flex: none">'
        f'<div style="display: flex; flex-direction: column; gap: 14px; min-width: 0; flex: 1 1 420px">{h2("A Prasaditya Group company", "group-h")}'
        + p("Prasaditya ARC is promoted by the Prasaditya Group, headquartered in Hyderabad.", extra="max-width: 760px")
        + p("The group's chief promoter and chairperson, M. Siva Rama Vara Prasad, is Promoter Director of the company.", extra="max-width: 760px")
        + more("Leadership.dc.html", "Board and management") + "</div></div>"
        , id_="group", label_id="group-h")
    + section(h2("Our partners in equity", "partners-h", center=True)
              + p("Shareholders in Prasaditya ARC alongside the promoter group.", extra="text-align: center; max-width: 640px; margin-inline: auto")
              + f'<ul style="list-style: none; margin: 0; padding: 0; width: 100%; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(150px, 100%), 1fr)); gap: 24px; align-items: center">{partners}</ul>',
              bg="#F7F5EF", gap=24, id_="partners", label_id="partners-h")
    + section(head_block("Registration and corporate details", None, "registration-h")
              + kv([("Legal name", "Prasaditya ARC Limited"),
                    ("Former name", "Pridhvi Asset Reconstruction and Securitisation Company Limited (PARAS)"),
                    ("Corporate Identity Number", "U67120TG2007PLC053327"),
                    ("Regulator", "Reserve Bank of India, under Section 3 of the SARFAESI Act, 2002"),
                    ("Date of registration", "9 April 2008; fresh Certificate of Registration in the new name issued 24 April 2026"),
                    ("RBI registration number", PH("[—]")),
                    ("Registered and corporate office", "Plot No. 6, 6A, 6B, 4th Floor, Raja Praasadamu, Kondapur, Hyderabad, Telangana 500 084, India")]),
              id_="registration", label_id="registration-h", gap=32)
)
write("About", "About", about)

# =====================================================================
# LEADERSHIP
# =====================================================================
def person(name, role, bio, img=None, initials=None, placeholder=False):
    if img:
        pic = f'<img src="./assets/{img}" alt="{name}" style="width: 128px; height: 128px; border-radius: 50%; object-fit: cover; background: #FFFFFF">'
    else:
        pic = f'<span class="mono{" mono-ph" if placeholder else ""}" aria-hidden="true">{initials}</span>'
    nm_color = "#8A8A8A" if placeholder else "#152238"
    return (f'<div style="display: flex; flex-direction: column; gap: 16px">{pic}<div style="display: flex; flex-direction: column; gap: 6px">'
            f'<span style="font-family: {F_SERIF}; font-weight: 600; font-size: 22px; line-height: 1.25; color: {nm_color}">{name}</span>'
            f'{label(role)}<span style="font-size: 15px; color: #4B5160">{bio}</span></div></div>')

board = [
    person("M. Siva Rama Vara Prasad", "Promoter Director",
           "Chief promoter and chairperson of the Prasaditya Group.",
           "96f8921ea57c17ccfef9e05d0d9219d0.png"),
    person("Koteswara Rao SSR", "Chairperson and Independent Director",
           "Fellow of the Institute of Chartered Accountants of India and senior partner at Brahmayya &amp; Co., Hyderabad. Former President of the Federation of Andhra Pradesh Chambers of Commerce and Industry.",
           "8db4c4b135d3278badee6b5510c689af.png"),
    person("R. Mallikarjuna", "Managing Director &amp; CEO",
           "Former General Manager of Andhra Bank, where he headed recovery and legal, and former Presiding Officer of Debts Recovery Tribunal I, Hyderabad. A registered Insolvency Professional.",
           "03bc2d60f458d22444bec0d35604bb98.png"),
    person("[Name]", "Independent Director", "[Short biography: former role, institution and relevant experience.]", initials="—", placeholder=True),
    person("[Name]", "Independent Director", "[Short biography: former role, institution and relevant experience.]", initials="—", placeholder=True),
    person("[Name]", "Nominee Director", "[Nominating shareholder and short biography.]", initials="—", placeholder=True),
]
mgmt = [
    person("R. Mallikarjuna", "Managing Director &amp; CEO",
           "Leads acquisitions, resolution and the company's relationships with lenders and investors.", "03bc2d60f458d22444bec0d35604bb98.png"),
    person("K.V. Ramakrishna Prasad", "Vice President (Legal &amp; Resolutions)",
           "Heads legal and resolutions, and is the company's Grievance Redressal Officer.", initials="KR"),
    person("[Name]", "Chief Financial Officer", "[Short biography.]", initials="—", placeholder=True),
    person("[Name]", "Company Secretary &amp; Compliance Officer", "[Short biography.]", initials="—", placeholder=True),
]
leadership = (
    hero(crumbs(("Leadership", None)), "Board and management",
         "The board of directors and the management team of Prasaditya ARC Limited.")
    + subnav([("board", "Board of directors"), ("management", "Management"), ("committees", "Board committees")])
    + section(head_block("Board of directors", None, "board-h")
              + grid(board, 300) + note("Grey entries are placeholders for directors whose details are to be added."),
              id_="board", label_id="board-h")
    + section(head_block("Management", "The people who run acquisitions, resolution, finance and compliance day to day.", "mgmt-h")
              + grid(mgmt, 260), bg="#F7F5EF", id_="management", label_id="mgmt-h")
    + section(head_block("Board committees", "Composition, terms of reference and the policies each committee oversees are published under corporate governance.",
                         "com-h", ("Governance.dc.html#committees", "Committees and policies")),
              id_="committees", label_id="com-h", pad="64px")
)
write("Leadership", "Leadership", leadership)

# =====================================================================
# BUSINESS
# =====================================================================
arr = '<svg class="arr" aria-hidden="true" width="28" height="28" viewBox="0 0 28 28" style="flex: none; align-self: center"><path d="M6 14h14M14 8l6 6-6 6" fill="none" stroke="#8A6508" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>'
def step(tag, t, b, dark=False):
    if dark:
        return (f'<div style="flex: 1 1 0; display: flex; flex-direction: column; gap: 8px; padding: 22px 24px; background: #152238; border-radius: 2px">'
                f'{label(tag, "#E3B42A")}<span style="font-weight: 700; color: #FFFFFF">{t}</span><span style="font-size: 14px; color: #D7DBE3">{b}</span></div>')
    return (f'<div style="flex: 1 1 0; display: flex; flex-direction: column; gap: 8px; padding: 22px 24px; background: #F7F5EF; border-radius: 2px">'
            f'{label(tag)}<span style="font-weight: 700; color: #152238">{t}</span><span style="font-size: 14px; color: #4B5160">{b}</span></div>')

flow = (f'<div class="flow" aria-label="How a stressed loan moves through an asset reconstruction company" style="display: flex; align-items: stretch; gap: 12px">'
        + step("Lender", "A bank or NBFC sells a non-performing loan", "Singly or as a portfolio, by auction or negotiated sale") + arr
        + step("Trust", "A trust buys the loan, funded by security receipts", "Receipts are held by the lender, other investors and the ARC") + arr
        + step("Prasaditya ARC", "We manage the trust and resolve the account", "Settlement, restructuring, revival, or enforcement and e-auction", True) + arr
        + step("Investors", "Recoveries redeem the security receipts", "The trust closes once the receipts are paid out") + "</div>")

audience = lambda t, who, items, cta: (
    f'<div class="card" style="display: flex; flex-direction: column; gap: 14px; padding: 28px">{label(who)}{h3(t)}'
    f'<ul style="margin: 0; padding-left: 20px; color: #4B5160; font-size: 16px; display: flex; flex-direction: column; gap: 6px">'
    + "".join(f"<li>{i}</li>" for i in items) + f'</ul>{cta}</div>')

business = (
    hero(crumbs(("Business", None)), "What we do with a stressed loan",
         "We acquire non-performing financial assets from banks and financial institutions, resolve each account, "
         "and return the proceeds to the holders of security receipts.")
    + subnav([("model", "Business model"), ("resolution", "Ways to resolve"), ("work", "Working with us"), ("faq", "Questions")])
    + section(
        f'<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(400px, 100%), 1fr)); gap: 32px 72px; align-items: start">'
        f'<div style="display: flex; flex-direction: column; gap: 16px">{h2("Our business model", "model-h")}'
        + p("Banks and financial institutions carry loans that have stopped performing. An ARC takes those loans off their books and does the "
            "specialist work of recovering value from them, so lenders can return to lending.") + "</div>"
        + numbered([("Acquisition.", "We acquire non-performing financial assets from banks and financial institutions, individually or as portfolios, funded through security receipts issued to qualified investors."),
                    ("Resolution.", "Each account is worked towards resolution: restructuring the debt, a negotiated settlement, revival of the business, or enforcement of security under the SARFAESI Act and the insolvency code."),
                    ("Realisation.", "Secured assets are sold through public e-auctions, and recoveries are passed back to the holders of security receipts.")])
        + "</div>" + flow, id_="model", label_id="model-h", gap=44)
    + section(head_block("Ways to resolve an account", "An account may be resolved through any of the routes below, depending on its circumstances.", "res-h")
              + grid([ruled("Restructuring", "Rescheduling repayments or changing the terms of the debt where the underlying business can carry it."),
                      ruled("Settlement", "A negotiated one-time settlement with the borrower or guarantors, in line with our board-approved policy."),
                      ruled("Revival", "Supporting a change in management, fresh funding or a sale of the business as a going concern."),
                      ruled("Enforcement", "Taking possession of secured assets under the SARFAESI Act, 2002 and selling them by public e-auction, or proceedings under the insolvency code.",
                            more("Auctions.dc.html", "Current e-auction notices", " margin-top: 4px"))]),
              bg="#F7F5EF", id_="resolution", label_id="res-h")
    + section(head_block("Working with us", None, "work-h")
              + grid([audience("Selling stressed assets", "Banks and financial institutions",
                               ["Single accounts or portfolios", "Cash or security-receipt structures", "Due diligence on a defined timetable"],
                               more("Contact.dc.html", "Talk to our acquisitions team")),
                      audience("Investing in security receipts", "Qualified buyers",
                               ["Participation in trusts alongside the ARC", "Regular reporting on each trust", "Redemption as recoveries are made"],
                               more("Contact.dc.html", "Ask about current trusts")),
                      audience("If your loan has been assigned to us", "Borrowers and guarantors",
                               ["We deal with you under our Fair Practice Code", "Settlement proposals are considered on merit", "A named Grievance Redressal Officer"],
                               more("Contact.dc.html#grievance", "Grievance redressal"))], 280, "24px 24px"),
              id_="work", label_id="work-h")
    + section(head_block("Questions", None, "faq-h")
              + '<div style="border-top: 1px solid #D6D3C9">'
              + qa("What is a security receipt?", "A security receipt is an instrument issued by a trust set up by the ARC. It gives its holder an undivided right in the financial asset the trust has acquired. Holders are paid as the trust recovers money from the account.", True)
              + qa("Why do banks sell loans to an ARC?", "Selling a non-performing loan takes it off the bank's books, frees capital for fresh lending, and hands the recovery work to a specialist whose sole business it is.")
              + qa("My loan has been assigned to Prasaditya ARC. What happens now?", "You will receive a notice of assignment. From then on, payments and correspondence about the loan are with us. Contact the office to discuss your account; you can also raise any complaint with our Grievance Redressal Officer.")
              + qa("How are secured assets sold?", "Through public e-auctions under the Security Interest (Enforcement) Rules, 2002. Each sale notice is published with its tender document and annexures on our auctions page and in newspapers.")
              + "</div>", bg="#F7F5EF", id_="faq", label_id="faq-h", gap=32)
)
write("Business", "Business", business)

# =====================================================================
# CAREERS
# =====================================================================
careers = (
    hero(crumbs(("Careers", None)), "Careers at Prasaditya ARC",
         "Recovery is specialist work. We look for people with banking, legal, credit, valuation and finance experience who want to see "
         "difficult accounts through to resolution.")
    + section(head_block("Who we hire", None, "who-h")
              + grid([ruled("Resolution and recovery", "Officers who manage a book of accounts from acquisition to closure."),
                      ruled("Legal", "Advocates and legal officers for SARFAESI, DRT and insolvency proceedings."),
                      ruled("Acquisitions and valuation", "Credit and valuation specialists who assess portfolios offered by lenders."),
                      ruled("Finance, compliance and secretarial", "Accounting, trust reporting, regulatory returns and company-secretarial work.")]),
              label_id="who-h")
    + section(head_block("Current openings", "Openings are listed here as they arise.", "open-h")
              + table(["Role", "Function", "Location", "Experience", ""],
                      [[PH("[Role]"), PH("[Function]"), "Hyderabad", PH("[— years]"), PH("[Apply]")],
                       [PH("[Role]"), PH("[Function]"), "Hyderabad", PH("[— years]"), PH("[Apply]")]], 640, (2, 3))
              + note("Replace the bracketed rows with current openings, or with “No openings at present” when there are none."),
              bg="#F7F5EF", label_id="open-h", gap=32)
    + section(
        f'<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(400px, 100%), 1fr)); gap: 32px 72px; align-items: start">'
        f'<div style="display: flex; flex-direction: column; gap: 16px">{h2("How to apply", "apply-h")}'
        + p("Send your CV with the role you are applying for in the subject line. We will contact you if your experience matches an opening.")
        + f'<div style="display: flex; flex-wrap: wrap; gap: 12px; padding-top: 4px">{btn("mailto:co@prasadityaarc.co.in?subject=Application", "Email your CV")}</div>'
        + note("Applications go to co@prasadityaarc.co.in unless a dedicated careers address is set up.") + "</div>"
        + numbered([("Apply.", "Send your CV and the role you are interested in."),
                    ("Conversation.", "A first discussion with the head of the function."),
                    ("Interview.", "One or more interviews with the function head and management."),
                    ("Offer.", "References and an offer letter.")]) + "</div>",
        label_id="apply-h")
)
write("Careers", "Careers", careers)

# =====================================================================
# CONTACT
# =====================================================================
contact_card = lambda tag, title, lines: (
    f'<div style="display: flex; flex-direction: column; gap: 10px; padding-top: 18px; border-top: 3px solid #E3B42A">{label(tag)}{h3(title, 22)}'
    + "".join(f'<span style="font-size: 16px; color: #4B5160; overflow-wrap: anywhere">{l}</span>' for l in lines) + "</div>")

form = f'''<form action="mailto:co@prasadityaarc.co.in" method="post" enctype="text/plain" class="card" style="display: flex; flex-direction: column; gap: 18px; padding: 32px">
{h3("Send us a message", 24)}
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(220px, 100%), 1fr)); gap: 18px">
<label class="field">Full name<input type="text" name="name" autocomplete="name" required></label>
<label class="field">Phone<input type="tel" name="phone" autocomplete="tel"></label>
</div>
<label class="field">Email<input type="email" name="email" autocomplete="email" required></label>
<label class="field">About
<select name="topic">
<option>Selling stressed assets</option>
<option>Investing in security receipts</option>
<option>An account assigned to Prasaditya ARC</option>
<option>An e-auction or tender</option>
<option>Investor Relations</option>
<option>Careers</option>
<option>Something else</option>
</select></label>
<label class="field">Message<textarea name="message" rows="5" style="min-height: 140px; resize: vertical"></textarea></label>
<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 12px 20px">
<button type="submit" class="btn-g" style="display: inline-flex; align-items: center; min-height: 52px; padding-inline: 28px; border: 0; border-radius: 2px; font-family: {F_SANS}; font-weight: 700; font-size: 15px; cursor: pointer">Send message</button>
<span style="font-size: 13px; color: #5F6673">Opens your email app with the message filled in. For complaints, use the grievance contacts.</span>
</div>
</form>'''

contact = (
    hero(crumbs(("Contact", None)), "Contact us",
         "Our registered and corporate office is in Kondapur, Hyderabad. Write, call or use the form, and tell us whether your enquiry "
         "is about an account, an auction, an investment or something else.")
    + section(
        f'<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(400px, 100%), 1fr)); gap: 40px 64px; align-items: start">'
        f'<div style="display: flex; flex-direction: column; gap: 36px">'
        + contact_card("Registered and corporate office", "Prasaditya ARC Limited",
                       ["Plot No. 6, 6A, 6B, 4th Floor, Raja Praasadamu, Kondapur, Hyderabad, Telangana 500 084, India",
                        '<a href="tel:+914041413333">+91-40-41413333</a>', '<a href="mailto:co@prasadityaarc.co.in">co@prasadityaarc.co.in</a>',
                        "Office hours: " + PH("[Monday to Saturday, 9:30 am to 6:00 pm]")])
        + contact_card("Auctions and tenders", "Questions about a sale notice",
                       ["Each sale notice names the authorised officer to contact for inspection and bidding.",
                        '<a href="Auctions.dc.html">See current notices</a>'])
        + "</div>" + form + "</div>", label_id=None, gap=0)
    + section(
        head_block("Grievance redressal", "If you have a complaint about how an account has been handled, write to the Grievance Redressal Officer. "
                   "Please quote your account or trust name.", "grievance-h", color=None)
        + grid([contact_card("Grievance Redressal Officer", "Mr. K.V. Ramakrishna Prasad",
                             ["Vice President (Legal &amp; Resolutions)", '<a href="tel:04041413333">040-41413333</a>',
                              '<a href="mailto:Ramakrishnaprasadkv@prasadityaarc.co.in">Ramakrishnaprasadkv@prasadityaarc.co.in</a>']),
                contact_card("Credit information bureau complaints", "Customer care",
                             ["For corrections to credit information reported by us.",
                              '<a href="mailto:customercare@prasadityaarc.co.in">customercare@prasadityaarc.co.in</a>']),
                contact_card("Shareholders and investors", "Investor grievances",
                             ["Company Secretary &amp; Compliance Officer: " + PH("[Name]"), PH("[investor email]"),
                              '<a href="Investors.dc.html#grievance">Investor grievance redressal</a>'])], 260, "36px 40px")
        + note("Our customer grievance redressal policy and Fair Practice Code are published under corporate governance. "
               '<a href="Governance.dc.html#policies">Read the policies</a>.'),
        bg="#F7F5EF", id_="grievance", label_id="grievance-h")
)
write("Contact", "Contact", contact)
