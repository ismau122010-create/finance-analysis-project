from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from typing import Any

def _month_key(date_str: str) -> str: 

    # convert "yyyy-mm-dd" -> "yyyy-mm"

   dt = datetime.strptime(date_str.strip(), "%Y-%m-%d")
   return dt.strftime("%Y-%m")


def monthly_totals(cleaned: list[dict[str,Any]]) -> dict[str, float]:

    # return totals per month: {"2025-12": 50,30, ...}

    totals: dict[str,float] = defaultdict(float)

    for t in cleaned:
        month = _month_key(t["date"])
        totals[month]+= float(t["amount"])

# convert defaultdict -. normal dict and round 
    return {m:round(v,2) for m, v in sorted(totals.items())}


def category_totals(cleaned: list[dict[str, Any]]) -> dict[str,float]: 

    # return totals per category: {"food": 120.0, "bills": 3000.0, ...}

    totals: dict[str, float] = defaultdict(float)

    for t in cleaned:
        cat = str(t["category"]).strip().lower()
        totals[cat] += float(t["amount"])

    return {c: round(v,2) for c, v in sorted(totals.items())}    
        
