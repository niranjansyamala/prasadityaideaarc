from common import *

PH = '<span class="ph">{}</span>'.format

# =====================================================================
# AUCTIONS
# =====================================================================
notices = [
    ("mid-city", "M/s Mid City Projects LLP", "Property in Mumbai; notices in The Indian Express and Loksatta", "4 July 2026",
     ["Sale notice", "Tender document", "Annexure 2", "Annexure 3", "Annexure 4", "Annexure 5", "Annexure 6"]),
    ("rupa", "M/s Rupa Traders (RTKVB)", "Two secured properties, one per guarantor", "7 July 2026",
     ["Sale notice, property 1", "Sale notice, property 2", "Tender documents", "Annexures 2 to 5"]),
    ("indo-dutch", "M/s Indo-Dutch Proteins Limited", "Secured asset, item no. 1", "16 June 2026",
     ["Sale notice", "Tender document", "Annexures"]),
    ("vm", "M/s VM Commodities (India) Pvt Ltd", "Secured asset, item no. 1", "10 June 2026",
     ["Sale notice", "Tender document", "Annexures"]),
    ("gupta", "M/s Gupta Group Portfolio", "Properties at Krishna Nagar, Akkireddy Palem and Lalapet", "4 to 6 June 2026",
     ["Sale notice, Krishna Nagar", "Sale notice, Akkireddy Palem", "Sale notice, Lalapet", "Tender documents"]),
    ("msr", "M/s MSR Mega Bio Power Limited", "Open land, and a residential property, in two separate auctions", "1 to 2 June 2026",
     ["Sale notice, open land", "Sale notice, residential property", "Tender documents", "Annexures"]),
]
cards = []
for id_, acct, assets, date, docs in notices:
    cards.append(
        f'<article id="{id_}" class="card" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(300px, 100%), 1fr)); gap: 20px 40px; padding: 28px">'
        f'<div style="display: flex; flex-direction: column; gap: 8px">'
        f'<div style="display: flex; flex-wrap: wrap; gap: 8px; align-items: center">{chip("Sale notice published")}'
        f'<span style="font-family: {F_SANS}; font-weight: 700; font-size: 13px; color: #5F6673; font-variant-numeric: tabular-nums">{date}</span></div>'
        f'{h3(acct)}<span style="font-size: 16px; color: #4B5160">{assets}</span>'
        f'<dl style="margin: 6px 0 0; display: grid; grid-template-columns: auto 1fr; gap: 2px 16px; font-size: 14px; color: #4B5160">'
        f'<dt style="font-weight: 700; color: #152238">Auction date</dt><dd style="margin: 0">{PH("[date and time]")}</dd>'
        f'<dt style="font-weight: 700; color: #152238">Reserve price</dt><dd style="margin: 0">{PH("₹ [—]")}</dd>'
        f'<dt style="font-weight: 700; color: #152238">EMD</dt><dd style="margin: 0">{PH("₹ [—]")}</dd>'
        f'<dt style="font-weight: 700; color: #152238">Authorised officer</dt><dd style="margin: 0">{PH("[name, phone]")}</dd></dl></div>'
        f'<div style="display: flex; flex-direction: column; gap: 12px">{label("Documents", "#5F6673")}'
        f'<div style="display: flex; flex-wrap: wrap; gap: 8px">' + "".join(pdf(d + " (PDF)") for d in docs) + "</div></div></article>")
for n in range(7, 13):
    cards.append(
        f'<article class="card" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(300px, 100%), 1fr)); gap: 20px 40px; padding: 28px; border-style: dashed">'
        f'<div style="display: flex; flex-direction: column; gap: 8px"><div>{chip("Notice " + str(n), "later")}</div>'
        f'{h3("[Account name]", color="#8A8A8A")}<span style="font-size: 16px; color: #8A8A8A">[Assets on offer] · [sale notice date]</span></div>'
        f'<div style="display: flex; flex-direction: column; gap: 12px">{label("Documents", "#5F6673")}'
        f'<div style="display: flex; flex-wrap: wrap; gap: 8px">{pdf("Sale notice (PDF)")}{pdf("Tender document (PDF)")}</div></div></article>')

