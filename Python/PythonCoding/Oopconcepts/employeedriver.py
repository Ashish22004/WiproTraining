from Oopconcepts.EmployeeDetails import EmployeeDetails

# Driver
eno = int(input('Emp No :'))
name = input('Emp name :')
bp = float(input('basic pay :'))

employee = EmployeeDetails(empno=eno, ename=name, basicpay=bp)

print('salary :', employee.calculate_netsal())
print('Emp name :', employee.ename)
print('Emp no :', employee.empno)
