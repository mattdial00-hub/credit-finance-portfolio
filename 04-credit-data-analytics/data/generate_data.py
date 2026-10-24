"""
Generate the synthetic Prairie Lantern Bank commercial loan database.

Everything here is fictional. Borrower financials, risk grades, payment behavior,
and defaults are simulated from a known process so the SQL and modeling work
can be demonstrated end to end. Run:  python generate_data.py
Output: prairie_lantern_loans.db (SQLite) and one CSV per table.
"""
import sqlite3, math, random, datetime as dt, csv, os
import numpy as np

SEED = 2026
rng = np.random.default_rng(SEED); random.seed(SEED)
HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, "prairie_lantern_loans.db")
N_BORROWERS = 1500
AS_OF = dt.date(2026, 9, 30)
QUARTERS = [dt.date(y, m, d) for y in range(2023, 2027) for (m, d) in ((3, 31), (6, 30), (9, 30), (12, 31))]
QUARTERS = [q for q in QUARTERS if q <= AS_OF]

# industry: (sector, true risk offset, base DSCR median, yearly shocks)
IND = {
    "Manufacturing":         ("C&I", -0.10, 1.70, {}),
    "Construction":          ("C&I",  0.30, 1.55, {2025: -0.05}),
    "Healthcare":            ("C&I", -0.35, 1.85, {}),
    "Wholesale Distribution":("C&I",  0.00, 1.60, {}),
    "Transportation":        ("C&I",  0.25, 1.50, {2023: -0.08, 2024: -0.05}),
    "Energy Services":       ("C&I",  0.35, 1.65, {2025: -0.04}),
    "Restaurants":           ("C&I",  0.60, 1.40, {2023: -0.06, 2024: -0.04}),
    "Professional Services": ("C&I", -0.20, 1.80, {}),
    "Agriculture":           ("C&I",  0.10, 1.55, {}),
    "Retail Trade":          ("C&I",  0.30, 1.45, {}),
    "CRE - Multifamily":     ("CRE", -0.30, 1.45, {2024: -0.03}),
    "CRE - Office":          ("CRE",  0.50, 1.50, {2023: -0.10, 2024: -0.12, 2025: -0.08}),
    "CRE - Retail":          ("CRE",  0.20, 1.45, {}),
    "CRE - Industrial":      ("CRE", -0.45, 1.60, {2024: 0.03}),
    "CRE - Hospitality":     ("CRE",  0.45, 1.40, {2024: -0.05}),
    "CRE - Self Storage":    ("CRE", -0.30, 1.55, {}),
    "CRE - Senior Housing":  ("CRE",  0.30, 1.35, {2023: -0.04}),
}
IND_W = {"Manufacturing": 9, "Construction": 7, "Healthcare": 7, "Wholesale Distribution": 6, "Transportation": 5, "Energy Services": 5,
         "Restaurants": 4, "Professional Services": 5, "Agriculture": 3, "Retail Trade": 4, "CRE - Multifamily": 10, "CRE - Office": 7,
         "CRE - Retail": 6, "CRE - Industrial": 8, "CRE - Hospitality": 4, "CRE - Self Storage": 4, "CRE - Senior Housing": 3}
MACRO = {2022: 0.0, 2023: -0.03, 2024: -0.02, 2025: 0.0}
CITIES = [("Houston", "TX", 30), ("Dallas", "TX", 18), ("San Antonio", "TX", 10), ("Austin", "TX", 8), ("Fort Worth", "TX", 7), ("Beaumont", "TX", 4),
          ("Corpus Christi", "TX", 4), ("Lake Charles", "LA", 5), ("Baton Rouge", "LA", 5), ("Shreveport", "LA", 3), ("Tulsa", "OK", 3), ("Oklahoma City", "OK", 3)]
A = ["Bluebonnet", "Cedar Bayou", "Lone Star", "Gulfline", "Red River", "Pecan Hollow", "Ironwood", "Sabine", "Brazos", "Trinity", "Live Oak", "Cypress",
     "Mesquite", "Caddo", "Guadalupe", "Frio", "Nueces", "Pinewood", "Prairie View", "Copper Creek", "Stonegate", "Harborview", "Magnolia", "Westpark",
     "Eastfield", "Northline", "Riverbend", "Highland", "Twin Oaks", "Bayside", "Clearfork", "Granite Ridge", "Silverleaf", "Sandstone", "Falcon Point"]
