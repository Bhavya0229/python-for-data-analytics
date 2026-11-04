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

# ==================================================
# PART 2: CONDITIONS — BUSINESS RULES
# ==================================================

#9.Customer tier
spend = 62000
#spend = 5000 tested
#100000, 49999.99, 20000 and 5000
if spend >= 100000:
    tier = 'Platinum'
elif spend >= 50000:
    tier = 'Gold'
elif spend >= 20000:
    tier = 'Silver'
elif spend < 20000:
    tier = 'Bronze'
else:
    print("Invalid tier")
print(f"Spend: {spend} ({tier})")

#10.Discount slab
purchase = 5400
#purchase = 10000  tested
#999.99, 1000, 4999.99 and 10000

if purchase < 1000:
    discount = 0
elif purchase >= 1000 and purchase < 5000:
    discount = 5
elif purchase >= 5000 and purchase < 10000:
    discount = 10
elif purchase >= 10000:
    discount = 15
else:
    print("Invalid input")

final_amount = purchase - (purchase*discount/100)
print(f"Discount: {discount}% Final Amount: {final_amount:.2f}")

#11.RAG status 
achievement = 92.4
#achievement = 89.99  tested
#100, 90 and 89.99
if achievement >= 100:
    RAG = 'Green'
elif achievement >= 90:
    RAG = 'Amber'
elif achievement < 90:
    RAG = 'Red'
else:
    print("Invalid input")
print(f"Achievement: {achievement} ({RAG})")

#12.Tax slab calculation
income = 750000
#income = 1000000 tested
#250000, 600000 and 1000000
if income <= 300000:
    tax_amount = 0
elif income > 300000 and income <= 600000:
    tax_amount = (income - 300000) * 5 / 100
elif income > 600000:
    tax_amount = (300000 * 5 / 100) + ((income - 600000) * 10 / 100)
else:
    print("Invalid input")

print(f"Tax amount: {tax_amount:.2f}")

#13.Order validation
quantity = 15
#0,-2,5  test quantities
#quantity = 5
stock = 10
payment = "Paid"
#payment = "Not Paid"  #test case
if quantity <= 0:
    print("Reject: invalid quantity")
elif quantity > stock:
    print("Reject: insufficient stock")
elif payment != 'Paid':
    print("Reject: payment failed")
else:
    print("Accept")

#14.Loan eligibility
age = 62  
#age = 50  test case
monthly_income = 40000
credit_score = 680  
#credit_score = 800  test case
if age >= 18 and age <= 60 and monthly_income >= 25000 and credit_score >= 700:
    print("Eligible")
else:
    if age < 18 or age > 60:
        print("Age is not between 18 and 60 years")
    if monthly_income < 25000:
        print("Monthly income is not atleat 25000")
    if credit_score < 700:
        print("Credit score is not atleast 700")


#15.Fiscal quarter
month = 5
#month = 12  test case
#1, 3, 4 and 12
if month >= 4 and month <= 6:
    calendar = 'Q2'
    Fiscal = 'Q1'
elif month > 6 and month <= 9:
    calendar = 'Q3'
    Fiscal = 'Q2'
elif month > 9 and month <= 12:
    calendar = 'Q4'
    Fiscal = 'Q3'
elif month >= 1 and month < 4:
    calendar = 'Q1'
    Fiscal = 'Q4'
print(f"Calendar {calendar}, Fiscal {Fiscal}")