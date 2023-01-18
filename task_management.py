def calculate_tax(price, is_exempt, is_imported):
    tax_rate = 0
    if is_exempt:
        tax_rate += 0
    else:
        tax_rate += 10
    if is_imported:
        tax_rate += 5
    tax = round(price * (tax_rate/100), 2)
    return tax

def calculate_cost(price, is_exempt, is_imported):
    tax = calculate_tax(price, is_exempt, is_imported)
    total_cost = round(price + tax, 2)
    return total_cost

def print_receipt(basket):
    total_sales_tax = 0
    total_cost = 0
    for item in basket:
        item_name = item[0]
        item_price = item[1]
        is_exempt = item[2]
        is_imported = item[3]
        item_tax = calculate_tax(item_price, is_exempt, is_imported)
        item_total_cost = calculate_cost(item_price, is_exempt, is_imported)
        total_sales_tax += item_tax
        total_cost += item_total_cost
        print(f"{item_name}: {item_total_cost}")
    print(f"Sales Taxes: {total_sales_tax}")
    print(f"Total: {total_cost}")

basket1 = [("book", 12.49, True, False), ("music CD", 14.99, False, False), ("chocolate bar", 0.85, True, False)]
basket2 = [("imported box of chocolates", 10.00, True, True), ("imported bottle of perfume", 47.50, False, True)]
basket3 = [("imported bottle of perfume", 27.99, False, True), ("bottle of perfume", 18.99, False, False), ("packet of headache pills", 9.75, True, False), ("box of imported chocolates", 11.25, True, True)]

print_receipt(basket1)
print('-----------------------------------')
print_receipt(basket2)
print('-----------------------------------')
print_receipt(basket3)
