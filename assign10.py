import webbrowser as wb
from tkinter import * 
obj=Tk(className=" Zayed_Assign_10")
e=Entry(obj,font=("",30))
e.grid(row= 500,column=500)
def navigate():
    query=e.get()
    wb.open("https://www.youtube.com/search?q="+query)
    print("Navigating To-> ",query)
b=Button(obj,text="Search",
         anchor="center",
         command=navigate,
         font=("",30))
b.grid(row= 500,column=1000)
b1=Button(obj,text="Close",
          anchor="center",
         command=obj.destroy,
         font=("",30))
b1.grid(row= 500,column=1500)
obj.mainloop()