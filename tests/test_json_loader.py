import json
import pytest

from src.io.json_loader import load_transactions


def test_load_transactions_success(tmp_path):
    # Arrange: create a valid transactions JSON array
    p = tmp_path / "transactions.json"
    p.write_text(
        json.dumps(
            [
                {"date": "2025-12-01", "amount": 10, "category": "food", "description": "x"},
                {"date": "2025-12-02", "amount": 5.5, "category": "bills", "description": "y"},
            ]
        ),
        encoding="utf-8",
    )

    # Act
    data = load_transactions(p)

    # Assert
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["category"] == "food"


def test_load_transactions_missing_file(tmp_path):
    p = tmp_path / "does_not_exist.json"
    with pytest.raises(FileNotFoundError):
        load_transactions(p)


def test_load_transactions_not_a_list(tmp_path):
    # Arrange: JSON object instead of JSON array
    p = tmp_path / "transactions.json"
    p.write_text(json.dumps({"bad": "shape"}), encoding="utf-8")

    # Act + Assert
    with pytest.raises(ValueError):
        load_transactions(p)
