from src.analysis.aggregations import monthly_totals, category_totals


def test_monthly_totals_groups_by_yyyy_mm():
    cleaned = [
        {"date": "2025-12-01", "amount": 12.50, "category": "food", "description": "Tesco meal deal"},
        {"date": "2025-12-02", "amount": 2.80, "category": "transport", "description": "bus fare"},
        {"date": "2025-12-02", "amount": 35.00, "category": "bills", "description": "[hone bill]"},
    ]

    result = monthly_totals(cleaned)

    assert result == {
        "2025-12": 50.3,
        
    }


def test_category_totals_groups_and_sorts_and_rounds():
    cleaned = [
        {"date": "2025-12-01", "amount": 10.0, "category": "Food", "description": "x"},
        {"date": "2025-12-02", "amount": 2.499, "category": "food", "description": "y"},
        {"date": "2025-12-03", "amount": 7.0, "category": "bills", "description": "z"},
    ]

    result = category_totals(cleaned)

    # category_totals lowercases and sums
    assert result["food"] == 12.5  # 10 + 2.499 -> 12.499 -> 12.50 (rounded)
    assert result["bills"] == 7.0
