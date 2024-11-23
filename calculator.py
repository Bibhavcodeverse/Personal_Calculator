import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        
        self.expression = ""
        self.input_text = tk.StringVar()
        self.entry = tk.Entry(self.root, textvariable=self.input_text, font=('arial', 20, 'bold'), bd=30, insertwidth=4, width=14, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)
        
       
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '=', '+'
        ]
        
        
        row = 1
        col = 0
        for button in buttons:
            self.create_button(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        
        self.create_button('C', row, col)
    
    def create_button(self, value, row, col):
        button = tk.Button(self.root, text=value, padx=20, pady=20, font=('arial', 18, 'bold'), command=lambda: self.on_button_click(value))
        button.grid(row=row, column=col)
    
    def on_button_click(self, value):
        if value == "=":
            try:
                result = str(eval(self.expression))  
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""
        elif value == "C":
            self.expression = ""
            self.input_text.set("")
        else:
            self.expression += value
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
