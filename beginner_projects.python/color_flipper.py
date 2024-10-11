import tkinter as tk
import random


# Function to generate a random color
def generate_random_color():
    random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return random_color


# Function to change the background color
def change_color():
    new_color = generate_random_color()
    root.config(bg=new_color)
    color_label.config(text=f"Current Color: {new_color}", bg=new_color)


# Create the main window
root = tk.Tk()
root.title("Color Flipper")
root.geometry("400x300")

# Create a label to display the current color code
color_label = tk.Label(root, text="Current Color: #FFFFFF", font=("Helvetica", 16))
color_label.pack(pady=20)

# Create a button to change the color
color_button = tk.Button(root, text="Change Color", command=change_color, font=("Helvetica", 16), bg="#007BFF",
                         fg="white")
color_button.pack(pady=20)

# Start the main loop
root.mainloop()
