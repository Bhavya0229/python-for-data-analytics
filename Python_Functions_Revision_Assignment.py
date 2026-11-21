# Python Functions – Revision Assignment
# Focus: Python for Data Analytics
# Purpose: Practise reusable functions through
# practical business and data analysis scenarios.

# Section 1: Basic Functions, Parameters and Return

# Task 1: Calculate total and average daily revenue
daily_revenue = [12500, 18000, 14500, 22000, 16000, 19500]
def analyze_revenue(revenue_list):
    total_revenue = 0
    for revenue in revenue_list:
        total_revenue += revenue
    avg_revenue = total_revenue/len(revenue_list)
    return total_revenue,avg_revenue
result = analyze_revenue(daily_revenue)
print(result)

#Task 2: Calculate discounted product price using a default parameter
def calculate_discounted_price(original_price,discount_percentage = 10):
    final_price = original_price - original_price*discount_percentage/100
    return final_price
result = calculate_discounted_price(5000,20)
print(result)
result1 = calculate_discounted_price(8000)
print(result1)

#Task 3: Calculate employee bonus using keyword arguments
def calculate_bonus(salary,bonus_percentage):
    bonus_amount = salary*bonus_percentage/100
    return bonus_amount
result = calculate_bonus(salary=60000,bonus_percentage=15)
print(result)

# Task 4: Understanding variable scope

company_name = "ABC Retail"
monthly_revenue = 150000

def display_business_report():
    monthly_expenses = 90000
    profit = monthly_revenue - monthly_expenses

    print(company_name)
    print(profit)

display_business_report()

# Answers:
# 1. Global variables: company_name and monthly_revenue
# 2. Local variables: monthly_expenses and profit
# 3. profit cannot normally be accessed outside the function
#    because it is a local variable.

#Task 5: Calculate total revenue from multiple branches using *args
def calculate_total_branch_revenue(*args):
    total_revenue = sum(args)
    return total_revenue

result = calculate_total_branch_revenue(25000, 30000, 18000)
result1 = calculate_total_branch_revenue(15000, 22000, 28000, 35000, 19000)
print(result)
print(result1)