SUF = {"Manufacturing": ["Manufacturing", "Machine Works", "Industries", "Fabrication"], "Construction": ["Construction", "Builders", "Contractors", "Electric"],
       "Healthcare": ["Medical Group", "Dental", "Physical Therapy", "Family Practice"], "Wholesale Distribution": ["Supply", "Distributors", "Wholesale"],
       "Transportation": ["Logistics", "Trucking", "Freight"], "Energy Services": ["Oilfield Services", "Energy Services", "Pipeline Services"],
       "Restaurants": ["Restaurant Group", "Kitchen", "Grill"], "Professional Services": ["Engineering", "Consulting", "Advisors"],
       "Agriculture": ["Farms", "Feed & Seed", "Ag Supply"], "Retail Trade": ["Outfitters", "Home Center", "Mercantile"],
       "CRE - Multifamily": ["Apartments", "Residences", "Village"], "CRE - Office": ["Office Plaza", "Office Center", "Tower"],
       "CRE - Retail": ["Shopping Center", "Commons", "Marketplace"], "CRE - Industrial": ["Industrial Park", "Distribution Center", "Business Park"],
       "CRE - Hospitality": ["Hotel", "Inn & Suites", "Lodge"], "CRE - Self Storage": ["Self Storage", "Storage"], "CRE - Senior Housing": ["Senior Living", "Assisted Living"]}
ENT = ["LLC", "Inc.", "LP", "Ltd."]

def pick(d):
    keys = list(d); w = np.array([d[k] for k in keys], float); return keys[rng.choice(len(keys), p=w / w.sum())]
def logistic(x): return 1 / (1 + math.exp(-x))
def master_grade(pd_):
    for g, ub in enumerate([0.002, 0.005, 0.01, 0.02, 0.04, 0.08, 0.18, 0.40], start=1):
        if pd_ < ub: return g
    return 9
def qend(d):
    for q in QUARTERS:
        if d <= q: return q
    return None

# ---------------- borrowers ----------------
borrowers, names = [], set()
for i in range(N_BORROWERS):
    ind = pick(IND_W); sector = IND[ind][0]
    while True:
        nm = f"{random.choice(A)} {random.choice(SUF[ind])}, {random.choice(ENT)}"
        if nm not in names: names.add(nm); break
    city, state, _ = CITIES[rng.choice(len(CITIES), p=np.array([c[2] for c in CITIES]) / sum(c[2] for c in CITIES))]
    rel_year = int(rng.choice(range(2014, 2026), p=np.array([3, 4, 5, 6, 7, 8, 8, 9, 10, 10, 9, 6], float) / 85))
    borrowers.append(dict(borrower_id=f"B{1001 + i}", name=nm, industry=ind, sector=sector, city=city, state=state,
                          years_in_business=int(max(2, rng.normal(16, 9))), relationship_start=dt.date(rel_year, int(rng.integers(1, 13)), 1),
                          guarantor=int(rng.random() < (0.85 if sector == "C&I" else 0.7))))

