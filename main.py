import tkinter as tk
from tkinter import messagebox

def calculate_price():
    try:

        price = float(entry_price.get())
        discount = float(entry_discount.get())
        quantity = int(entry_quantity.get()) 

        
        if price < 0 or discount < 0 or quantity < 0:
            messagebox.showwarning("Input Error", "Numbers cannot be negative!")
            return

 
        total_base = price * quantity
        discount_amount = total_base * (discount / 100)
        final_price = total_base - discount_amount


        label_result.config(text=f"Final Price: Rp. {final_price:,.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")




root = tk.Tk()
root.title("Discount Calculator")
root.geometry("400x350")


label_price = tk.Label(root, text="Original Price (Rp):", font=("Arial", 10))
label_price.pack(pady=5)
entry_price = tk.Entry(root, font=("Arial", 12))
entry_price.pack(pady=5)


label_quantity = tk.Label(root, text="Quantity:", font=("Arial", 10))
label_quantity.pack(pady=5)
entry_quantity = tk.Entry(root, font=("Arial", 12))
entry_quantity.insert(0, "1") 
entry_quantity.pack(pady=5)


label_discount = tk.Label(root, text="Discount (%):", font=("Arial", 10))
label_discount.pack(pady=5)
entry_discount = tk.Entry(root, font=("Arial", 12))
entry_discount.pack(pady=5)


btn_calc = tk.Button(root, text="Calculate", font=("Arial", 10, "bold"), command=calculate_price)
btn_calc.pack(pady=20)


label_result = tk.Label(root, text="Final Price: Rp. 0.00", font=("Arial", 12, "bold"))
label_result.pack(pady=10)


root.mainloop()