from src.io.json_loader import load_transactions
from src.cleaning.validator import validate_and_clean
from src.io.json_exporter import export_json, export_text
from src.config import cleaned_transactions
from src.config import (
    cleaned_transactions,
    monthly_summary,
    category_breakdown,
)

from src.analysis.aggregations import monthly_totals, category_totals



def main() -> None:

    # 1 load raw
    raw = load_transactions()

    # 2- clean 
    cleaned = validate_and_clean(raw)

    # save cleaned
    export_json(cleaned, cleaned_transactions)

    # analyse
    monthly = monthly_totals(cleaned)
    categories = category_totals(cleaned)

  
  # 5) Export reports (JSON)
    export_json(monthly, monthly_summary)
    export_json(categories, category_breakdown)



    print(f"loaded: {len(raw)} transactions")
    print(f"cleaned: {len(cleaned)} transactions")
    print(f"svaled cleaned file to : {cleaned_transactions}")
    print(f"saved monthly summary: {monthly_summary}")
    print(f"saved category breakdown: {category_breakdown}")

if __name__ == "__main__":
    main()    