import tkinter as tk
from tkinter import messagebox

def apnd(thing,display):
    if (error_status.get()==True):
        error_status.set(False)
        clear()
    display.set(display.get()+ str(thing))
def operator(thing, display):
    if (error_status.get()==False and str(display.get())!="" and display.get()[-1] not in ['+','-','/','x',"(-)"]):
        apnd(thing,display)
    
       
def clear():
    display.set("")
def err(code):
    display.set("Err: " +code)
    error_status.set(True)
def negs(display,neg):
    if (display.get()[-1]in['+','-','/','x']):
        error_status=True
        apnd("(-)")
    
    
    
    
    
    
    
    
    
#post processing

#tokenization
def errCatch(s):
    ret=""
    if (s[-1] in ['+','-','/','x']):
        ret="Improper Syntax"
    for i in range(2,len(s),1):
        if (s[i-1]=='/' and s[i]==0):
            ret="Divide by Zero"
    return ret
    
def divmerge(arr):
    left = float(arr[0][1:])
    right = float(arr[1][1:])
    return arr[0][0] + str(left / right)

def multimerge(arr):
    left = float(arr[0][1:])
    right = float(arr[1][1:])
    return arr[0][0] + str(left * right)

def process(display):
    text=display.get()
    # how i will do this: tokenize operator-number pairs, combine the divisions like +4, /8 to +,4/8 then calculate the 4/8 and then merge to do +0.5
    text="+"+ text
    temp="+"
    tokens=[]
    for i in range(1, len(text),1):
        if(text[i] not in ['+','-','x','/']):
            temp+=text[i]
        else:
            tokens.append(temp)
            temp=text[i]
    tokens.append(temp)
    return tokens
def full(display):
    tokens=process(display)
    i=1
    total=0
    while (i<len(tokens)):
        if (tokens[i][0]=='/'):
            arr=[tokens[i-1],tokens[i]]
            tokens[i-1]=divmerge(arr)
            tokens.pop(i)
        else:
            i+=1
    i=1
    while (i<len(tokens)):
        if (tokens[i][0]=='x'):
            arr=[tokens[i-1],tokens[i]]
            tokens[i-1]=multimerge(arr)
            tokens.pop(i)
        else:
            i+=1
            
    print(tokens)
    for j in range(0,len(tokens),1):
        num= float(tokens[j][1:])
        if (tokens[j][0]=='+'):
            total+=num
        else:
            total-=num
    display.set(str(total))
    error_status.set(True)
    if (total>1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
        err("Screw you.")


'''  
def divmerge(arr):
    calc=str(arr[0][1:len(arr[0])-1]) + str(arr[1])
    num=0
    while (calc[num]!='/'):
        num+=1
    return arr[0][0] + str(float(calc[0:num])/float(calc[num+1:]))
def multimerge(arr):
    calc=str(arr[0][1:len(arr[0])-1]) + str(arr[1])
    num=0
    while (calc[num]!='x'):
        num+=1
    return arr[0][0] + str(float(calc[0:num])*float(calc[num+1:]))
    '''
    
    
    
    
    
    
    
    
    
app = tk.Tk()
app.title("NanoCalc V2.0")
app.geometry("300x200")
dispFrame= tk.Frame(app,padx=10)
dispFrame.pack(fill="x",expand=False)
thing = tk.Frame(app,padx=10)
thing.pack(fill="both", expand=True)
error_status=tk.BooleanVar()
error_status.set(False)
display=tk.StringVar()
display.set("")
neg=tk.BooleanVar()
neg.set(False)


disp = tk.Label(dispFrame,textvariable=display)
disp.grid(row=0, column=0, columnspan=5, pady=10,sticky="we")
b1 = tk.Button(thing, text="   1   ",command=lambda: apnd(1,display))
b1.grid(row=1,column=0)


b2 = tk.Button(thing, text="   2   ",command=lambda: apnd(2,display))
b2.grid(row=1,column=1)


b3 = tk.Button(thing, text="   3   ",command=lambda: apnd(3,display))
b3.grid(row=1,column=2)


b4 = tk.Button(thing, text="   4   ",command=lambda: apnd(4,display))
b4.grid(row=2,column=0)


b5 = tk.Button(thing, text="   5   ",command=lambda: apnd(5,display))
b5.grid(row=2,column=1)

b6 = tk.Button(thing, text="   6   ",command=lambda: apnd(6,display))
b6.grid(row=2,column=2)

b7 = tk.Button(thing, text="   7   ",command=lambda: apnd(7,display))
b7.grid(row=3,column=0)

b8 = tk.Button(thing, text="   8   ",command=lambda: apnd(8,display))
b8.grid(row=3,column=1)

b9 = tk.Button(thing, text="   9   ",command=lambda: apnd(9,display))
b9.grid(row=3,column=2)

ac = tk.Button(thing, text="   ac  ",command=lambda: clear())
ac.grid(row=4,column=0)

b0 = tk.Button(thing, text="   0   ",command=lambda: apnd(0,display))
b0.grid(row=4,column=1)

enter = tk.Button(thing, text="   =   ",command=lambda: full(display))
enter.grid(row=4,column=2)

plus =tk.Button(thing, text="+",command= lambda: operator("+", display) )
plus.grid(row=1,column=3)

minus =tk.Button(thing, text="-",command= lambda: operator("-", display) )
minus.grid(row=2,column=3)

neg =tk.Button(thing, text="(-)",command= lambda: operator("(-)", display) )
minus.grid(row=2,column=4)

multiply =tk.Button(thing, text="x",command= lambda: operator("x", display) )
multiply.grid(row=3,column=3)

divide =tk.Button(thing, text="/",command= lambda: operator("/", display) )
divide.grid(row=4,column=3)
#thing is like the grid and placement framework that we are using and then we do text="+" and command=lambada: (which basically tells the program to run the following section of code only when the button is clicked) and then the function which in our case is opperator.



app.mainloop()



