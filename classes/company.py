from employee import Employee

class Company:
    def __init__(self):
        self.employees =[]
        
    def add_employees(self, new_employee):
        self.employees.append(new_employee)
        
    def display_employees(self):
        print('Current Employees:')
        for i in self.employees:
            print(i.fname, i.lname)
        print('_________________________')
    
    def pay_employees(self):
        print('Paying employees')
        for i in self.employees:
            print('Paycheck for:', i.fname, i.lname)
            #f string to format the numbers -- ,.2f (floats rouding to 2 decimal places)
            print(f'Amount: ${i.calculate_paycheck():,.2f}')
            print('__________________')
            

def main():
    my_company = Company()
    
    employee1 = Employee('Sarah', 'Hess', 50000)
    my_company.add_employees(employee1)
    employee2 = Employee('Sarita', 'Ness', 80000)
    my_company.add_employees(employee2)
    
    my_company.display_employees()
    my_company.pay_employees()

main()