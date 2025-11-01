# This application estimates the environmental footprint of everyday habits.
# It encourages users to make informed lifestyle choices using simple calculations.
# The goal is educational, not diagnostic: all figures are simplified averages. Not all Farms, cars, showers are the same. 

import tkinter as tk
from tkinter import ttk, messagebox

# Environmental data (per litre of milk)
# Sources:
# Our World in Data (via Statista) for cow & almond milk
# Swissmilk LCA comparative analysis for oat & soy milk
milk_data = {
    "almond": {"water": 371, "co2": 0.14},   # litres & kg CO2 per L
    "oat": {"water": 270, "co2": 0.21},
    "soy": {"water": 140, "co2": 0.22},
    "cow": {"water": 628, "co2": 3.20}
}

# Functions to calculate impacts 
# The brain of this operation.
# Calculates damage
def calculate_impact():
    try:
        coffees = int(entry_coffee.get())
        km_driven = float(entry_km.get())
        meat_meals = int(entry_meat.get())
        fast_fashion = int(entry_fashion.get())
        shower_minutes = int(entry_shower.get())
        milk_choice = milk_var.get().lower()

        # Simplified daily activity impacts
        coffee_base_water = coffees * 130
        car_emissions = km_driven * 0.21
        meat_emissions = meat_meals * 2.5
        fast_fashion_water = fast_fashion * 2700 / 30
        shower_water = shower_minutes * 9

        # Milk impact
        milk_per_coffee = 0.2
        if milk_choice in milk_data:
            milk_water = milk_data[milk_choice]["water"] * milk_per_coffee * coffees
            milk_emissions = milk_data[milk_choice]["co2"] * milk_per_coffee * coffees
        else:
            milk_water = milk_emissions = 0
 # Total daily impact combining all categories
        total_coffee_water = coffee_base_water + milk_water
        total_water = total_coffee_water + fast_fashion_water + shower_water
        total_emissions = car_emissions + meat_emissions + milk_emissions
 # Display formatted results inside the output text box
 # Data Sources :
# - Driving emissions: National Transport Commission (light-vehicle emissions intensity Australia)
# - Meat meal emissions: Meat & Livestock Australia (greenhouse gas footprint report)
# -  Fast fashion water impact: Florida State University Sustainable Campus (water use per clothing item)
#-  Shower water consumption: Localsearch Australia guidance (average shower water flow)
# - Milk production impacts: Various lifecycle analysis sources for dairy, oat, soy, and almond milk
# All my values are simplified estimates for educational comparison, not precise life cycle calculations.
        result_text = f"""
🌱 Estimated Daily Environmental Impact 🌱

☕ Coffee ({coffees} cups with {milk_choice} milk)
   → {total_coffee_water:.0f} L water
   → {milk_emissions:.2f} kg CO₂
  
    
🚗 Driving: {km_driven} km → {car_emissions:.2f} kg CO₂
🥩 Meat meals: {meat_meals} → {meat_emissions:.2f} kg CO₂
👕 Fast fashion: {fast_fashion}/month → {fast_fashion_water:.0f} L water/day
🚿 Showers: {shower_minutes} min → {shower_water:.0f} L water

💧 Total water use: {total_water:.0f} L/day
💨 Total CO₂ emissions: {total_emissions:.2f} kg/day

Small choices, big impact 🌏
"""
        result_box.config(state="normal")
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, result_text)
        result_box.config(state="disabled")

    except ValueError:
        # Input validation error: prevents program crashing on bad inputs
        messagebox.showerror("Input Error", "Please enter valid numeric values for all fields.")
# Navigation functions: controls switching between pages
def show_tips_page():
    calculator_frame.pack_forget()
    tips_frame.pack(fill="both", expand=True)

def show_calculator_page():
    tips_frame.pack_forget()
    calculator_frame.pack(fill="both", expand=True)

# GUI setup section: builds user interface using Tkinter 
root = tk.Tk()
root.title("🌍 Daily Habits Environmental Impact Calculator 🌿")
root.geometry("750x800")
root.configure(bg="#E9F5E1")

# Page 1: Calculator 
calculator_frame = tk.Frame(root, bg="#E9F5E1")
calculator_frame.pack(fill="both", expand=True)

title = tk.Label(
    calculator_frame,
    text="🌿 Daily Habits Environmental Impact Calculator 🌿",
    font=("Helvetica", 18, "bold"),
    bg="#A8D5BA",
    fg="#1E392A",
    pady=15
)
title.pack(fill="x")

