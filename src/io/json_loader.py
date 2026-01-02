import json
from typing import Any
from src.config import raw_transactions

def load_transactions(path=raw_transactions) -> list[dict[str,Any]]:
                                                                   
   # load transactions from a Json file and return a list of dicts. 

   if not path.exists():
      raise FileNotFoundError(f"missing file: {path}")
   
   data = json.loads(path.read_text(encoding= "utf-8"))

   if not isinstance(data, list):
      raise ValueError("transactions.json must contain a json array (a list).")
   
   return data


                    
                              

                                                                               




