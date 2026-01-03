from datetime import datetime
from typing import Any

REQUIRED_KEYS = {"date", "amount","category", "description", "merchant"}

def _is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    

def validate_and_clean(transactions):
    cleaned = []


    for t  in transactions:
        # must be a dictionary
        if not isinstance(t,dict):
            continue     # if its not a dictionary skip it the data input. 

 
        #  this will check if the all required keys present if not it will skip. 
        if not REQUIRED_KEYS.issubset(t.keys()):     
            continue

        date = str(t["date"]).strip()    # turn the date to a string and remove any spaces.
        category = str(t["category"]).strip().lower()   # turn category to string and must be lower cases and without any spaces. 
        description = str(t["description"]).strip()       # simalr concept above
        mercahnt = str(t["merchant"]).strip()

       # amount must be a number 
        try:
           amount = float(t["amount"])
        except (TypeError,ValueError):
          continue
    

    # date format check
        if not _is_valid_date(date):
         continue

        cleaned.append(
           {
           "date": date,
           "amount": round(amount,2),
           "category": category,
           "description": description,
           "merchant": mercahnt,
        }
        )
    return cleaned

    
    








