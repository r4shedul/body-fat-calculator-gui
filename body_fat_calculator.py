import tkinter as tk
import math

def body_fat_male(height, neck, waist):
    try:
        return 495 / (1.0324 - 0.19077 * math.log10(waist - neck) +
                      0.15456 * math.log10(height)) - 450
    except ValueError:
        return None

def body_fat_female(height, neck, waist, hip):
    try:
        return 495 / (1.29579 - 0.35004 * math.log10(waist + hip - neck) +
                      0.22100 * math.log10(height)) - 450
    except ValueError:
        return None

def calculate():
    gender = gender_var.get()
    try:
        height = float(entry_height.get())
        neck = float(entry_neck.get())
        waist = float(entry_waist.get())
        age = int(entry_age.get())

        if gender == "Male":
            result = body_fat_male(height, neck, waist)
        else:
            hip = float(entry_hip.get())
            result = body_fat_female(height, neck, waist, hip)

        if result is not None:
            result_label.config(text=f"Estimated Body Fat: {round(result, 2)} %")
        else:
            result_label.config(text="Invalid input. Check measurements.")
    except ValueError:
        result_label.config(text="Please enter all values correctly.")

def update_form(*args):
    if gender_var.get() == "Male":
        entry_hip_label.grid_remove()
        entry_hip.grid_remove()
    else:
        entry_hip_label.grid(row=5, column=0, sticky="w", pady=5)
        entry_hip.grid(row=5, column=1, pady=5, sticky="ew")

root = tk.Tk()
root.title("Body Fat Calculator")
root.geometry("400x480")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20, bg='#f0f0f0')
frame.pack(expand=True)

header = tk.Label(frame, text="Body Fat Calculator", font=("Arial", 16, "bold"), bg='#b32d2e', fg='white', pady=10)
header.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="ew")

tk.Label(frame, text="Select your gender:", anchor="w", bg='#f0f0f0').grid(row=1, column=0, sticky="w", pady=5)
gender_var = tk.StringVar(value="Male")
gender_var.trace("w", update_form)
tk.OptionMenu(frame, gender_var, "Male", "Female").grid(row=1, column=1, pady=5, sticky="ew")

tk.Label(frame, text="Enter your age:", anchor="w", bg='#f0f0f0').grid(row=2, column=0, sticky="w", pady=5)
entry_age = tk.Entry(frame)
entry_age.grid(row=2, column=1, pady=5, sticky="ew")

tk.Label(frame, text="Enter your height (in cm):", anchor="w", bg='#f0f0f0').grid(row=3, column=0, sticky="w", pady=5)
entry_height = tk.Entry(frame)
entry_height.grid(row=3, column=1, pady=5, sticky="ew")

tk.Label(frame, text="Enter your waist circumference (in cm):", anchor="w", bg='#f0f0f0').grid(row=4, column=0, sticky="w", pady=5)
entry_waist = tk.Entry(frame)
entry_waist.grid(row=4, column=1, pady=5, sticky="ew")

entry_hip_label = tk.Label(frame, text="Enter your hip circumference (in cm):", anchor="w", bg='#f0f0f0')
entry_hip = tk.Entry(frame)

tk.Label(frame, text="Enter your neck circumference (in cm):", anchor="w", bg='#f0f0f0').grid(row=6, column=0, sticky="w", pady=5)
entry_neck = tk.Entry(frame)
entry_neck.grid(row=6, column=1, pady=5, sticky="ew")

tk.Button(frame, text="Calculate", bg='#b32d2e', fg='white', command=calculate).grid(row=7, column=0, columnspan=2, pady=20)

result_label = tk.Label(frame, text="", fg="blue", font=("Arial", 12), bg='#f0f0f0')
result_label.grid(row=8, column=0, columnspan=2, pady=10)

update_form()
root.mainloop()
