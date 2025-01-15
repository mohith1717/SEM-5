#!/usr/bin/env python3
import sys

def process_input():
  
    customer_totals = {}

    for line in sys.stdin:
        line = line.strip()
        parts = line.split()

        if len(parts) == 3:
            customer_id = parts[0]
            points = int(parts[1])
            total_cost = float(parts[2])

            if customer_id not in customer_totals:
                customer_totals[customer_id] = (points, total_cost)
            else:
                current_points, current_total = customer_totals[customer_id]
                customer_totals[customer_id] = (current_points, current_total + total_cost)

    for customer_id, (points, total_cost) in customer_totals.items():
        print(f"{customer_id} {points} {total_cost:.3f}")

def main():
   
    process_input()

if __name__ == "__main__":
    main()
