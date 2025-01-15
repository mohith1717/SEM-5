#!/usr/bin/env python3

import sys

def calculate_discounted_price(points, total_cost):
    if points < 100:
        discount = 0
    elif 100 <= points < 200:
        discount = 0.10
    elif 200 <= points < 300:
        discount = 0.20
    elif 300 <= points < 400:
        discount = 0.30
    else:
        discount = 0.40

    final_price = total_cost * (1 - discount)
    return round(final_price, 3)


def process_input():
    customer_totals = {}

    for line in sys.stdin:
        line = line.strip()
        parts = line.split()

        if len(parts) == 3:
            customer_id = parts[0]
            points = int(parts[1])
            total_cost = float(parts[2])

            final_price = calculate_discounted_price(points, total_cost)
            if customer_id in customer_totals:
                customer_totals[customer_id] += final_price
            else:
                customer_totals[customer_id] = final_price

    return customer_totals


def main():
    customer_totals = process_input()
    for customer_id, total in sorted(customer_totals.items()):
        print(f"{customer_id} {total:.1f}")


if __name__ == "__main__":
    main()
