"""
ETL Pipeline — Real Estate Sales Optimisation
==============================================
Author: Kresio Azevedo Fernando
Portfolio: kresio-azevedo-fernando.github.io

Purpose:
    Extracts client and sales data from Excel dataset,
    transforms and cleans it, and loads into SQLite
    database ready for SQL analysis and Power BI dashboard.

Usage:
    python etl_pipeline.py

Output:
    realestate.db — SQLite database with cleaned tables
"""

import pandas as pd
import sqlite3
import os
from datetime import datetime

EXCEL_PATH = "../dados/dataset-anonimizado.xlsx"
DB_PATH    = "realestate.db"


def extract(path):
    print(f"[EXTRACT] Reading: {path}")
    xl = pd.ExcelFile(path)
    sheets = {}
    for sheet in xl.sheet_names:
        sheets[sheet] = xl.parse(sheet)
        print(f"  ✓ Sheet '{sheet}' — {len(sheets[sheet])} rows")
    return sheets


def transform(sheets):
    print("\n[TRANSFORM] Cleaning and standardising data...")
    cleaned = {}
    for name, df in sheets.items():
        df.columns = (
            df.columns.str.strip().str.lower()
            .str.replace(" ", "_").str.replace(r"[^\w]", "", regex=True)
        )
        df = df.dropna(how="all")

        # Standardise gender if present
        for col in df.columns:
            if "gender" in col or "genero" in col or "sexo" in col:
                df[col] = df[col].str.strip().str.upper()
                df[col] = df[col].map(
                    {"M": "Male", "F": "Female",
                     "H": "Male", "MALE": "Male", "FEMALE": "Female"}
                ).fillna(df[col])

            if "age" in col or "idade" in col:
                df[col] = pd.to_numeric(df[col], errors="coerce")
                df["age_group"] = pd.cut(
                    df[col],
                    bins=[17, 25, 30, 35, 40, 50, 65, 100],
                    labels=["18-25","26-30","31-35",
                            "36-40","41-50","51-65","65+"]
                )

            if "salary" in col or "salario" in col or "income" in col:
                df[col] = pd.to_numeric(df[col], errors="coerce")
                df["salary_band"] = pd.cut(
                    df[col],
                    bins=[0, 30000, 45000, 60000, 80000, 999999],
                    labels=["<30K","30-45K","45-60K","60-80K","80K+"]
                )

            if "purchased" in col or "comprou" in col or "bought" in col:
                df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)

        df["_loaded_at"] = datetime.utcnow().isoformat()
        cleaned[name] = df
        print(f"  ✓ '{name}' cleaned — {len(df)} rows, {len(df.columns)} columns")
    return cleaned


def load(tables, db_path):
    print(f"\n[LOAD] Writing to: {db_path}")
    conn = sqlite3.connect(db_path)
    for name, df in tables.items():
        safe = name.lower().replace(" ", "_")
        df.to_sql(safe, conn, if_exists="replace", index=False)
        print(f"  ✓ Table '{safe}' — {len(df)} rows loaded")
    conn.close()


def validate(db_path):
    print("\n[VALIDATE] Row counts:")
    conn = sqlite3.connect(db_path)
    cur  = conn.cursor()
    for (t,) in cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall():
        n = cur.execute(f"SELECT COUNT(*) FROM '{t}'").fetchone()[0]
        print(f"  {t}: {n} rows")
    conn.close()


def run():
    print("=" * 55)
    print(" ETL Pipeline — Real Estate Sales Optimisation")
    print(f" Started: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC")
    print("=" * 55)
    if not os.path.exists(EXCEL_PATH):
        print(f"[ERROR] File not found: {EXCEL_PATH}")
        print("Place the Excel dataset in the 'dados/' folder.")
        return
    sheets = extract(EXCEL_PATH)
    tables = transform(sheets)
    load(tables, DB_PATH)
    validate(DB_PATH)
    print("\n[PIPELINE COMPLETE]")
    print(f"  Database: {DB_PATH}")
    print("  Next step: open sql-analysis.ipynb in Google Colab")


if __name__ == "__main__":
    run()
