from src.cleaning.validator import validate_and_clean


def test_validate_and_clean_keeps_valid_and_normalizes():
    raw = [
        {
            "date": "2025-12-01",
            "amount": "12.5",
            "category": " Food ",
            "description": " Tesco ",
             "merchant": "Tesco"
        }
    ]

    cleaned = validate_and_clean(raw)

    assert len(cleaned) == 1
    t = cleaned[0]
    assert t["date"] == "2025-12-01"
    assert t["amount"] == 12.5
    assert t["category"] == "food"
    assert t["description"] == "Tesco"
    assert t["merchant"] == "Tesco"


def test_validate_and_clean_drops_missing_keys():
    raw = [
        {"date": "2025-12-01", "amount": 10, "category": "food"}  # missing description
    ]
    cleaned = validate_and_clean(raw)
    assert cleaned == []


def test_validate_and_clean_drops_bad_amount():
    raw = [
        {"date": "2025-12-01", "amount": "not-a-number", "category": "food", "description": "x"}
    ]
    cleaned = validate_and_clean(raw)
    assert cleaned == []


def test_validate_and_clean_drops_bad_date_format():
    raw = [
        {"date": "01-12-2025", "amount": 10, "category": "food", "description": "x"}  # wrong format
    ]
    cleaned = validate_and_clean(raw)
    assert cleaned == []


def test_validate_and_clean_rounds_amount_to_2dp():
    raw = [
        {"date": "2025-12-01", "amount": 10.129, "category": "food", "description": "x",  "merchant": "Tesco"},
    ]
    cleaned = validate_and_clean(raw)
    assert cleaned[0]["amount"] == 10.13


def test_validate_and_clean_drops_non_dict_items():
    raw = ["hello", 123, None]
    cleaned = validate_and_clean(raw)  # should not crash
    assert cleaned == []
