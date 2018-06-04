import sys
import datetime
import Tkinter as TK
from Tkinter import StringVar 

class my_datetime(datetime.datetime):
    def current_month(self):
        self = datetime.date( datetime.date.today().year,
                              datetime.date.today().month,
                              1)
    def next_day(self):
        self += datetime.timedelta(days=1)
        
    def next_month(self):
        if self.month != 12:
            self = datetime.date(self.year,self.month + 1,self.day)
        else:
            self = datetime.date(self.year+1,1,self.day)
            
def mortgage_payoff_schedule(   start_date, mortgage_balance, 
                                mortgage_interest_rate, mortgage_payment,
                                extra_payment_amt=0):
    curr_date = start_date 
    mortgage_interest_paid = 0
    
    while mortgage_balance > 0:
        if curr_date.day == 1:
            interest_due = mortgage_balance * mortgage_interest_rate
            mortgage_interest_paid += interest_due
            principle_paid = mortgage_payment - interest_due + extra_payment_amt
            mortgage_balance = mortgage_balance - principle_paid
        
        curr_date += datetime.timedelta(days=1)
    
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

        heloc_interest_paid -= heloc_balance * heloc_intereste_rate
        heloc_balance += heloc_balance * heloc_intereste_rate

        if curr_date.day == 1:
            interest_due = mortgage_balance * mortgage_interest_rate
            mortgage_interest_paid += interest_due
            principle_paid = mortgage_payment - interest_due
            mortgage_balance = mortgage_balance - principle_paid
            # print "Mortgage Payment:", curr_date, mortgage_balance, heloc_balance
        
        curr_date += datetime.timedelta(days=1)

    print "Mortgage Paid Off"
    print curr_date, mortgage_balance, mortgage_interest_paid, heloc_balance, heloc_interest_paid
    return curr_date, mortgage_balance, heloc_balance

def add_event(date, value, freq):
    global monthly_cashflow

    print date, value, freq
    return True