auctions = (
    hero(crumbs(("Auctions and tenders", None)), "E-auction and tender notices",
         "Sale notices issued under the Security Interest (Enforcement) Rules, 2002. Each notice is published with its tender document "
         "and annexures, and in newspapers circulating where the asset is located.",
         f'<div class="in in-4" style="display: flex; flex-wrap: wrap; gap: 12px 32px; padding-top: 8px; font-family: {F_SANS}; font-weight: 700; font-size: 14px; color: #FFFFFF">'
         f'<span><span style="color: #E3B42A">12</span> notices published</span><span>Updated {PH("[date]")}</span></div>')
    + subnav([("notices", "Current notices"), ("bid", "How to take part"), ("terms", "Terms and disclaimers")])
    + section(head_block("Current notices", "Most recent first. Open a notice for the property description, reserve price, earnest money deposit, inspection dates and bidding terms.", "notices-h")
              + '<div style="display: flex; flex-direction: column; gap: 16px">' + "".join(cards) + "</div>"
              + note("Notices 7 to 12 and the bracketed fields are placeholders to be filled from the published sale notices."),
              bg="#F7F5EF", id_="notices", label_id="notices-h", gap=32)
    + section(
        f'<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(400px, 100%), 1fr)); gap: 32px 72px; align-items: start">'
        f'<div style="display: flex; flex-direction: column; gap: 16px">{h2("How to take part", "bid-h")}'
        + p("Every e-auction follows the terms in its own sale notice and tender document. Read both before you bid; the steps below are the usual sequence.")
        + more("Contact.dc.html", "Questions about an auction") + "</div>"
        + numbered([("Read the notice.", "Download the sale notice and tender document for the asset and check the description, reserve price and dates."),
                    ("Inspect.", "Arrange an inspection with the authorised officer named in the notice, on the dates it sets."),
                    ("Register and deposit.", "Register on the e-auction platform named in the notice and pay the earnest money deposit before the deadline."),
                    ("Submit the tender.", "Send the signed tender form with KYC documents and proof of the deposit."),
                    ("Bid online.", "Bid on the auction date, in the increments the notice specifies."),
                    ("Pay and complete.", "The successful bidder pays the balance within the time set in the notice; the sale is then confirmed and a sale certificate issued.")])
        + "</div>", id_="bid", label_id="bid-h")
    + section(head_block("Terms and disclaimers", None, "terms-h")
              + '<div style="border-top: 1px solid #D6D3C9">'
              + qa("Assets are sold on an as-is basis", "Secured assets are sold on an “as is where is, as is what is and whatever there is” basis. Bidders should satisfy themselves about title, encumbrances and statutory dues before bidding.", True)
              + qa("The sale notice prevails", "Where anything on this page differs from the published sale notice or tender document, the notice and tender document prevail.")
              + qa("Right to accept or reject bids", "The authorised officer may accept or reject any bid, or postpone or cancel an auction, as set out in the terms of sale.")
              + "</div>", bg="#F7F5EF", id_="terms", label_id="terms-h", gap=32)
)
write("Auctions", "Auctions and tenders", auctions)

# =====================================================================
# INVESTORS
# =====================================================================
def doc_row(title, desc, status, kind, action=""):
    return (f'<li class="row" style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px 24px; padding: 18px 20px; border-bottom: 1px solid #ECEAE3">'
            f'<span style="display: flex; flex-direction: column; gap: 2px; min-width: 0; flex: 1 1 320px"><span style="font-weight: 700; color: #152238">{title}</span>'
            f'<span style="font-size: 14px; color: #5F6673">{desc}</span></span>'
            f'<span style="display: flex; align-items: center; gap: 10px">{chip(status, kind)}{action}</span></li>')

ON_FILING = "On filing of the DRHP"  # counsel: these go live only on the DRHP filing date