#Task 6: Display store report using **kwargs
def display_store_report(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

display_store_report(
    store_name = "Ludhiana Central",
    manager = "Rahul",
    monthly_sales = 250000,
    employees = 18,
    rating = 4.5
)

#Task 7: Calculate total monthly sales by passing a list
monthly_sales = [45000, 52000, 38000, 61000, 49000]

def calculate_monthly_sales(sales_list):
    total_sales = 0
    for sale in sales_list:
        total_sales += sale
    return total_sales
result = calculate_monthly_sales(monthly_sales)
print(result)
# Concept: The parameter refers to the same list object.

#Task 8: Update daily orders without modifying the original list
daily_orders = [120, 150, 180, 200]
def update_daily_orders(orders_list):
    new_orders_list = orders_list.copy()
    new_orders_list.append(250)
    return new_orders_list
result = update_daily_orders(daily_orders)
print("Original:", daily_orders)
print("Updated:", result)

#Task 9: Classify hospital appointment waiting times
def classify_waiting_time(waiting_minutes):
    if waiting_minutes <= 15:
        return "Short Wait"
    elif waiting_minutes <= 30:
        return "Moderate Wait"
    else:
        return "Long Wait"

result = classify_waiting_time(12)
result1 = classify_waiting_time(25)
result2 = classify_waiting_time(45)
print(result)
print(result1)
print(result2)

#Task 10: Count delayed shipments using a loop and conditional logic
delivery_times = [18, 26, 32, 15, 41, 29, 12, 38]
def count_delayed_shipments(delivery_list):
    delayed_shipment_count = 0
    for time in delivery_list:
        if time > 30:
            delayed_shipment_count += 1
    return delayed_shipment_count
result = count_delayed_shipments(delivery_times)
print(result)

#Task 11: Filter completed hospital appointments using a function
appointments = [
    {"PatientID": 101, "Department": "Cardiology", "Status": "Completed"},
    {"PatientID": 102, "Department": "Neurology", "Status": "Cancelled"},
    {"PatientID": 103, "Department": "Cardiology", "Status": "Completed"},
    {"PatientID": 104, "Department": "Orthopaedics", "Status": "Pending"},
    {"PatientID": 105, "Department": "Neurology", "Status": "Completed"},
    {"PatientID": 106, "Department": "Cardiology", "Status": "Cancelled"}
]

def get_completed_appointments(appointment_list):
    completed_appointments = []
    for record in appointment_list:
        if record["Status"] == "Completed":
            completed_appointments.append(record)
    return completed_appointments
result = get_completed_appointments(appointments)
print(result)        

#Task 12: Filter employees based on department and experience
employees = [
    {"Name": "Aarav", "Experience": 3, "Department": "IT"},
    {"Name": "Priya", "Experience": 5, "Department": "Finance"},
    {"Name": "Rahul", "Experience": 2, "Department": "IT"},
    {"Name": "Neha", "Experience": 6, "Department": "HR"},
    {"Name": "Amit", "Experience": 4, "Department": "IT"}
]

def filter_eligible_employees(employee_list,required_department,minimum_experience):
    eligible_employees = []
    for employee in employee_list:
        if employee["Department"] == required_department and employee["Experience"] >= minimum_experience:
            eligible_employees.append(employee)
    return eligible_employees
result = filter_eligible_employees(employees, "IT", 3)
print(result)

#Task 13: Calculate delivered shipment costs by region
shipments = [
    {"ShipmentID": 501, "Region": "North", "Cost": 2500, "Status": "Delivered"},
    {"ShipmentID": 502, "Region": "South", "Cost": 1800, "Status": "Pending"},
    {"ShipmentID": 503, "Region": "North", "Cost": 3200, "Status": "Delivered"},
    {"ShipmentID": 504, "Region": "West", "Cost": 2100, "Status": "Cancelled"},
    {"ShipmentID": 505, "Region": "South", "Cost": 2800, "Status": "Delivered"},
    {"ShipmentID": 506, "Region": "North", "Cost": 1500, "Status": "Pending"}
]

def calculate_delivered_shipment_cost(shipment_list,required_region):
    total_delivered_cost = 0
    for shipment in shipment_list:
        if shipment["Status"] == "Delivered" and shipment["Region"] == required_region:
            total_delivered_cost += shipment["Cost"]
    return total_delivered_cost
result = calculate_delivered_shipment_cost(shipments,"North")
print(result)

#Task 14: Calculate total inspected and defective products
# using multiple return values and tuple unpacking
inspection_results = [
    {"BatchID": 701, "Inspected": 100, "Defective": 5},
    {"BatchID": 702, "Inspected": 150, "Defective": 12},
    {"BatchID": 703, "Inspected": 120, "Defective": 8},
    {"BatchID": 704, "Inspected": 130, "Defective": 10}
]

def analyze_quality(inspection_list):
    inspected_count = 0
    defective_count = 0
    for product in inspection_list:
        inspected_count += product["Inspected"]
        defective_count += product["Defective"]
    return inspected_count,defective_count
total_inspected,total_defective = analyze_quality(inspection_results)
print(f"Total Inspected: {total_inspected}")
print(f"Total Defective: {total_defective}")

#Task 15: Analyse successful bank transactions using a dictionary return
transactions = [
    {"TransactionID": 801, "Account": "Savings", "Amount": 5000, "Status": "Successful"},
    {"TransactionID": 802, "Account": "Current", "Amount": 8000, "Status": "Failed"},
    {"TransactionID": 803, "Account": "Savings", "Amount": 3500, "Status": "Successful"},
    {"TransactionID": 804, "Account": "Savings", "Amount": 2000, "Status": "Failed"},
    {"TransactionID": 805, "Account": "Current", "Amount": 6000, "Status": "Successful"},
    {"TransactionID": 806, "Account": "Savings", "Amount": 4500, "Status": "Successful"}
]

def analyze_transactions(transaction_list,required_account):
    total_successful_transaction = 0
    successful_transaction_count = 0
    for amount in transaction_list:
        if amount["Account"] == required_account and amount["Status"] == "Successful":
            total_successful_transaction += amount["Amount"]
            successful_transaction_count += 1
    if successful_transaction_count > 0:
        avg_successful_transaction = total_successful_transaction/successful_transaction_count
        return {
            "TotalAmount": total_successful_transaction,
            "TransactionCount": successful_transaction_count,
            "AverageAmount": avg_successful_transaction
        }
    else:
        return{
            "TotalAmount":0,
            "TransactionCount":0,
            "AverageAmount":0
        }
result = analyze_transactions(transactions,"Savings")
print(result)

#Task 16: Combine functions to calculate confirmed booking revenue
hotel_bookings = [
    {"BookingID": 901, "Hotel": "Sunrise", "Amount": 8500, "Status": "Confirmed"},
    {"BookingID": 902, "Hotel": "Lake View", "Amount": 6200, "Status": "Cancelled"},
    {"BookingID": 903, "Hotel": "Sunrise", "Amount": 10500, "Status": "Confirmed"},
    {"BookingID": 904, "Hotel": "Mountain Stay", "Amount": 7500, "Status": "Pending"},
    {"BookingID": 905, "Hotel": "Lake View", "Amount": 9000, "Status": "Confirmed"}
]

def get_confirmed_bookings(booking_list):
    confirmed_bookings = []
    for booking in booking_list:
        if booking["Status"] == "Confirmed":
            confirmed_bookings.append(booking)
    return confirmed_bookings

def calculate_booking_revenue(booking_list):
    total_booking_revenue = 0
    for booking in booking_list:
        total_booking_revenue += booking["Amount"]
    return total_booking_revenue

result = get_confirmed_bookings(hotel_bookings)
print(result)
result1 = calculate_booking_revenue(result)
print(result1)

#Hospital Performance Analysis
appointments = [
    {"AppointmentID": 1001, "Department": "Cardiology", "Fee": 1200, "Status": "Completed"},
    {"AppointmentID": 1002, "Department": "Dermatology", "Fee": 800, "Status": "Completed"},
    {"AppointmentID": 1003, "Department": "Cardiology", "Fee": 1500, "Status": "Cancelled"},
    {"AppointmentID": 1004, "Department": "Cardiology", "Fee": 1000, "Status": "Completed"},
    {"AppointmentID": 1005, "Department": "Paediatrics", "Fee": 900, "Status": "Completed"},
    {"AppointmentID": 1006, "Department": "Cardiology", "Fee": 1300, "Status": "Completed"},
    {"AppointmentID": 1007, "Department": "Dermatology", "Fee": 700, "Status": "Cancelled"},
    {"AppointmentID": 1008, "Department": "Cardiology", "Fee": 1100, "Status": "Completed"}
]

def get_department_appointments(appointment_list, required_department):
    completed_appointments = []
    for appointment in appointment_list:
        if appointment["Department"] == required_department and appointment["Status"] == "Completed":
            completed_appointments.append(appointment)
    return completed_appointments

result = get_department_appointments(appointments,"Cardiology") 
print(result)
        
def calculate_department_revenue(appointment_list):
    total_fees = 0
    count_appointments = 0
    for appointment in appointment_list:
        total_fees += appointment["Fee"]
        count_appointments += 1
    return total_fees,count_appointments
result1 = calculate_department_revenue(result)
print(result1)

def generate_department_report(appointment_list, required_department):
    filtered_appointments = get_department_appointments(appointment_list, required_department)
    total_fees, appointment_count = calculate_department_revenue(filtered_appointments)
    if appointment_count > 0:
        avg_appointment_fee = total_fees/appointment_count
        return{
            "Department": required_department,
            "TotalAppointments": appointment_count,
            "TotalRevenue": total_fees,
            "AverageFee": avg_appointment_fee
        }
    else:
        return{
            "Department": required_department,
            "TotalAppointments": 0,
            "TotalRevenue": 0,
            "AverageFee": 0
        }
report = generate_department_report(appointments, "Cardiology")
print(report)
report1 = generate_department_report(appointments, "Neurology")
print(report1)