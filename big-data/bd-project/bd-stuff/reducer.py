#!/usr/bin/env python3
import sys
import json

def main():
    city_data = {}

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        try:
            city, status = line.split('\t')

            if city not in city_data:
                city_data[city] = {"profit_stores": 0, "loss_stores": 0}

            if status == "profit":
                city_data[city]["profit_stores"] += 1
            elif status == "loss":
                city_data[city]["loss_stores"] += 1

        except ValueError as e:
            sys.stderr.write(f"Error processing line: {line} - {e}\n")

    # Output the aggregated results
    for city, data in city_data.items():
        print(json.dumps({
            "city": city,
            "profit_stores": data["profit_stores"],
            "loss_stores": data["loss_stores"]
        }))

if __name__ == "__main__":
    main()