def doc_list(rows):
    return '<ul style="margin: 0; padding: 0; list-style: none; border: 1px solid #E3E1D9; border-bottom: 0; border-radius: 2px; background: #FFFFFF">' + "".join(rows) + "</ul>"

investors = (
    hero(crumbs(("Investor Relations", None)), "Investor Relations",
         "The documents required under the Companies Act, 2013 and the SEBI ICDR Regulations, 2018 in connection with the proposed public "
         "offering, kept in one place and published as they are filed.",
         f'<div class="in in-4" style="display: flex; flex-wrap: wrap; gap: 12px; padding-top: 8px">{btn("Ipo.dc.html", "About the proposed offering")}'
         f'{btn("#grievance", "Investor grievances", "btn-ow")}</div>')
    + subnav([("drhp", "DRHP"), ("restated", "Restated financials"), ("offer-docs", "Material creditors and industry report"),
              ("reports", "Annual reports"), ("group", "Group companies"), ("governance", "Governance"),
              ("shareholders", "Shareholders"), ("grievance", "Grievance redressal")])
    + section(
        f'<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(400px, 100%), 1fr)); gap: 32px 72px; align-items: start">'
        f'<div style="display: flex; flex-direction: column; gap: 16px">{h2("Draft Red Herring Prospectus", "drhp-h")}'
        + p("The DRHP will be hosted here, with the prescribed disclaimer, once it is filed with SEBI and the stock exchanges. "
            "Visitors will be asked to confirm they have read the disclaimer before the document opens.") + "</div>"
        + f'<div style="display: flex; flex-direction: column; gap: 10px; padding: 28px; background: #152238; border-radius: 2px; border-top: 3px solid #E3B42A">'
        + label("Status", "#E3B42A") + f'<span style="font-family: {F_SERIF}; font-weight: 600; font-size: 28px; color: #FFFFFF">Not yet filed</span>'
        + '<span style="font-size: 15px; color: #D7DBE3">Filing date, SEBI and exchange links, and any addenda will appear here.</span>'
        + f'<dl style="margin: 8px 0 0; display: grid; grid-template-columns: auto 1fr; gap: 4px 16px; font-size: 14px; color: #C5CAD6">'
        + f'<dt style="font-weight: 700; color: #FFFFFF">Filed with SEBI</dt><dd style="margin: 0">[—]</dd>'
        + f'<dt style="font-weight: 700; color: #FFFFFF">Book running lead managers</dt><dd style="margin: 0">[—]</dd>'
        + f'<dt style="font-weight: 700; color: #FFFFFF">Registrar to the offer</dt><dd style="margin: 0">[—]</dd></dl></div></div>',
        id_="drhp", label_id="drhp-h")
    + section(head_block("Restated financial information", "Restated Financial Information of the company for the periods covered by the Draft Red Herring Prospectus.", "restated-h")
              + doc_list([doc_row("Restated Financial Information",
                                  "As at and for the three months ended June 30, 2026 and for the financial years ended March 31, 2026, March 31, 2025 and March 31, 2024",
                                  ON_FILING, "soon")]),
              bg="#F7F5EF", id_="restated", label_id="restated-h", gap=32)
    + section(head_block("Other offer-related documents", "Published with the Draft Red Herring Prospectus.", "offer-h")
              + doc_list([doc_row("Outstanding overdues to material creditors",
                                  "Names of the material creditors and the amounts involved, as at June 30, 2026", ON_FILING, "soon"),
                          doc_row("Industry report", PH("[Title of the report, issuing agency and date]"), ON_FILING, "soon")]),
              id_="offer-docs", label_id="offer-h", gap=32)
    + section(head_block("Annual reports and audited statements", "Annual reports and audited financial statements of the company for the preceding three financial years.", "reports-h", ("Financials.dc.html", "All annual reports"))
              + doc_list([doc_row(f"Annual report {y}", "Directors' report, audited financial statements and auditors' report", ON_FILING, "soon")
                          for y in ("2025-26", "2024-25", "2023-24")]),
              bg="#F7F5EF", id_="reports", label_id="reports-h", gap=32)
    + section(head_block("Group companies", "Audited financial statements of each Group Company for the preceding three financial years, with the particulars below.", "group-h")
              + f'<div style="display: flex; flex-direction: column; gap: 16px">{h3("[Name of Group Company]", color="#8A8A8A")}'
              + table(["Financial year", "Reserves (excluding revaluation reserve)", "Sales", "Profit after tax", "Earnings per share", "Diluted earnings per share", "Net asset value", "Audited financial statements"],
                      [[y] + [PH("[—]")] * 6 + [pdf("PDF")] for y in ("2025-26", "2024-25", "2023-24")], 980, (0, 7))
              + "</div>"
              + note("One table for each Group Company identified in the DRHP. Remove this section if the DRHP identifies none."),
              id_="group", label_id="group-h", gap=32)
    + section(head_block("Corporate governance", "The members of the board and of each committee, and the company's corporate governance policies.", "gov-h", ("Governance.dc.html", "Governance and policies"))
              + grid([ruled("Board and committees", "Composition of the board and of each committee, with terms of reference.", more("Governance.dc.html#committees", "Committees")),
                      ruled("Policies", "Fair Practice Code, grievance redressal, related-party transactions and the other policies.", more("Governance.dc.html#policies", "Policies")),
                      ruled("Codes of conduct", "For directors and senior management, and for the prevention of insider trading.", more("Governance.dc.html#codes", "Codes"))]),
              bg="#F7F5EF", id_="governance", label_id="gov-h")
    + section(head_block("Shareholders", None, "sh-h")
              + doc_list([doc_row("Shareholding pattern", "Promoter group, partner banks and other shareholders", "Before listing", "later"),
                          doc_row("Notices of general meetings", "With explanatory statements and results of voting", "On issue", "later"),
                          doc_row("Material contracts and documents for inspection", "Listed in the offer document", "With the RHP", "later")]),
              id_="shareholders", label_id="sh-h", gap=32)
    + section(head_block("Investor grievance redressal", "Shareholders and investors can write to the Company Secretary and Compliance Officer.", "grv-h", color="#FFFFFF", intro_color="#D7DBE3")
              + grid([f'<div style="display: flex; flex-direction: column; gap: 8px; padding-top: 18px; border-top: 3px solid #E3B42A">{label("Compliance Officer", "#E3B42A")}'
                      f'<span style="font-family: {F_SERIF}; font-weight: 600; font-size: 22px; color: #FFFFFF">[Name]</span><span>Company Secretary &amp; Compliance Officer</span><span>[email] · +91-40-41413333</span></div>',
                      f'<div style="display: flex; flex-direction: column; gap: 8px; padding-top: 18px; border-top: 1px solid #2C3B57">{label("Registrar and share transfer agent", "#E3B42A")}'
                      f'<span style="font-family: {F_SERIF}; font-weight: 600; font-size: 22px; color: #FFFFFF">[Registrar]</span><span>[address, phone and email]</span></div>',
                      f'<div style="display: flex; flex-direction: column; gap: 8px; padding-top: 18px; border-top: 1px solid #2C3B57">{label("Customer complaints", "#E3B42A")}'
                      f'<span style="font-family: {F_SERIF}; font-weight: 600; font-size: 22px; color: #FFFFFF">Mr. K.V. Ramakrishna Prasad</span><span>Grievance Redressal Officer · 040-41413333</span>'
                      f'<a href="Contact.dc.html#grievance" class="fl">All grievance contacts</a></div>'], 260, "32px 40px")
              + note("Once listed, complaints can also be lodged on SEBI's SCORES platform.", dark=True),
              bg="#152238", color="#D7DBE3", id_="grievance", label_id="grv-h")
)
write("Investors", "Investor Relations", investors)