# ---------------- financials and true default process ----------------
financials, outcomes = [], {}
INTERCEPT = -2.86
for b in borrowers:
    sector, off, med, shocks = IND[b["industry"]]
    first_fy = max(2022, b["relationship_start"].year - 1)
    base = math.log(med * 1.12) + rng.normal(0, 0.22)
    lndscr = base
    lev = float(np.clip(rng.lognormal(math.log(2.1), 0.3), 0.6, 5.5)) if sector == "C&I" else None
    ltv = float(np.clip(rng.normal(0.60, 0.07), 0.35, 0.85)) if sector == "CRE" else None
    cr = float(np.clip(rng.lognormal(math.log(1.5), 0.25), 0.7, 3.5)) if sector == "C&I" else None
    rev = float(np.clip(rng.lognormal(math.log(9e6), 0.8), 1.2e6, 9e7)) if sector == "C&I" else float(np.clip(rng.lognormal(math.log(1.6e6), 0.6), 3e5, 1.5e7))
    prev = None
    for fy in range(first_fy, 2026):
        if fy > first_fy:
            d = MACRO.get(fy, 0) + shocks.get(fy, 0) + rng.normal(0, 0.13) + 0.3 * (base - lndscr)
            lndscr += d
            if lev is not None: lev = float(np.clip(lev * math.exp(-0.8 * d + rng.normal(0, 0.07)), 0.4, 8))
            if ltv is not None: ltv = float(np.clip(ltv * math.exp(-0.5 * d + (0.05 if b["industry"] == "CRE - Office" else 0) + rng.normal(0, 0.03)), 0.3, 1.2))
            if cr is not None: cr = float(np.clip(cr * math.exp(0.4 * d + rng.normal(0, 0.06)), 0.5, 4))
            rev *= math.exp(rng.normal(0.04, 0.08) + 0.5 * d)
        dscr = math.exp(lndscr)
        chg = 0 if prev is None else lndscr - prev
        x = INTERCEPT - 2.6 * math.log(dscr) + off + 1.3 * max(0, -chg) - 0.4 * b["guarantor"] - 0.012 * (b["years_in_business"] - 15)
        x += 0.40 * (lev - 2.5) - 0.55 * (cr - 1.5) if sector == "C&I" else 3.2 * (ltv - 0.62)
        pd_true = logistic(x)
        ebitda = rev * float(np.clip(rng.normal(0.13, 0.03), 0.04, 0.3)) if sector == "C&I" else rev * 0.95
        financials.append(dict(borrower_id=b["borrower_id"], fiscal_year=fy, statement_date=dt.date(fy, 12, 31), revenue=round(rev, -3), ebitda=round(ebitda, -3),
                               dscr=round(dscr, 2), funded_debt_to_ebitda=None if lev is None else round(lev, 2), current_ratio=None if cr is None else round(cr, 2),
                               ltv=None if ltv is None else round(ltv, 3), _pd=pd_true))
        prev = lndscr
        if rng.random() < pd_true:
            dd = dt.date(fy + 1, 1, 1) + dt.timedelta(days=int(rng.integers(0, 365)))
            if dd <= AS_OF:
                outcomes[b["borrower_id"]] = dd
            break  # no further statements after a default (or censored default after the as-of date)

# ---------------- loans ----------------
loans = []
lid = 5001
for b in borrowers:
    sector = b["sector"]; n = 1 + int(rng.random() < 0.45) + int(rng.random() < 0.12)
    for k in range(n):
        if sector == "CRE":
            ftype = "CRE Term"; commit = float(np.clip(rng.lognormal(math.log(2.0e6), 0.6), 4e5, 1.2e7)); amort = 25; coll = "Real estate (1st lien)"
        else:
            ftype = ["Term Loan", "Revolving Line", "Equipment Loan"][k % 3] if k else random.choice(["Term Loan", "Revolving Line", "Equipment Loan"])
            commit = float(np.clip(rng.lognormal(math.log(7.0e5), 0.7), 1.0e5, 6e6))
            amort = {"Term Loan": 7, "Revolving Line": None, "Equipment Loan": 7}[ftype]
            coll = {"Term Loan": "Business assets (blanket)", "Revolving Line": "A/R and inventory", "Equipment Loan": "Equipment (PMSI)"}[ftype]
        start = max(b["relationship_start"], dt.date(2015, 1, 1))
        span = (dt.date(2025, 12, 31) - start).days
        orig = start + dt.timedelta(days=int(rng.integers(0, max(1, span)))) if k else start
        if orig > dt.date(2025, 12, 31): orig = dt.date(2025, 12, 1)
        dd_b = outcomes.get(b["borrower_id"])
        if dd_b and orig > dd_b - dt.timedelta(days=150): orig = dd_b - dt.timedelta(days=150)  # no new loans to a borrower about to default
        if ftype == "Revolving Line": mat = dt.date(2027, int(rng.integers(1, 13)), 28)
        elif ftype == "CRE Term": mat = dt.date(int(rng.integers(2026, 2034)), int(rng.integers(1, 13)), 28)
        else: mat = dt.date(int(rng.integers(2027, 2032)), int(rng.integers(1, 13)), 28)
        if mat <= AS_OF: mat = dt.date(2026, 12, 31)
        rate_type = "Floating" if ftype == "Revolving Line" or rng.random() < 0.4 else "Fixed"
        loans.append(dict(loan_id=f"L{lid}", borrower_id=b["borrower_id"], facility_type=ftype, origination_date=orig, maturity_date=mat,
                          commitment=round(commit, -3), rate_type=rate_type, interest_rate=round(float(rng.normal(0.072, 0.008)), 4),
                          collateral_type=coll, amort_years=amort, officer=random.choice(["M. Dial", "R. Castillo", "J. Whitfield", "A. Nguyen", "T. Broussard", "K. Okafor"])))
        lid += 1

