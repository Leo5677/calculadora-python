import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Python")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # Variável para armazenar a expressão
        self.current = ""
        
        # Display
        self.display = tk.Entry(root, font=('Arial', 20), justify='right', bd=10)
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        
        # Botões
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '√', '^', 'CE'
        ]
        
        # Criar e posicionar os botões
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            btn = ttk.Button(root, text=button, command=cmd)
            btn.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Configurar o grid
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
            
    def click(self, key):
        if key == '=':
            try:
                # Substituir ^ por ** para potência
                result = eval(self.current.replace('^', '**'))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.current = str(result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Erro")
                self.current = ""
        
        elif key == 'C':
            self.current = ""
            self.display.delete(0, tk.END)
            
        elif key == 'CE':
            self.current = self.current[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.current)
            
        elif key == '√':
            try:
                result = math.sqrt(float(self.current))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.current = str(result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Erro")
                self.current = ""
                
        else:
            self.current += key
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.current)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop() 
