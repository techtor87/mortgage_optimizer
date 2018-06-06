import sys
import datetime
import Tkinter as TK
from Tkinter import StringVar 
from graph_output import *
from input_window import *
from financial_calculations import *

def add_event(day_of_month, value, freq):
    global monthly_cashflow
    global cf_list

    monthly_cashflow.append([int(day_of_month),float(value),int(freq)])
    
    cf_list.delete(0,'end')
    for i in monthly_cashflow:
        cf_list.insert('end',i)

    var_update('run')
    return True

def remove_event(listbox_index):
    global monthly_cashflow
    global cf_list

    for i in reversed(listbox_index):
        del monthly_cashflow[i]

    cf_list.delete(0,'end')
    for i in monthly_cashflow:
        cf_list.insert('end',i)

    var_update('run')
    return True

def var_update(*args):
    global mortgage_maturity
    global mortgage_payment
    global mortgage_balance
    global mortgage_interest_rate
    global mortgage_extra_payment
    global heloc_intereste_rate
    global heloc_credit_limit
    global heloc_loan_size
    global heloc_low_limit
    global monthly_cashflow
    global start_date
    
    is_change = False
    
    for i in args:
        if i == 'run':
            is_change = True
            print 'found run'

    # if mortgage_maturity != datetime.strptime(sv_mortgage_maturity.get()strftime ):
        # mortgage_maturity = datetime.strptime(sv_mortgage_maturity.get()strftime )
        # is_change = True

    if mortgage_payment != float(sv_mortgage_payment.get()):
        mortgage_payment != float(sv_mortgage_payment.get())
        is_change = True

    if mortgage_balance != float(sv_mortgage_balance.get()):
        mortgage_balance = float(sv_mortgage_balance.get())
        is_change = True

    if mortgage_balance != float(sv_mortgage_balance.get()):
        mortgage_balance = float(sv_mortgage_balance.get())
        is_change = True

    if mortgage_extra_payment != float(sv_mortgage_extra_payment.get()):
        mortgage_extra_payment = float(sv_mortgage_extra_payment.get())
        is_change = True

    if heloc_intereste_rate != float(sv_heloc_intereste_rate.get()):
        heloc_intereste_rate = float(sv_heloc_intereste_rate.get())
        is_change = True

    if heloc_credit_limit != float(sv_heloc_credit_limit.get()):
        heloc_credit_limit = float(sv_heloc_credit_limit.get())
        is_change = True

    if heloc_loan_size != float(sv_heloc_loan_size.get()):
        heloc_loan_size = float(sv_heloc_loan_size.get())
        is_change = True

    if heloc_low_limit != float(sv_heloc_loan_size.get()):
        heloc_low_limit = float(sv_heloc_loan_size.get())
        is_change = True

    # if start_date = datetime.strptime(sv_mortgage_maturity.get()):
        # start_date = datetime.strptime(sv_mortgage_maturity.get())
        # is_change = True

    start_date = datetime.date( datetime.date.today().year,
                              datetime.date.today().month,
                              1)
    
    for i in monthly_cashflow:
        if isinstance(i[0],(int,long)):
            i[0] = start_date + datetime.timedelta(days=i[0]-1)
            is_change = True

    cf_list.delete(0,'end')
    for i in monthly_cashflow:
        cf_list.insert('end',i)

    if is_change:        
        mortgage_payoff_schedule(   start_date, mortgage_balance, 
                                    mortgage_interest_rate, mortgage_payment,mortgage_extra_payment)
            
        mortgage_optimize(  start_date, 
                            mortgage_balance, mortgage_interest_rate, 
                            mortgage_payment, mortgage_maturity, 
                            heloc_credit_limit, heloc_intereste_rate, 
                            heloc_loan_size, heloc_low_limit, 
                            monthly_cashflow)

    return

