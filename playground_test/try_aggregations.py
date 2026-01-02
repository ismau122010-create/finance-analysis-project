from src.analysis.aggregations import _month_key, monthly_totals, category_totals

cleaned = [
    {"date": "2025-12-01", "amount": 10.0, "category": " Food "},
    {"date": "2025-12-31", "amount": 5.25, "category": "food"},
    {"date": "2026-01-01", "amount": 2.0, "category": "Bills"},
]

print("month_key:",_month_key("2025-12-18"))
print("monthly_totals:", monthly_totals(cleaned))
print("category_totals:", category_totals(cleaned))
