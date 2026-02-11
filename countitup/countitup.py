import tkinter as tk
from tkinter import ttk, messagebox

def calculate():
    try:
        age = int(age_entry.get())
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        gender = gender_var.get()
        activity = activity_var.get()

        # BMR calculation
        if gender == "Male":
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161

        activity_levels = {
            "Sedentary": 1.2,
            "Lightly Active": 1.375,
            "Moderately Active": 1.55,
            "Very Active": 1.725
        }

        calories = bmr * activity_levels[activity]

        # BMI calculation
        bmi = weight / ((height / 100) ** 2)
        if bmi < 18.5:
            bmi_status = "Underweight"
        elif bmi < 25:
            bmi_status = "Normal"
        elif bmi < 30:
            bmi_status = "Overweight"
        else:
            bmi_status = "Obese"

        result_label.config(
            text=f"BMR: {bmr:.2f} kcal\n"
                 f"Daily Calories: {calories:.2f} kcal\n"
                 f"BMI: {bmi:.2f} ({bmi_status})"
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

# Main window
root = tk.Tk()
root.title("CountItUp – Calories Calculator")
root.geometry("350x420")
root.resizable(False, False)

# Title
tk.Label(root, text="CountItUp", font=("Arial", 18, "bold")).pack(pady=10)

# Input frame
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Age").grid(row=0, column=0, sticky="w")
age_entry = tk.Entry(frame)
age_entry.grid(row=0, column=1)

tk.Label(frame, text="Weight (kg)").grid(row=1, column=0, sticky="w")
weight_entry = tk.Entry(frame)
weight_entry.grid(row=1, column=1)

tk.Label(frame, text="Height (cm)").grid(row=2, column=0, sticky="w")
height_entry = tk.Entry(frame)
height_entry.grid(row=2, column=1)

tk.Label(frame, text="Gender").grid(row=3, column=0, sticky="w")
gender_var = tk.StringVar(value="Male")
ttk.Combobox(frame, textvariable=gender_var, values=["Male", "Female"], state="readonly").grid(row=3, column=1)

tk.Label(frame, text="Activity Level").grid(row=4, column=0, sticky="w")
activity_var = tk.StringVar(value="Sedentary")
ttk.Combobox(
    frame,
    textvariable=activity_var,
    values=["Sedentary", "Lightly Active", "Moderately Active", "Very Active"],
    state="readonly"
).grid(row=4, column=1)

# Calculate button
tk.Button(root, text="Calculate", command=calculate, bg="#4CAF50", fg="white").pack(pady=15)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.pack(pady=10)

root.mainloop()