input_frame = tk.Frame(calculator_frame, bg="#E9F5E1")
input_frame.pack(pady=20)

def create_label_entry(parent, text, row):
    label = tk.Label(parent, text=text, bg="#E9F5E1", fg="#2E4D2C", font=("Helvetica", 12, "bold"))
    entry = tk.Entry(parent, font=("Helvetica", 12), width=10)
    label.grid(row=row, column=0, sticky="w", pady=5, padx=10)
    entry.grid(row=row, column=1, pady=5)
    return entry

entry_coffee = create_label_entry(input_frame, "How many coffees per day?", 0)
entry_km = create_label_entry(input_frame, "Kilometres driven per day?", 1)
entry_meat = create_label_entry(input_frame, "Meat-based meals per day?", 2)
entry_fashion = create_label_entry(input_frame, "Fast fashion items per month?", 3)
entry_shower = create_label_entry(input_frame, "Minutes showering?", 4)

# Milk dropdown
tk.Label(input_frame, text="Type of milk used?", bg="#E9F5E1", fg="#2E4D2C", font=("Helvetica", 12, "bold")).grid(row=5, column=0, pady=10, sticky="w", padx=10)
milk_var = tk.StringVar(value="oat")
milk_menu = ttk.Combobox(input_frame, textvariable=milk_var, values=["almond", "oat", "soy", "cow"], font=("Helvetica", 12))
milk_menu.grid(row=5, column=1, pady=10)

# Calculate button
calculate_btn = tk.Button(
    calculator_frame,
    text="Calculate My Impact 🌎",
    font=("Helvetica", 14, "bold"),
    bg="#6DBE77",
    fg="white",
    activebackground="#57A76B",
    padx=20,
    pady=10,
    relief="flat",
    command=calculate_impact
)
calculate_btn.pack(pady=10)

# Result box
result_box = tk.Text(calculator_frame, height=15, width=75, font=("Helvetica", 12), wrap="word", bg="#F4FBF3", fg="#1E392A")
result_box.pack(padx=20, pady=10)
result_box.config(state="disabled")

# Tips button
tips_btn = tk.Button(
    calculator_frame,
    text="💪 Learn How to Make a Difference",
    font=("Helvetica", 13, "bold"),
    bg="#A8D5BA",
    fg="#1E392A",
    relief="flat",
    command=show_tips_page
)
tips_btn.pack(pady=10)

# Footer
footer = tk.Label(
    calculator_frame,
    text="🌎 Small changes make a big difference • Live consciously • Choose sustainably 🌎",
    font=("Helvetica", 10, "italic"),
    bg="#E9F5E1",
    fg="#3B5930",
    pady=10
)
footer.pack(fill="x")

# Page 2: Tips page
# Because data is great, but actions are greater
tips_frame = tk.Frame(root, bg="#E9F5E1")

tips_title = tk.Label(
    tips_frame,
    text="💪 Ways You Can Make a Difference 💚",
    font=("Helvetica", 18, "bold"),
    bg="#A8D5BA",
    fg="#1E392A",
    pady=15
)
tips_title.pack(fill="x")

tips_text = """Your daily choices matter - even small changes can reduce your environmental footprint and inspire others to do the same.

☕ Coffee
- Bring a reusable cup instead of disposable ones.
- Choose plant-based milk or support local cafés that prioritise sustainable sourcing.

🚗 Transport
- Walk, cycle, or use public transport for short trips.
- Carpool with friends or co-workers.
- Combine errands to reduce kilometres.

🍔 Food Choices
- Swap one or two meat meals each week for plant based options.
- Buy local, seasonal produce.
- Reduce food waste by planning meals and using leftovers.

👗 Fashion
- Buy second-hand or from ethical brands.
- Avoid fast fashion and host clothing swaps.

🚿 Water & Energy
- Keep showers under 5 minutes.
- Turn off taps when brushing teeth or washing dishes.
- Use cold laundry cycles and air dry clothes.
"""

tips_box = tk.Text(tips_frame, height=30, width=80, font=("Helvetica", 12), wrap="word", bg="#F4FBF3", fg="#1E392A")
tips_box.pack(padx=20, pady=20)
tips_box.insert(tk.END, tips_text)
tips_box.config(state="disabled")

back_btn = tk.Button(
    tips_frame,
    text="⬅️ Back to Calculator",
    font=("Helvetica", 13, "bold"),
    bg="#A8D5BA",
    fg="#1E392A",
    relief="flat",
    command=show_calculator_page
)
back_btn.pack(pady=10)

root.mainloop()
#Thank you for this semester! <3
