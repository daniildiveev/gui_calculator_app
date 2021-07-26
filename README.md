# A simple GUI calculator on python

## Preamble 
I decided to create a simple calculator using python and two libraries: tkinter and pyinstaller. 

`tkinter` is used to create a GUI (graphic user interface)

`pyinstaller` is used to create a final execution file (.exe) (using this one is optional, but this will make usage easier)

## Building calculator logic

So, let's start making our calculator using `tkinter`.

```Python 
import tkinter as tk

expr = "" #this is the main variable where our whole expression will be stored

root = tk.Tk() #initializing gui
root.geometry("300x275") #setting window size

result = tk.Text(root, height=2, width=16, font=("Arial", 24)) #creating text field in gui
result.grid(columnspan=5)

```
Ok, so now, if you run `calculator.py` and get empty window, that means you have done everyting right.

For now, let's write some fucntions to help interact with our calculator: adding a symbol func, an evaluation function and clearing field function.
```Python
def add_to_expr(symbol):
    #this function will symbols to our expression
    global expr
    expr += str(symbol)
    result.delete(1.0, 'end') #clearing text field
    result.insert(1.0, expr) #writing expression to gui text field

def eval_expr():
    #this function will evaluate our expression using eval python class
    global expr
    try:
        expr = str(eval(expr))
        result.delete(1.0, 'end')
        result.insert(1.0, expr)
    except:
        clear_field()
        result.insert(1.0,'An error occured') #if some kind of error occures(eg division by 0)

def clear_field():
    #this one will clear our text field
    global expr
    expr = ''
    result.delete(1.0, 'end')
 ```
 Now that's pretty much it, all what's left is to add button.
 
 ```Python
 #adding buttons
btn_1 = tk.Button(root, text="1", command=lambda:add_to_expr("1"), width=5, font=("Arial",24))
btn_1.grid(row=2, column=0)
btn_2 = tk.Button(root, text="2", command=lambda:add_to_expr("2"), width=5, font=("Arial",24))
btn_2.grid(row=2, column=1)
btn_3 = tk.Button(root, text="3", command=lambda:add_to_expr("3"), width=5, font=("Arial",24))
btn_3.grid(row=2, column=2)
btn_4 = tk.Button(root, text="4", command=lambda:add_to_expr("4"), width=5, font=("Arial",24))
btn_4.grid(row=3, column=0)
btn_5 = tk.Button(root, text="5", command=lambda:add_to_expr("5"), width=5, font=("Arial",24))
btn_5.grid(row=3, column=1)
btn_6 = tk.Button(root, text="6", command=lambda:add_to_expr("6"), width=5, font=("Arial",24))
btn_6.grid(row=3, column=2)
btn_7 = tk.Button(root, text="7", command=lambda:add_to_expr("7"), width=5, font=("Arial",24))
btn_7.grid(row=4, column=0)
btn_8 = tk.Button(root, text="8", command=lambda:add_to_expr("8"), width=5, font=("Arial",24))
btn_8.grid(row=4, column=1)
btn_9 = tk.Button(root, text="9", command=lambda:add_to_expr("9"), width=5, font=("Arial",24))
btn_9.grid(row=4, column=2)
btn_0 = tk.Button(root, text="0", command=lambda:add_to_expr("0"), width=5, font=("Arial",24))
btn_0.grid(row=5, column=1)
btn_plus = tk.Button(root, text="+", command=lambda:add_to_expr("+"), width=5, font=("Arial",24))
btn_plus.grid(row=2, column=3)
btn_minus = tk.Button(root, text="-", command=lambda:add_to_expr("-"), width=5, font=("Arial",24))
btn_minus.grid(row=3, column=3)
btn_mul = tk.Button(root, text="*", command=lambda:add_to_expr("*"), width=5, font=("Arial",24))
btn_mul.grid(row=4, column=3)
btn_div = tk.Button(root, text="/", command=lambda:add_to_expr("/"), width=5, font=("Arial",24))
btn_div.grid(row=5, column=3)
btn_bracket_1 = tk.Button(root, text="(", command=lambda:add_to_expr("("), width=5, font=("Arial",24))
btn_bracket_1.grid(row=5, column=0)
btn_bracket_1 = tk.Button(root, text=")", command=lambda:add_to_expr(")"), width=5, font=("Arial",24))
btn_bracket_1.grid(row=5, column=2)
btn_clear = tk.Button(root, text="(", command=lambda:add_to_expr("("), width=5, font=("Arial",24))
btn_clear.grid(row=5, column=0)
btn_equals = tk.Button(root, text="C", command=clear_field(), width=5, font=("Arial",24))
btn_equals.grid(row=6, column=0,)
btn_point = tk.Button(root, text=".", command=lambda:add_to_expr("."), width=5, font=("Arial",24))
btn_point.grid(row=6, column=1)
btn_equals = tk.Button(root, text="=", command=lambda:eval_expr(), width=10, font=("Arial",24))
btn_equals.grid(row=6, column=2, columnspan=2)
```

NOTE! using `lambda` in initiliazing button is SUPER necessary.

Okay, in the end of our code we need to add `root.mainloop()`, so our code could work properly.

That is all for calculator logic, now let's create exe file.

## Creating execution file (optional)

To create exe file, we will need `pyinstaller` library, but not a regular one.

Open command line and run `!pip install https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz`, this will install the right vesrion of `pyinstaller`.

After that, go to directory (in command line), where your .py file is and run `!pip install https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz` 

Nextly, go to  `dist` directory and run `calculator.exe`.

### Enjoy!!!!
