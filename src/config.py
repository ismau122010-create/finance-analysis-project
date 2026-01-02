from pathlib import Path

project_root = Path(__file__).resolve().parents[1]

raw_transactions = project_root/ "data" / "raw" / "transactions.json"
cleaned_transactions = project_root / "data" / "cleaned" / "cleaned_transactions.json"

reports_dir = project_root / "data" / "reports"
monthly_summary = reports_dir / "monthly_summary.json"




