-- Prairie Lantern Bank commercial loan database (fictional)
-- SQLite schema. One row per borrower, loan, fiscal year, test, quarter, or default.

CREATE TABLE borrowers (
    borrower_id        TEXT PRIMARY KEY,
    name               TEXT NOT NULL,
    industry           TEXT NOT NULL,
    sector             TEXT NOT NULL CHECK (sector IN ('C&I', 'CRE')),
    city               TEXT,
    state              TEXT,
    years_in_business  INTEGER,
    relationship_start DATE,
    guarantor          INTEGER  -- 1 = personal guaranty in place
);

CREATE TABLE loans (
    loan_id          TEXT PRIMARY KEY,
    borrower_id      TEXT NOT NULL REFERENCES borrowers(borrower_id),
    facility_type    TEXT NOT NULL,
    origination_date DATE NOT NULL,
    maturity_date    DATE NOT NULL,
    commitment       REAL NOT NULL,
    rate_type        TEXT,
    interest_rate    REAL,
    collateral_type  TEXT,
    amort_years      INTEGER,    -- NULL for revolving lines
    officer          TEXT
);

CREATE TABLE financials (
    borrower_id           TEXT NOT NULL REFERENCES borrowers(borrower_id),
    fiscal_year           INTEGER NOT NULL,
    statement_date        DATE NOT NULL,
    revenue               REAL,
    ebitda                REAL,     -- NOI for CRE borrowers
    dscr                  REAL,
    funded_debt_to_ebitda REAL,     -- C&I only
    current_ratio         REAL,     -- C&I only
    ltv                   REAL,     -- CRE only
    PRIMARY KEY (borrower_id, fiscal_year)
);

CREATE TABLE covenant_tests (
    loan_id     TEXT NOT NULL REFERENCES loans(loan_id),
    test_date   DATE NOT NULL,
    fiscal_year INTEGER NOT NULL,
    covenant    TEXT NOT NULL,
    requirement REAL NOT NULL,
    actual      REAL NOT NULL,
    result      TEXT NOT NULL CHECK (result IN ('Pass', 'Fail'))
);

CREATE TABLE quarterly_snapshots (
    loan_id       TEXT NOT NULL REFERENCES loans(loan_id),
    as_of_date    DATE NOT NULL,
    outstanding   REAL NOT NULL,
    risk_grade    INTEGER NOT NULL CHECK (risk_grade BETWEEN 1 AND 9),
    days_past_due INTEGER NOT NULL,
    nonaccrual    INTEGER NOT NULL,
    charge_off    REAL NOT NULL,
    PRIMARY KEY (loan_id, as_of_date)
);

CREATE TABLE defaults (
    loan_id             TEXT PRIMARY KEY REFERENCES loans(loan_id),
    borrower_id         TEXT NOT NULL REFERENCES borrowers(borrower_id),
    default_date        DATE NOT NULL,
    exposure_at_default REAL NOT NULL,
    recovery_amount     REAL,       -- NULL while in workout
    loss_amount         REAL,
    lgd                 REAL,
    resolution_date     DATE,
    status              TEXT
);

CREATE INDEX ix_snap_date ON quarterly_snapshots(as_of_date);
CREATE INDEX ix_loans_borrower ON loans(borrower_id);
CREATE INDEX ix_cov_loan ON covenant_tests(loan_id, test_date);
