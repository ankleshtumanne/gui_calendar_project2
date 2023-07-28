from tkinter import *   # we import the libarary 
from tkcalendar import * # we import calender library 

root=Tk()                      #call the libraryes
root.geometry("300x300")       # it will give you shape and size of the calendar 
root.title("Calender")          # showing the tittle 
root.configure(bg="lightblue")   # using for background 


def selectDate():      # create a function for select any date , if user want according to him/her
    myDate=mycal.get_date() # we gateing date for these lines 
    selectDate=Label(text=myDate) # it will  be given "Select date"
    selectDate.pack(padx=2,pady=2)

mycal=Calendar(root, setmode="Day",date_pattern='D/M/Y') # these lines give formate of date/month/year 
mycal.pack(padx=15,pady=15)

open_cal=Button(root,text="Select Date",command=selectDate) # here call the fuction 
open_cal.pack(padx=15,pady=15) # pack ka matlab hai ki open call ke ander jitna bhi data h vo 1 packate ke ander store h


root .mainloop()

