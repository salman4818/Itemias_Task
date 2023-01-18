# Itemias_Task
The above code is a Python program that calculates the sales tax and total cost of items in a basket, and then prints out a receipt with the item names, costs, total sales tax, and total cost.
The code defines 3 functions:

calculate_tax(price, is_exempt, is_imported): This function takes in the price of an item, and whether the item is exempt from sales tax and/or imported, and calculates the sales tax on the item.
calculate_cost(price, is_exempt, is_imported): This function takes in the same inputs as the calculate_tax function, and calculates the total cost of the item (price + sales tax).
print_receipt(basket): This function takes in a list of items in the basket, where each item is a tuple containing the item name, price, whether it's exempt from sales tax, and whether it's imported. The function calculates the sales tax and total cost for each item, and keeps a running total of the sales tax and total cost for the entire basket. It then prints out a receipt with the item names, costs, total sales tax, and total cost.
The code also includes examples of using the print_receipt function on 3 different baskets of items.

To run the code, simply call the print_receipt() function with a basket of items as its argument. The receipt will be printed out in the console.