# =====================================================================
# FINANCIALS
# =====================================================================
years = [f"{y}-{str(y + 1)[2:]}" for y in range(2025, 2007, -1)]  # 2025-26 ... 2008-09
def yr_row(y):
    return [f"Annual report {y}", pdf("Annual report (PDF)"), pdf("Annual return extract (PDF)") if int(y[:4]) >= 2014 else '<span class="ph">—</span>']
recent, older = years[:8], years[8:]

metric = lambda k, d: (f'<div style="display: flex; flex-direction: column; gap: 12px"><span class="rule" aria-hidden="true"></span>'
                       f'<dt style="font-family: {F_SANS}; font-weight: 700; font-size: 13px; color: #5F6673">{k}</dt>'
                       f'<dd style="margin: 0; font-family: {F_SERIF}; font-weight: 600; font-size: clamp(36px, 3.6vw, 52px); line-height: 1.05; color: #8A8A8A; font-variant-numeric: tabular-nums">₹ [—] crore</dd>'
                       f'<dd style="margin: 0; font-size: 14px; color: #5F6673">{d}</dd></div>')

financials = (
    hero(crumbs(("Financials", None)), "Financial information",
         "Audited figures for each financial year, every annual report since 2008-09, and the regulatory disclosures we publish.")
    + subnav([("ytd", "Year to date"), ("audited", "Audited figures"), ("reports", "Annual reports"), ("disclosures", "Disclosures")])
    + section(head_block("Performance, year to date", "Financial year 2026-27, 1 April 2026 to [DATE]. Unaudited management figures, updated [monthly].", "ytd-h")
              + '<dl style="margin: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(240px, 100%), 1fr)); gap: 40px 40px">'
              + metric("Debt acquired", "Dues acquired from banks and financial institutions in the period")
              + metric("Recoveries", "Collected across all trusts in the period")
              + metric("Security receipts redeemed", "Paid back to the holders of security receipts")
              + metric("Assets under management", "Outstanding security receipts across all trusts at period end")
              + "</dl>" + note("Replace the brackets with the figures for the period when they are reviewed."),
              id_="ytd", label_id="ytd-h")
    + section(head_block("Audited figures by year", "Key figures from the audited financial statements, ₹ crore.", "aud-h")
              + table(["Financial year", "Total income", "Profit after tax", "Net worth", "Security receipts outstanding", "Recoveries"],
                      [[y] + ['<span class="ph">[—]</span>'] * 5 for y in years[:5]], 760, (1, 2, 3, 4, 5))
              + note("Figures to be taken from each year's audited statements."),
              bg="#F7F5EF", id_="audited", label_id="aud-h", gap=32)
    + section(head_block("Annual reports", "Directors' report, audited financial statements and auditors' report for each year, with the extract of the annual return.", "rep-h")
              + table(["Year", "Annual report", "Annual return"], [yr_row(y) for y in recent], 560)
              + f'<details class="qa" style="border-top: 1px solid #D6D3C9"><summary>Earlier years, {older[-1]} to {older[0]}</summary><div style="max-width: none">'
              + table(["Year", "Annual report", "Annual return"], [yr_row(y) for y in older], 560) + "</div></details>",
              id_="reports", label_id="rep-h", gap=32)
    + section(head_block("Regulatory disclosures", None, "dis-h")
              + grid([ruled("Disclosures under RBI directions", "Disclosures required of asset reconstruction companies in the notes to the financial statements.", pdf("Latest (PDF)")),
                      ruled("Security receipts and trusts", "Details of trusts and security receipts outstanding, as required to be disclosed.", pdf("Latest (PDF)")),
                      ruled("CSR", "Corporate social responsibility policy, annual action plan and amounts spent.", pdf("Latest (PDF)"))]),
              bg="#F7F5EF", id_="disclosures", label_id="dis-h")
)
write("Financials", "Financials", financials)

