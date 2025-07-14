import tkinter as tk
from tkinter import messagebox

# Function to calculate bets and show results
def calculate_bets():
    try:
        investment = float(entry_investment.get())
        odd1 = float(entry_odd1.get())
        odd2 = float(entry_odd2.get())

        R = investment / (1/odd1 + 1/odd2)
        bet1 = R / odd1
        bet2 = R / odd2
        profit = R - investment
        percentage = float(profit / investment) * 100

        result_text = (
            f"Common Return (R): €{R:.2f}\n"
            f"Bet on Team 1: €{bet1:.2f}\n"
            f"Bet on Team 2: €{bet2:.2f}\n"
            f"Total Bet: €{bet1 + bet2:.2f}\n"
            f"Guaranteed Profit: €{profit:.2f}\n"
            f"Percentage  : % {percentage:.2f}"
        )

        label_result.config(text=result_text, fg="black")

        if R < investment:
            label_warning.config(text="⚠️ Not a good deal", fg="red")
        else:
            label_warning.config(text="")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for all fields.")

# Function to draw gradient background
def draw_gradient(canvas, color1, color2):
    width = 400
    height = 400
    r1, g1, b1 = root.winfo_rgb(color1)
    r2, g2, b2 = root.winfo_rgb(color2)
    r_ratio = (r2 - r1) / height
    g_ratio = (g2 - g1) / height
    b_ratio = (b2 - b1) / height

    for i in range(height):
        nr = int(r1 + (r_ratio * i)) >> 8
        ng = int(g1 + (g_ratio * i)) >> 8
        nb = int(b1 + (b_ratio * i)) >> 8
        color = f"#{nr:02x}{ng:02x}{nb:02x}"
        canvas.create_line(0, i, width, i, fill=color)

# Create main window
root = tk.Tk()
root.title("2-Way Betting Calculator")
root.geometry("400x400")

# Canvas for gradient background
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack(fill="both", expand=True)
draw_gradient(canvas, "white", "lightblue")

# Frame to place widgets on top of canvas
frame = tk.Frame(root, bg="white")
frame.place(relwidth=1, relheight=1)

# Input fields
tk.Label(frame, text="Enter Total Investment (EUR):", bg="white").pack(pady=5)
entry_investment = tk.Entry(frame, width=20)
entry_investment.pack()

tk.Label(frame, text="Enter Odds for Team 1:", bg="white").pack(pady=5)
entry_odd1 = tk.Entry(frame, width=20)
entry_odd1.insert(0, "")
entry_odd1.pack()

tk.Label(frame, text="Enter Odds for Team 2:", bg="white").pack(pady=5)
entry_odd2 = tk.Entry(frame, width=20)
entry_odd2.insert(0, "")
entry_odd2.pack()

# Button to calculate
btn_calculate = tk.Button(frame, text="Calculate Bets", command=calculate_bets)
btn_calculate.pack(pady=10)

# Output display
label_result = tk.Label(frame, text="", justify="left", bg="white")
label_result.pack(pady=5)
label_warning = tk.Label(frame, text="", justify="left", bg="white")
label_warning.pack(pady=5)

# Run the application
root.mainloop()
