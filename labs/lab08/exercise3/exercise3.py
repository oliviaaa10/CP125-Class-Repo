# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:
import csv
def calculate_order_total(products_file, order_file, output_file):
    prices = {}

    f_product = open(products_file, "r")
    reader = csv.reader(f_product)
    next(reader)

    for row in reader :
        prices[row[0]] = float(row[2])

    f_product.close()

    grand_total = 0

    f_order = open(order_file, "r", newline= "" )
    order_reader = csv.reader(f_order)

    f_out = open(output_file, "w", newline= "")
    writer = csv.writer(f_out)

    writer.writerow(["product_id", "total_cost"])

    next(order_reader)


    for row in order_reader :
        product_id = row[0]
        quantity = int(row[1])
        total_cost = prices[product_id] * quantity

        writer.writerow([product_id, "{:.2f}".format(total_cost)])

        grand_total += total_cost

    
    f_order.close()
    f_out.close()

    return grand_total


# Test your code here
result = calculate_order_total("labs/lab08/exercise3/data/products.csv", "labs/lab08/exercise3/data/order.csv", ";abs/lab08/exercise3/data/total.csv")
print(f"Grand total: ${result:.2f}")
