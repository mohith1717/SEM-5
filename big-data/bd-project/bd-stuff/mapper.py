#!/usr/bin/env python3
import sys
import json

def process_store(store_data):
    city = store_data.get("city")
    categories = set(store_data.get("categories", []))
    sales_data = store_data.get("sales_data", {})
    
    total_profit = 0
    has_sales_data = False
    
    if not sales_data:
        # Skip processing if sales_data is empty
        return
    
    for category, data in sales_data.items():
        if category in categories:  # Only consider categories listed for the store
            revenue = data.get("revenue")
            cogs = data.get("cogs")
            
            if revenue is not None and cogs is not None:
                has_sales_data = True
                total_profit += revenue - cogs
    
    if has_sales_data:
        status = "profit" if total_profit > 0 else "loss"
        print(f"{city}\t{status}")

def main():
    for line in sys.stdin:
        line = line.strip()
        
        # Handle potential square brackets and trailing commas
        if line.startswith('['):
            line = line[1:].strip()
        if line.endswith(']'):
            line = line[:-1].strip()
        if line.endswith(','):
            line = line[:-1].strip()

        if not line:  # Skip empty lines
            continue
        
        try:
            store_data = json.loads(line)
            process_store(store_data)
        except json.JSONDecodeError as e:
            sys.stderr.write(f"Error decoding JSON: {e}\nProblematic line: {line}\n")
        except Exception as e:
            sys.stderr.write(f"Error processing data: {e}\nProblematic line: {line}\n")

if __name__ == "__main__":
    main()
