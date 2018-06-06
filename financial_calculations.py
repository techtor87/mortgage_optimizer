import sys
import datetime
import Tkinter as TK
from Tkinter import StringVar

def mortgage_payoff_schedule(   start_date, mortgage_balance, 
                                mortgage_interest_rate, mortgage_payment,
                                extra_payment_amt=0):
    curr_date = start_date 
    mortgage_interest_paid = 0
    
    while mortgage_balance > 0:
        if curr_date.day == 1:
            interest_due = mortgage_balance * mortgage_interest_rate / 12
            mortgage_interest_paid += interest_due
            principle_paid = mortgage_payment - interest_due + extra_payment_amt
            mortgage_balance = mortgage_balance - principle_paid
        
        curr_date += datetime.timedelta(days=1)
    
    print "Standard Mortgage Paid Off"
    print curr_date, mortgage_balance, mortgage_interest_paid
    return curr_date, mortgage_interest_paid

def mortgage_optimize(start_date,
                        mortgage_balance, mortgage_interest_rate, 
                        mortgage_payment, mortgage_maturity, 
                        heloc_credit_limit, heloc_intereste_rate, 
                        heloc_loan_size, heloc_low_limit, 
                        monthly_cashflow):
    heloc_balance = 0
    heloc_interest_paid = 0
    mortgage_interest_paid = 0
    curr_date = start_date
    
    while mortgage_balance > 0:
    # for i in range(60):
        for i in monthly_cashflow:
            if curr_date == i[0]:
                heloc_balance += i[1]
                if i[2] == 0:
                    if i[0].month == 12:
                         i[0] = datetime.date(i[0].year+1,1,i[0].day)
                    else:
                        i[0] = datetime.date(i[0].year,i[0].month + 1,i[0].day)
                else:
                    i[0] = i[0] + datetime.timedelta(days=i[2])
                # print "HELOC cash event:", curr_date, heloc_balance, i

        if heloc_balance > heloc_low_limit and heloc_balance > heloc_credit_limit:
            if heloc_loan_size <= mortgage_balance:
                heloc_balance -= heloc_loan_size
                mortgage_balance -= heloc_loan_size
            elif heloc_loan_size > mortgage_balance:
                heloc_balance -= mortgage_balance
                mortgage_balance -= mortgage_balance
                
            # print "new HELOC loan on ", curr_date, heloc_balance

        if heloc_balance >= heloc_loan_size:
            return "HELOC Limit Reached"

        heloc_interest_paid -= heloc_balance * heloc_intereste_rate / 365
        heloc_balance += heloc_balance * heloc_intereste_rate / 365

        if curr_date.day == 1:
            interest_due = mortgage_balance * mortgage_interest_rate / 12
            mortgage_interest_paid += interest_due
            principle_paid = mortgage_payment - interest_due
            mortgage_balance = mortgage_balance - principle_paid
            # print "Mortgage Payment:", curr_date, mortgage_balance, heloc_balance
        
        curr_date += datetime.timedelta(days=1)

    print "Mortgage Paid Off"
    print curr_date, mortgage_balance, heloc_balance, mortgage_interest_paid + heloc_interest_paid
    return curr_date, mortgage_balance, heloc_balance