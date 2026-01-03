from src.io.json_loader import load_transactions
from src.cleaning.validator import validate_and_clean

raw = load_transactions()
cleaned = validate_and_clean(raw)

assert len(cleaned) == 3

assert cleaned[0] == {
    "date": "2025-12-01",
    "amount": 12.50,
    "category": "food",
    "description": "Tesco meal deal",
    "merchant": "Tesco"
}

assert cleaned[1] == {
    "date": "2025-12-02",
    "amount": 2.80,
    "category": "transport",
    "description": "Bus fare",
    "merchant": "First-bus"
}

assert cleaned[2] == {
    "date": "2025-12-02",
    "amount": 35.00,
    "category": "bills",
    "description": "Phone bill",
    "merchant": "Tesco"
    
}

print("\n✅ Playground checks passed!")
