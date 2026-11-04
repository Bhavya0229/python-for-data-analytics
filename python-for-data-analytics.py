# ==================================================
# PYTHON FOR DATA ANALYTICS — REVISION ASSIGNMENT
# ==================================================
# Part 1: Variables, Data Types and Business Arithmetic
# Questions: Q1–Q8
# KPI variables and types

product = "Laptop"
units_sold = 12
unit_price = 55000.0
in_stock = True
print(f"Product: {product} ({type(product)})")
print(f"Units Sold: {units_sold} ({type(units_sold)})")
print(f"Unit Price: {unit_price} ({type(unit_price)})")
print(f"In Stock: {in_stock} ({type(in_stock)})")
print(f"Revenue: {units_sold*unit_price:,.2f}")

#2.Profit and margin
revenue = 125000
cost = 98500
profit = revenue - cost
profit_margin = (profit/revenue)*100.0
print(f"Profit: {profit}")
print(f"Margin: {profit_margin:.2f}%")

#3.Growth rate
last_month = 84000
this_month = 91560
#this_month = 79800  Testing
growth_rate = ((this_month - last_month)/last_month)*100.0
print(f"Growth: {growth_rate:+.2f}%")

#4.Conversion funnel
visitors = 12500
signups = 1875
purchases = 300
signup_rate = (signups/visitors)*100.0
purchase_rate = (purchases/signups)*100.0
overall_conversion = (purchases/visitors)*100.0
print(f"Signup rate: {signup_rate:.2f}%")
print(f"Purchase rate: {purchase_rate:.2f}%")
print(f"Overall: {overall_conversion:.2f}%")

#5.Text to numbers 
qty_text = "12"
price_text = "499.50"
discount_text = "10" # percent
amount_payable = (int(qty_text) * float(price_text)) * (1 - float(discount_text) / 100)
print(f"Amount Payable after discount: {amount_payable:.2f}")
print(f"qty_text * 2: {qty_text * 2}") #1212
#This is not a number because originally the type of qty_text is string and * does the repitition not calculation.

#6.Order metrics
total_revenue = 482500
orders = 160
customers = 125
average_order_value = total_revenue/orders
revenue_per_customer = total_revenue/customers
orders_per_customer = orders/customers
print(f"Average order value: {average_order_value:.2f}")
print(f"Revenue per customer: {revenue_per_customer:.2f}")
print(f"Orders per customer: {orders_per_customer:.2f}")

#7.Target versus actual
target = 500000
actual = 462000
achievement_percent = (actual/target)*100.0
shortfall_amount = target - actual
shortfall_percent = ((target-actual)/target)*100.0
print(f"Achievement Percentage: {achievement_percent:.1f}%")
print(f"Shortfall amount: {shortfall_amount:.1f}")
print(f"Shortfall Percentage: {shortfall_percent:.1f}%")

#8.Report formatting
revenue = 1234567.891
margin = 0.1834
print(f"Revenue: {revenue:,.2f}")
print(f"Margin: {margin*100:.2f}%")
print(f"Revenue rounded: {round(revenue,-3)/1000:,.0f}K")

