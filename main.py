import tkinter as tk

expr = ""

def add_to_expr(symbol):
    global expr
    expr += str(symbol)
    result.delete(1.0, 'end')
    result.insert(1.0, expr)

def eval_expr():
    global expr
    try:
        expr = str(eval(expr))
        result.delete(1.0, 'end')
        result.insert(1.0, expr)
    except:
        clear_field()
        result.insert(1.0,'An error occured')

def clear_field():
    global expr
    expr = ''
    result.delete(1.0, 'end')

root = tk.Tk()
root.geometry("300x275")

result = tk.Text(root, height=2, width=16, font=("Arial", 32))
result.grid(columnspan=5)

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

root.mainloop()