# Created on :05 OCTOBER 2020
# Creator:Author:Victor Nkuna
# Email: victor.nkuna@yahoo.com
def tax_system():
    print("*********************WELCOME TO THE  EMPLOYEES'S TAX ADMINISTRATION SYSTEM********************")
    print()
    print("********************PYTHON ADDITIONAL EXERCISES 1:WEEK3****************")
    print()


    annual_salary = float(input("Please Enter your annual salary:\n"))

    print()

    print("I am going to ask you a few ,questions:\n")


    print()

    type_of_employee = input("Are you a Full time employee?\n")

    if type_of_employee =="Yes" or type_of_employee == "yes":

        annual_tax_amount     =  annual_salary*(0.295)

        monthly_gross_salary  =  annual_salary/12

        percentage_tax        =  (annual_tax_amount/annual_salary)*100

        monthly_tax_payable   =   annual_tax_amount/12

        net_monthly_salary    =   monthly_gross_salary - monthly_tax_payable
        print()

        print("The tax administration system will oupt the folowing variables:\n"
            "gross monthly salary,percentage tax,monthly tax payable and net monthly salary")
        print()

        print("gross monthly salary:",monthly_gross_salary, "\n")
        print()

        print("percentage tax:",percentage_tax,"\n")
        print()

        print("monthly tax payable:",monthly_tax_payable,"\n")
        print()

        print("net monthly salary:",net_monthly_salary,"\n")
        print()

    else:

        _annual_tax_amount     =  annual_salary*(0.25)

        _monthly_gross_salary  =  annual_salary/12

        _percentage_tax        =  (_annual_tax_amount/annual_salary)*100

        _monthly_tax_payable   =   _annual_tax_amount/12

        _net_monthly_salary    =   (_monthly_gross_salary) - (_monthly_tax_payable)

        print()

        print("The tax administration system will output the following variables:\n"
            "gross monthly salary,percentage tax,monthly tax payable and net monthly salary")
        print()

        print("gross monthly salary:",_monthly_gross_salary, "\n")
        print()

        print("percentage tax:",_percentage_tax,"\n")
        print()

        print("monthly tax payable:",_monthly_tax_payable,"\n")
        print()

        print("net monthly salary:",_net_monthly_salary,"\n")
        print()
tax_system()


print("***********************START OF PYTHON ADDITIONAL EXERCISES 2**************")

print()


print("""Python Additional Exercises 2""")
print()
print()

def increase_salary_by_department():

    """  The Bright Light Company is increasing the salaries of their
    employees according to their department as can be seen in dictionary object below."""


    print("############WELCOME TO BRIGHT LIGHT COMPANY ANNUAL SALARY INCREASE SYSTEM############")
    print()



    department_code  = input("PLease  enter your department code:\n")
    print()
    print()

    annual_current_salary =  float(input("Please Enter current annual salary:\n"))
    print()
    print()


    if department_code =="A":
        monthly_salary_increase_A = annual_current_salary *(1+0.072)
        print("The monthly salary  after an increase of 7.2 percent for department A is:",monthly_salary_increase_A/12)
        print()


    elif department_code=="B":
        monthly_salary_increase_B = annual_current_salary*(1+0.068)
        print("The monthly salary  after an increase of 6.8 percent for department B is:",monthly_salary_increase_B/12)


    else:
        monthly_salary_increase_other = annual_current_salary*(1+0.063)
        print("The monthly salary  after an increase of 6.3 percent for department Other is:",monthly_salary_increase_other/12)
        print()

            # if items =="Other":
            #     break
            # else:
            #     continue

increase_salary_by_department()
