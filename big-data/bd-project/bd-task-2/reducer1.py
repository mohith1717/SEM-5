#!/usr/bin/env python3
import sys

def process_input():

    product_prices = {}
    customer_purchases = []

    for line in sys.stdin:
        line = line.strip()
        parts = line.split()

        if len(parts) == 2:

            product_id = parts[0]
            price = float(parts[1])
            product_prices[product_id] = price
            
        elif len(parts) == 4:
          
            product_id = parts[0]
            customer_id = parts[1]
            points = int(parts[2])
            quantity = int(parts[3])
            customer_purchases.append((customer_id, points, product_id, quantity))

    return product_prices, customer_purchases

def calculate_total_cost(product_prices, customer_purchases):
  
    for customer_id, points, product_id, quantity in customer_purchases:
        if product_id in product_prices:
            price = product_prices[product_id]
            total_cost = price * quantity
            yield f"{customer_id} {points} {total_cost}"

def main():
    
    product_prices, customer_purchases = process_input()

    for result in calculate_total_cost(product_prices, customer_purchases):
        print(result)

if __name__ == "__main__":
    main()
