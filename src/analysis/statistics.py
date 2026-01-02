from __future__ import annotations

from datetime import datetime
from typing import Any


def _parse_date(date_str: str) -> datetime:
    return datetime.strptime(date_str, "%Y-%m-%d")


def basic_statistics(cleaned: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Returns a JSON-serializable dict of basic stats.
    Assumes cleaned transactions already have:
      - date: 'YYYY-MM-DD'
      - amount: float-like
      - category: str
      - description: str
    """
    n = len(cleaned)

    if n == 0:
        return {
            "count": 0,
            "total_spent": 0.0,
            "average_transaction": 0.0,
            "min_transaction": None,
            "max_transaction": None,
            "date_range": None,
        }

    amounts = [float(t["amount"]) for t in cleaned]
    total = round(sum(amounts), 2)
    avg = round(total / n, 2)

    # find min/max by amount
    min_t = min(cleaned, key=lambda t: float(t["amount"]))
    max_t = max(cleaned, key=lambda t: float(t["amount"]))

    # date range (earliest to latest)
    dates = [_parse_date(t["date"]) for t in cleaned]
    start = min(dates).strftime("%Y-%m-%d")
    end = max(dates).strftime("%Y-%m-%d")

    return {
        "count": n,
        "total_spent": total,
        "average_transaction": avg,
        "min_transaction": {
            "amount": round(float(min_t["amount"]), 2),
            "date": min_t["date"],
            "category": min_t["category"],
            "description": min_t["description"],
        },
        "max_transaction": {
            "amount": round(float(max_t["amount"]), 2),
            "date": max_t["date"],
            "category": max_t["category"],
            "description": max_t["description"],
        },
        "date_range": {"start": start, "end": end},
    }
