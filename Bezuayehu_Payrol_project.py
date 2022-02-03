table_headers = ['Employee Name',
                 'Hours Worked',
                 'Pay Rate',
                 'Regular Pay',
                 'OT Pay',
                 'Gross Pay',
                 'Fed Tax',
                 'State Tax',
                 'FICA', 'Net Pay']
employees = []
while len(employees) < 11:
    employee_name = input("Employee Name: ")
    hours_worked = float(input("Hours Worked: "))
    pay_rate = float(input("Pay rate: "))
    print("*******************")
    regular_pay = round((hours_worked * pay_rate), 2)
    if hours_worked > 40:
        ot_pay = pay_rate * 1.5 * (hours_worked - 40)
    else:
        ot_pay = 0
    gross_pay = round((regular_pay + ot_pay), 2)
    fed_tax = round((0.1 * gross_pay), 2)
    state_tax = round((0.06 * gross_pay), 2)
    fica = round((0.03 * gross_pay), 2)
    deductible = round((fed_tax + state_tax + fica), 2)
    net_pay = round((gross_pay - deductible), 2)
    employee = employee_name, hours_worked, pay_rate, regular_pay, ot_pay, gross_pay, fed_tax, state_tax, fica, net_pay
    employees.append(employee)
row_format = "{:>15}" * (len(table_headers)+1)
print(row_format.format("Sr.No", *table_headers))
for i, row in zip(range(1, 11), employees):
    print(row_format.format(i, *row))