if __name__ == '__main__':
    # global mortgage_maturity
    # global mortgage_payment
    # global mortgage_balance
    # global mortgage_interest_rate
    # global heloc_intereste_rate
    # global heloc_credit_limit
    # global heloc_loan_size
    # global heloc_low_limit
    # global monthly_cashflow
    # global start_date

    # mortgage_maturity = 
    # mortgage_payment = 1923.88 - 729.74
    # mortgage_balance = 213535.32
    # mortgage_interest_rate = .04125 / 12
    # heloc_intereste_rate = .0475 / 365
    # heloc_credit_limit = -50000
    # heloc_loan_size = 10000 
    # heloc_low_limit = -2000
    # monthly_cashflow = []
    # start_date = datetime.date( datetime.date.today().year,
    #                           datetime.date.today().month,
    #                           1)

    monthly_cashflow = [[15,2183.08,14],
                        [8,1993.15,14],
                        [17,-5000,0],
                        [8,-1000,0],
                        [1,-2425,0]]

    input_screen = TK.Tk()
    input_screen.title("Mortgage Optimizer Inputs")
    
    mortgage_maturity = StringVar()
    mortgage_payment = StringVar()
    mortgage_balance = StringVar()
    mortgage_interest_rate = StringVar()
    mortgage_extra_payment = StringVar()
    heloc_intereste_rate = StringVar()
    heloc_credit_limit = StringVar()
    heloc_loan_size = StringVar()
    heloc_low_limit = StringVar()
    monthly_cashflow = StringVar()
    start_date = StringVar()

    mortgage_maturity.set(datetime.date(2044,10,1))
    mortgage_payment.set(1923.88 - 729.74)
    mortgage_balance.set(213535.32)
    mortgage_interest_rate.set(.04125)
    mortgage_extra_payment.set( 329.18)
    heloc_intereste_rate.set(.0475)
    heloc_credit_limit.set(-50000)
    heloc_loan_size.set(10000)
    heloc_low_limit.set(-2000)
    # monthly_cashflow.set()
    start_date.set(datetime.date( datetime.date.today().year,
                              datetime.date.today().month,
                              1))

    # mortgage_frame = TK.Frame(input_screen).grid(row=0)
    TK.Label(input_screen,text="Mortgage Balance").grid(row=0,column=0, sticky='W')
    TK.Entry(input_screen, textvariable=mortgage_balance).grid(row=0,column=1)

    TK.Label(input_screen,text="Mortgage Payment").grid(row=1,column=0, sticky='W')
    TK.Entry(input_screen, textvariable=mortgage_payment).grid(row=1,column=1)

    TK.Label(input_screen,text="Mortgage Maturity").grid(row=2,column=0, sticky='W')
    TK.Entry(input_screen, textvariable=mortgage_maturity).grid(row=2,column=1)

    TK.Label(input_screen,text="Mortgage Interest Rate").grid(row=3,column=0, sticky='W')
    TK.Entry(input_screen, textvariable=mortgage_interest_rate).grid(row=3,column=1) 
    
    TK.Label(input_screen,text="Mortgage Extra Payment").grid(row=4,column=0, sticky='W')
    TK.Entry(input_screen, textvariable=mortgage_extra_payment).grid(row=4,column=1) 
    
    # heloc_frame = TK.Frame(input_screen).pack()
    TK.Label(input_screen,text="HELOC Credit Limit").grid(row=5,column=0, sticky='W')
    TK.Entry(input_screen, textvariable=heloc_credit_limit).grid(row=5,column=1)

    TK.Label(input_screen,text="HELOC Interest Rate").grid(row=6,column=0, sticky='W')
    TK.Entry(input_screen, textvariable=heloc_intereste_rate).grid(row=6,column=1)

    TK.Frame(input_screen,height=10, bd=1, relief='sunken').grid(row=7)
    
    # sys_var_frame = TK.Frame(input_screen).pack()
    TK.Label(input_screen,text="HELOC Loan Size").grid(row=8,column=0, sticky='W')
    TK.Entry(input_screen, textvariable=heloc_loan_size).grid(row=8,column=1)

    TK.Label(input_screen,text="HELOC Low Limit").grid(row=9,column=0, sticky='W')
    TK.Entry(input_screen, textvariable=heloc_low_limit).grid(row=9,column=1)

    TK.Label(input_screen,text="Start Date").grid(row=10,column=0, sticky='W')
    TK.Entry(input_screen, textvariable=start_date).grid(row=10,column=1)

    TK.Frame(input_screen,height=10, bd=1, relief='sunken').grid(row=11)

    cashflow_frame = TK.Frame(input_screen,bd=9)
    cashflow_frame.grid(row=12,column = 0, columnspan=2,rowspan=3,sticky='WE')
    TK.Label(cashflow_frame,text="Cash Event").pack(side='left')
    cf_date = TK.Entry(cashflow_frame)
    cf_date.pack(side='left')
    cf_value = TK.Entry(cashflow_frame)
    cf_value.pack(side='left')
    cf_freq = TK.Entry(cashflow_frame)
    cf_freq.pack(side='left')
    TK.Button(cashflow_frame,text="Add Event",command = lambda: add_event(cf_date.get(),cf_value.get(),cf_freq.get())).pack(side='left')
    TK.Button(cashflow_frame,text="Remove Event").pack(side='bottom')
    TK.Listbox(cashflow_frame,selectmode='single').pack(side='bottom')
    input_screen.mainloop()

    # for i in monthly_cashflow:
    #     i[0] = curr_date + datetime.timedelta(days=i[0]-1)
        
    # print mortgage_payoff_schedule(   curr_date, mortgage_balance, 
    #                             mortgage_interest_rate, mortgage_payment,mortgage_extra_payment)
        
    # mortgage_optimize(  curr_date, 
    #                     mortgage_balance, mortgage_interest_rate, 
    #                     mortgage_payment, mortgage_maturity, 
    #                     heloc_credit_limit, heloc_intereste_rate, 
    #                     heloc_loan_size, heloc_low_limit, 
    #                     monthly_cashflow)