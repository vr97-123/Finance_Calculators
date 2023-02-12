##Python file: finance_calculators.py
# import the Python's math module
import math
# output menu with the given conditions
print("Investment and home loan repayment calculator.\n------------------------------------------------------------\n"
      f"investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan\n")
# request a menu option from the user, casting a string variable
menu_option = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
# assess the first character from the string entered
first_char_option = menu_option[0:1]
# apply if statements, validating the first character from the string entered
if first_char_option == "i":
    print("Investment Calculator\n------------------------------------------------------------")
    # request the different variables, casting float and integer variables 
    deposit = float(input("Please enter the amount of money that you are investing: R"))
    interest_rate = float(input("Please enter the annual interest rate (as a percentage): ")) / 100
    years = int(input("Please enter the number of years you plan on investing: "))
    # request the user to input the interest type they require to be calculated 
    interest = input("Would you require a 'simple' or 'compound' interest? ").lower()
    # assess the first character from the string entered, validating the entered option
    first_char_option1 = interest[0:1]
    if first_char_option1 == "s":
        # compute the interest calculation using simple interest formula
        type_int = "Simple interest"
        interest_calc = deposit * (1 + (interest_rate * years))
    else:
        # compute the interest calculation using compound interest formula
        type_int = "Compound interest"
        interest_calc = deposit * math.pow((1 + interest_rate), years)
    # output the results as per the validation of the above calculations,
    # formatting and tabulating the position of the results for better visualisation
    print(f"------------------------------------------------------------\nInterest calculator - {type_int} applied:\n"
          f"- Amount invested:\tR{deposit:,.2f}\n- Annual Interest rate:\t{interest_rate:,.2f}%\n"
          f"- Investment term:\t\t{years} years")
    print(f"Total of investment after the investment term:\t{interest_calc:,.2f}")
    print(f"Amount of interest on the initial investment:\t{interest_calc - deposit:,.2f}")
elif first_char_option == "b":
    print(f"Bond Repayment Calculator\n------------------------------------------------------------")
    # request the different variables, casting float and integer variables 
    house_value = float(input("Please enter the value of the house: R"))
    interest_rate = float(input("Please enter the interest rate (as a percentage): ")) / 100
    months_payback = int(input("Please enter the number of months you plan to take to repay the bond: "))
    # compute annual interest rate, followed by the calculation using the bond repayment formula
    interest_rate = interest_rate / 12
    pay_per_month = (interest_rate * house_value) / (1 - (1 + interest_rate) ** (-months_payback))
    pay_per_month = round(pay_per_month, 2)
    # output the results as per the validation of the above calculations,
    # formatting and tabulating the position of the results for better visualisation
    print(f"Bond repayment for a house with:\n- Purchase price:\tR{house_value:,.2f}\n- Interest rate:"
          f"\t{interest_rate:,.3f}%\n- Loan term:\t\t{months_payback / 12 :.0f} years")
    print(f"The total of money you will have to repay each month:\n- Monthly repayment:\tR{pay_per_month:,.2f}")
else:
    # output message when the user does not type a valid option
    print("Wrong option entered. Please enter either 'investment' or 'bond'.")