# =====================================================================
# GOVERNANCE
# =====================================================================
committee = lambda name, purpose: (
    f'<div class="card" style="display: flex; flex-direction: column; gap: 12px; padding: 26px">{h3(name, 20)}{p(purpose, 15)}'
    f'<dl style="margin: 0; display: grid; grid-template-columns: auto 1fr; gap: 2px 14px; font-size: 14px; color: #4B5160">'
    f'<dt style="font-weight: 700; color: #152238">Chair</dt><dd style="margin: 0">{PH("[Name]")}</dd>'
    f'<dt style="font-weight: 700; color: #152238">Members</dt><dd style="margin: 0">{PH("[Names]")}</dd></dl>'
    f'<div>{pdf("Terms of reference (PDF)")}</div></div>')

pol = lambda t, d, live: (t, d, chip("Published", "on") if live else chip("To be published", "soon"), pdf("PDF") if live else '<span class="ph">—</span>')

governance = (
    hero(crumbs(("Investor Relations", "Investors.dc.html"), ("Corporate governance", None)), "Corporate governance",
         "The board, its committees and their terms of reference, and the policies covering how we deal with borrowers, "
         "investors, employees and related parties.")
    + subnav([("board", "Board"), ("committees", "Committees"), ("policies", "Policies"), ("codes", "Codes of conduct")])
    + section(head_block("Board composition", "Led by an independent chairperson, Koteswara Rao SSR.", "board-h", ("Leadership.dc.html", "Board and management"))
              + '<dl style="margin: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(200px, 100%), 1fr)); gap: 40px">'
              + "".join(f'<div style="display: flex; flex-direction: column; gap: 10px"><span class="rule" aria-hidden="true"></span>'
                        f'<dt style="font-family: {F_SANS}; font-weight: 700; font-size: 13px; color: #5F6673">{k}</dt>'
                        f'<dd style="margin: 0; font-family: {F_SERIF}; font-weight: 600; font-size: clamp(36px, 3.6vw, 52px); line-height: 1.05; color: #8A8A8A">[—]</dd></div>'
                        for k in ["Directors", "Independent directors", "Women directors", "Board meetings in 2025-26"])
              + "</dl>", id_="board", label_id="board-h")
    + section(head_block("Board committees", None, "com-h")
              + grid([committee("Audit Committee", "Oversees financial reporting, internal controls, the auditors and related-party transactions."),
                      committee("Nomination and Remuneration Committee", "Board appointments, evaluation and remuneration of directors and senior management."),
                      committee("Stakeholders' Relationship Committee", "Resolves the grievances of shareholders and security holders."),
                      committee("Risk Management Committee", "Reviews credit, market, operational and compliance risk."),
                      committee("Corporate Social Responsibility Committee", "Recommends the CSR policy and monitors spending."),
                      committee("IT Strategy Committee", "Oversees information technology and cyber security.")], 300, "24px 24px"),
              bg="#F7F5EF", id_="committees", label_id="com-h", gap=32)
    + section(head_block("Policies", None, "pol-h")
              + table(["Policy", "What it covers", "Status", ""],
                      [pol("Fair Practice Code", "How we deal with borrowers, from acquisition of the loan to closure", True),
                       pol("Customer grievance redressal policy", "How complaints are received, escalated and resolved", True),
                       pol("Policy on related-party transactions", "Approval and disclosure of transactions with related parties", False),
                       pol("Nomination and remuneration policy", "Criteria for appointing and paying directors and senior management", False),
                       pol("Whistle-blower policy and vigil mechanism", "How directors and employees can report concerns", False),
                       pol("Policy on materiality of events", "Which events are disclosed to the stock exchanges", False),
                       pol("Policy on preservation and archival of documents", "How long records are kept and published", False),
                       pol("Dividend distribution policy", "How the board decides on dividends", False),
                       pol("Corporate social responsibility policy", "Areas of CSR activity and how projects are chosen", False),
                       pol("Prevention of sexual harassment policy", "Under the POSH Act, 2013", False)], 760, (2,))
              + note("Status of each policy to be confirmed before publication."),
              id_="policies", label_id="pol-h", gap=32)
    + section(head_block("Codes of conduct", None, "codes-h")
              + grid([ruled("Code of conduct for directors and senior management", "Standards of conduct and the duties of independent directors.", pdf("PDF")),
                      ruled("Code for prevention of insider trading", "Under the SEBI (Prohibition of Insider Trading) Regulations, 2015, effective on listing.", chip("On listing", "later")),
                      ruled("Code of fair disclosure", "Practices for fair disclosure of unpublished price-sensitive information.", chip("On listing", "later"))]),
              bg="#F7F5EF", id_="codes", label_id="codes-h")
)
write("Governance", "Corporate governance", governance)