# ---------------- quarterly snapshots, defaults ----------------
fin_by = {}
for f in financials: fin_by.setdefault(f["borrower_id"], {})[f["fiscal_year"]] = f
snapshots, defaults = [], []
LGD_MEAN = {"Real estate (1st lien)": 0.24, "Business assets (blanket)": 0.42, "A/R and inventory": 0.40, "Equipment (PMSI)": 0.36}
bmap = {b["borrower_id"]: b for b in borrowers}
for L in loans:
    b = bmap[L["borrower_id"]]; ddate = outcomes.get(b["borrower_id"]); dq = qend(ddate) if ddate else None
    util = float(rng.uniform(0.45, 0.85)); grade_prev = None; closed = False; co_total = 0.0
    fins = fin_by.get(b["borrower_id"], {})
    for q in QUARTERS:
        if closed or q < qend(L["origination_date"]): continue
        # latest statements available at quarter end (received by April 30)
        fy_av = q.year - 1 if q.month >= 6 else q.year - 2
        f = fins.get(fy_av) or fins.get(min(fins)) if fins else None
        pd_obs = f["_pd"] if f else 0.02
        if grade_prev is None or q.month == 6:
            g = master_grade(pd_obs * math.exp(rng.normal(0, 0.60)))  # officer judgment adds noise
        else:
            g = grade_prev
        g = min(g, 7) if g > 7 and not dq else g
        yrs = (q - L["origination_date"]).days / 365.25
        if L["amort_years"]: bal = L["commitment"] * max(0.08, 1 - yrs / L["amort_years"])
        else:
            util = float(np.clip(util + rng.normal(0, 0.06), 0.2, 0.98)); bal = L["commitment"] * util
        dpd = 0; nonacc = 0; co = 0.0
        if rng.random() < (0.10 if g >= 6 else 0.015): dpd = int(rng.integers(5, 29))
        if g >= 6 and not dq and rng.random() < 0.03: dpd = int(rng.integers(30, 60))  # late but cures
        if dq:
            qi, di = QUARTERS.index(q), QUARTERS.index(dq)
            if qi == di - 1:
                g = max(g, 7); dpd = int(rng.integers(30, 60)) if rng.random() < 0.7 else dpd
            elif qi == di:
                g = 8; dpd = int(rng.integers(90, 120)); nonacc = 1
                ead = bal; lgd = float(np.clip(rng.beta(2, 2) * 2 * LGD_MEAN[L["collateral_type"]] * (1.3 if b["industry"] == "CRE - Office" else 1), 0.02, 0.95))
                defaults.append(dict(loan_id=L["loan_id"], borrower_id=b["borrower_id"], default_date=ddate, exposure_at_default=round(ead, 2),
                                     lgd=lgd, _q=di))
            elif qi > di:
                dft = [d_ for d_ in defaults if d_["loan_id"] == L["loan_id"]][0]
                g = 9 if qi - di >= 1 and dft["lgd"] > 0.35 else 8; nonacc = 1; dpd = 90 + 90 * (qi - di)
                loss = dft["exposure_at_default"] * dft["lgd"]
                if qi - di == 1: co = round(loss * 0.6, 2)
                if qi - di == 2:
                    co = round(loss - co_total, 2); closed = True
                    dft["resolution_date"] = q; dft["recovery_amount"] = round(dft["exposure_at_default"] - loss, 2); dft["loss_amount"] = round(loss, 2)
                co_total += co
                bal = max(0.0, dft["exposure_at_default"] - co_total - (dft["exposure_at_default"] - loss if closed else 0))
        snapshots.append(dict(loan_id=L["loan_id"], as_of_date=q, outstanding=round(bal, 2), risk_grade=g, days_past_due=dpd, nonaccrual=nonacc, charge_off=co))
        grade_prev = g