if __name__ == '__main__':  
    global mortgage_maturity
    global mortgage_payment
    global mortgage_balance
    global mortgage_interest_rate
    global mortgage_extra_payment
    global heloc_intereste_rate
    global heloc_credit_limit
    global heloc_loan_size
    global heloc_low_limit
    global monthly_cashflow
    global start_date

    global cf_list

    mortgage_maturity = datetime.date(2044,10,1)
    mortgage_payment = 1923.88 - 729.74
    mortgage_balance = 213535.32
    mortgage_interest_rate = .04125
    mortgage_extra_payment = 329.18
    heloc_intereste_rate = .0475
    heloc_credit_limit = -50000
    heloc_loan_size = 10000 
    heloc_low_limit = -2000
    monthly_cashflow = []
    start_date = datetime.date( datetime.date.today().year,
                              datetime.date.today().month,
                              1)

    monthly_cashflow = [[15,2183.08,14],
                        [8,1993.15,14],
                        [17,-5000,0],
                        [8,-1000,0],
                        [1,-2425,0]]

    input_screen = TK.Tk()
    input_screen.title("Mortgage Optimizer Inputs")
    
    sv_mortgage_maturity = StringVar()
    sv_mortgage_payment = StringVar()
    sv_mortgage_balance = StringVar()
    sv_mortgage_interest_rate = StringVar()
    sv_mortgage_extra_payment = StringVar()
    sv_heloc_intereste_rate = StringVar()
    sv_heloc_credit_limit = StringVar()
    sv_heloc_loan_size = StringVar()
    sv_heloc_low_limit = StringVar()
    # monthly_cashflow = StringVar()
    sv_start_date = StringVar()


    sv_mortgage_maturity.set(mortgage_maturity)
    sv_mortgage_payment.set(mortgage_payment)
    sv_mortgage_balance.set(mortgage_balance)
    sv_mortgage_interest_rate.set(mortgage_interest_rate)
    sv_mortgage_extra_payment.set(mortgage_extra_payment)
    sv_heloc_intereste_rate.set(heloc_intereste_rate)
    sv_heloc_credit_limit.set(heloc_credit_limit)
    sv_heloc_loan_size.set(heloc_loan_size)
    sv_heloc_low_limit.set(heloc_low_limit)
    # monthly_cashflow.set()
    sv_start_date.set(start_date)
    
    sv_mortgage_maturity.trace("w",var_update)
    sv_mortgage_payment.trace("w",var_update)
    sv_mortgage_balance.trace("w",var_update)
    sv_mortgage_interest_rate.trace("w",var_update)
    sv_mortgage_extra_payment.trace("w",var_update)
    sv_heloc_intereste_rate.trace("w",var_update)
    sv_heloc_credit_limit.trace("w",var_update)
    sv_heloc_loan_size.trace("w",var_update)
    sv_heloc_low_limit.trace("w",var_update)
    # monthly_cashflow.trace("w",var_update)
    sv_start_date.trace("w",var_update)

    # mortgage_frame = TK.Frame(input_screen).grid(row=0)
    TK.Label(input_screen,text="Mortgage Balance").grid(row=0,column=0, sticky='W')
    TK.Entry(input_screen, textvariable=sv_mortgage_balance).grid(row=0,column=1)

    TK.Label(input_screen,text="Mortgage Payment").grid(row=1,column=0, sticky='W')
    TK.Entry(input_screen, textvariable=sv_mortgage_payment).grid(row=1,column=1)

    TK.Label(input_screen,text="Mortgage Maturity").grid(row=2,column=0, sticky='W')
    TK.Entry(input_screen, textvariable=sv_mortgage_maturity).grid(row=2,column=1)

    TK.Label(input_screen,text="Mortgage Interest Rate").grid(row=3,column=0, sticky='W')
    TK.Entry(input_screen, textvariable=sv_mortgage_interest_rate).grid(row=3,column=1) 
    
    TK.Label(input_screen,text="Mortgage Extra Payment").grid(row=4,column=0, sticky='W')
    TK.Entry(input_screen, textvariable=sv_mortgage_extra_payment).grid(row=4,column=1) 
    
    # heloc_frame = TK.Frame(input_screen).pack()
    TK.Label(input_screen,text="HELOC Credit Limit").grid(row=5,column=0, sticky='W')
    TK.Entry(input_screen, textvariable=sv_heloc_credit_limit).grid(row=5,column=1)

    TK.Label(input_screen,text="HELOC Interest Rate").grid(row=6,column=0, sticky='W')
    TK.Entry(input_screen, textvariable=sv_heloc_intereste_rate).grid(row=6,column=1)

    TK.Frame(input_screen,height=10, bd=1, relief='sunken').grid(row=7)
    
    # sys_var_frame = TK.Frame(input_screen).pack()
    TK.Label(input_screen,text="HELOC Loan Size").grid(row=8,column=0, sticky='W')
    TK.Entry(input_screen, textvariable=sv_heloc_loan_size).grid(row=8,column=1)

    TK.Label(input_screen,text="HELOC Low Limit").grid(row=9,column=0, sticky='W')
    TK.Entry(input_screen, textvariable=sv_heloc_low_limit).grid(row=9,column=1)

    TK.Label(input_screen,text="Start Date").grid(row=10,column=0, sticky='W')
    TK.Entry(input_screen, textvariable=sv_start_date).grid(row=10,column=1)

    TK.Frame(input_screen,height=10, bd=1, relief='sunken').grid(row=11)

    cashflow_frame = TK.Frame(input_screen,bd=9)
    cashflow_frame.grid(row=12,column = 0, columnspan=2,sticky='WE')
    TK.Label(cashflow_frame,text="Cash Event").pack(side='left')
    cf_date = TK.Entry(cashflow_frame)
    cf_date.pack(side='left')
    cf_value = TK.Entry(cashflow_frame)
    cf_value.pack(side='left')
    cf_freq = TK.Entry(cashflow_frame)
    cf_freq.pack(side='left')

    list_frame = TK.Frame(input_screen,bd=9)
    list_frame.grid(row=13,column = 0, columnspan=2,rowspan=3,sticky='WE')
    TK.Button(list_frame,text="Add Event",command = lambda: add_event(cf_date.get(),cf_value.get(),cf_freq.get())).pack(side='left')
    TK.Button(list_frame,text="Remove Event",command = lambda: remove_event(cf_list.curselection())).pack(side='left')
    cf_list = TK.Listbox(list_frame,selectmode='multiple')
    cf_list.pack(side='right',fill='both',expand=1)
    for i in monthly_cashflow:
        cf_list.insert('end',i)

    var_update('run')

    input_screen.mainloop()