# =====================================================================
# IPO
# =====================================================================
stages = [("Board and shareholder approvals", "Approval of the offer by the board and shareholders.", "[status]", "later"),
          ("DRHP filed with SEBI and the stock exchanges", "The draft offer document is published for public comment.", "Not yet filed", "soon"),
          ("SEBI observations", "SEBI issues its observations on the draft.", "Later", "later"),
          ("RHP filed with the Registrar of Companies", "The red herring prospectus is filed and published.", "Later", "later"),
          ("Price band and offer period", "The price band and bid dates are announced.", "Later", "later"),
          ("Allotment and listing", "Shares are allotted and trading begins on the exchanges.", "Later", "later")]
stage_html = "".join(
    f'<li style="display: grid; grid-template-columns: 44px minmax(0, 1fr) auto; gap: 16px; align-items: center; padding-block: 16px; border-bottom: 1px solid #D6D3C9">'
    f'<span class="num" aria-hidden="true">{i}</span><span><span style="font-weight: 700; color: #152238">{t}.</span> <span style="color: #4B5160">{d}</span></span>'
    f'{chip(s if s != "[status]" else "[status]", k)}</li>'
    for i, (t, d, s, k) in enumerate(stages, 1))

ipo = (
    hero(crumbs(("Investor Relations", "Investors.dc.html"), ("Initial public offering", None)), "Proposed initial public offering",
         "Prasaditya ARC Limited proposes, subject to market conditions and the necessary approvals, to make an initial public offering of its equity shares. "
         "No offer document has been filed yet.")
    + section(
        f'<div style="display: flex; flex-direction: column; gap: 10px; padding: 24px 28px; background: #FBF6E6; border: 1px solid #E3B42A; border-radius: 2px">'
        f'{label("Important", "#6B4E06", 13)}'
        + p("This page is for information only and is not an offer, invitation or solicitation to buy or sell securities. Any offer will be made only through "
            "a red herring prospectus filed with the Registrar of Companies. [Final wording of the disclaimer to be provided by legal counsel.]", 15, "#3A3A3A")
        + "</div>", pad="40px 0px", gap=0)
    + section(
        f'<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(400px, 100%), 1fr)); gap: 32px 72px; align-items: start">'
        f'<div style="display: flex; flex-direction: column; gap: 16px">{h2("Where the offer stands", "st-h")}'
        + p("The usual sequence for a public offering in India. Each step will be updated here, with documents, as it is completed.")
        + more("Investors.dc.html#drhp", "Draft Red Herring Prospectus") + "</div>"
        + f'<ol style="margin: 0; padding: 0; list-style: none; border-top: 1px solid #D6D3C9">{stage_html}</ol></div>',
        label_id="st-h", pad="24px 72px")
    + section(head_block("Offer details", "To be completed from the offer document once filed.", "od-h")
              + kv([("Type of offer", PH("[Fresh issue and/or offer for sale]")), ("Offer size", PH("[—]")), ("Price band", PH("[—]")),
                    ("Minimum bid lot", PH("[—] equity shares")), ("Book running lead managers", PH("[—]")), ("Registrar to the offer", PH("[—]")),
                    ("Proposed listing", PH("[—]")), ("Offer opens / closes", PH("[—]"))]),
              bg="#F7F5EF", label_id="od-h", gap=32)
    + section(head_block("Before you invest", None, "bi-h")
              + grid([ruled("Read the offer document", "Investment decisions should be based only on the red herring prospectus, including its risk factors."),
                      ruled("Understand the business", "How an asset reconstruction company earns: management fees and its share of recoveries.", more("Business.dc.html", "Our business model")),
                      ruled("Ask us", "Questions about the offer can go to the Company Secretary and Compliance Officer.", more("Investors.dc.html#grievance", "Investor contacts"))]),
              label_id="bi-h")
)
write("Ipo", "Initial public offering", ipo)
