import math


print ("investment - to calculate the amount of interest you'll earn on your investment\nbond - to calculate the amount you'll have to pay on a home loan")
decision = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# Allowing valid entries

if decision == "investment" or decision == "INVESTMENT" or decision == "Investment":
    print(f"Your choice is: {decision}")
elif decision == "bond" or decision == "BOND" or decision == "Bond":
    print(f"Your choice is: {decision}")
else:
    print("Please check your spelling")


# If user chooses Interest:
if decision == "investment" or decision == "INVESTMENT" or decision == "Investment":
    
    # Variables for Interest formulas:

    P = float(input("Enter the amount you are depositing: "))  # Amount the user deposits

    r = float(input("Enter the interest rate (%). Please only enter the number: "))  # Interest rate
    r = r/100

    t = float(input("Enter the number of years you want to invest: "))  # Number of years that money is invested

    interest = input("Enter whether you want 'simple' or 'compound' interest: ")  # Choice of interest type- simple or compound


    if interest == "simple" or interest == "SIMPLE" or interest == "Simple":
        print(f"You have chosen: {interest}.")
        A = P *(1 + r*t)   # formula for simple interest
        A = round (A,2)   # make A into 2 decimal places
        print(f"£{A} is the total amount you will have with interest.")
    elif interest == "compound" or interest == "COMPOUND" or interest == "Compound":
        print(f"You have chosen: {interest}.")
        A = P * math.pow((1+r),t)   # formula for compound interest
        A = round(A,2)    # make A into 2 decimal places
        print(f"£{A} is the total amount you will have with interest.")
    else: print("Please check your spelling")


# If user chooses Bond
elif decision == "bond" or decision == "BOND" or decision == "Bond":
    
    # Variables for bond formula
    
    P = float(input("Enter the present value of the house: "))  # present value of the house

    interest_rate = float(input("Enter the annual rate (%). Please only enter the number: "))
    i = interest_rate / 100 / 12  # monthly interest rate

    n = int(input("Enter the number of months the bond will be repaid over: "))

    repayment = (i * P)/(1 - (1 + i)**(-n))  # bond repayment formula
    repayment = round(repayment,2)    # make A into 2 decimal places   

    print(f"£{repayment} is the amount you have to repay each month.")

else:
    print("end")

   