for d_ in defaults:
    d_.setdefault("resolution_date", None); d_.setdefault("recovery_amount", None); d_.setdefault("loss_amount", None)
    d_["status"] = "Resolved" if d_["resolution_date"] else "Open workout"

# ---------------- covenant tests ----------------
cov = []
for L in loans:
    b = bmap[L["borrower_id"]]
    for fy, f in fin_by.get(b["borrower_id"], {}).items():
        td = dt.date(fy + 1, 4, 30)
        if td > AS_OF or td < L["origination_date"]: continue
        req = 1.20 if b["sector"] == "CRE" else 1.25
        cov.append(dict(loan_id=L["loan_id"], test_date=td, fiscal_year=fy, covenant="Minimum DSCR", requirement=req, actual=f["dscr"], result="Pass" if f["dscr"] >= req else "Fail"))
        if b["sector"] == "CRE":
            cov.append(dict(loan_id=L["loan_id"], test_date=td, fiscal_year=fy, covenant="Maximum LTV", requirement=0.75, actual=f["ltv"], result="Pass" if f["ltv"] <= 0.75 else "Fail"))
        else:
            mx = 3.5 if L["facility_type"] == "Revolving Line" else 3.0
            cov.append(dict(loan_id=L["loan_id"], test_date=td, fiscal_year=fy, covenant="Maximum Funded Debt / EBITDA", requirement=mx, actual=f["funded_debt_to_ebitda"], result="Pass" if f["funded_debt_to_ebitda"] <= mx else "Fail"))

# ---------------- write ----------------
if os.path.exists(DB): os.remove(DB)
con = sqlite3.connect(DB)
schema = open(os.path.join(HERE, "..", "sql", "00_schema.sql")).read()
con.executescript(schema)
def ins(table, rows, cols):
    con.executemany(f"INSERT INTO {table} ({','.join(cols)}) VALUES ({','.join('?' * len(cols))})",
                    [[(r[c].isoformat() if isinstance(r[c], dt.date) else r[c]) for c in cols] for r in rows])
    with open(os.path.join(HERE, f"{table}.csv"), "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(cols)
        for r in rows: w.writerow([(r[c].isoformat() if isinstance(r[c], dt.date) else r[c]) for c in cols])
ins("borrowers", borrowers, ["borrower_id", "name", "industry", "sector", "city", "state", "years_in_business", "relationship_start", "guarantor"])
ins("loans", loans, ["loan_id", "borrower_id", "facility_type", "origination_date", "maturity_date", "commitment", "rate_type", "interest_rate", "collateral_type", "amort_years", "officer"])
ins("financials", financials, ["borrower_id", "fiscal_year", "statement_date", "revenue", "ebitda", "dscr", "funded_debt_to_ebitda", "current_ratio", "ltv"])
ins("covenant_tests", cov, ["loan_id", "test_date", "fiscal_year", "covenant", "requirement", "actual", "result"])
ins("quarterly_snapshots", snapshots, ["loan_id", "as_of_date", "outstanding", "risk_grade", "days_past_due", "nonaccrual", "charge_off"])
ins("defaults", defaults, ["loan_id", "borrower_id", "default_date", "exposure_at_default", "recovery_amount", "loss_amount", "lgd", "resolution_date", "status"])
con.commit()
for t in ["borrowers", "loans", "financials", "covenant_tests", "quarterly_snapshots", "defaults"]:
    print(t, con.execute(f"select count(*) from {t}").fetchone()[0])
print("defaulted borrowers", len(outcomes), "by year", {y: sum(1 for d in outcomes.values() if d.year == y) for y in (2023, 2024, 2025, 2026)})
con.close()
