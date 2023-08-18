salary=input('\nEnter your Monthly Salary: ')
currency=input('Enter your Currency: ')
salary=int(salary)
salaryDay=salary/22
salaryHour=salaryDay/9
salaryDaySat=salary/26
salaryHourSat=salaryDaySat/9
print(f'\nYou make {salary} {currency} per month.')
print(f'\nYou make ~{int(salaryDay)} {currency} per day and ~{int(salaryDaySat)} {currency} with Saturdays on.')
print(f'\nYou make ~{int(salaryHour)} {currency} per hour and ~{int(salaryHourSat)} {currency} with Saturdays on.\n')