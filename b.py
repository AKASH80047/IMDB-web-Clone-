import tkinter as tk
import webbrowser

# Credentials for login
USERNAME = "admin"
PASSWORD = "1234"
HTML_FILE = "index.html"  # Replace with your HTML file name

# Function to handle login
def login():
    user = username_entry.get()
    pwd = password_entry.get()

    if user == USERNAME and pwd == PASSWORD:
        webbrowser.open(HTML_FILE)  # Opens the HTML file in the default browser
    else:
        messagebox.showerror("Error", "Invalid username or password!")

# Function to reset the fields
def reset_fields():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Root window setup
root = tk.Tk()
root.title("Login Page")
root.geometry("600x400")  # Updated size
root.config(bg="#2c3e50")

# Add header
header = tk.Label(
    root, 
    text="Login Page", 
    font=("Arial", 24, "bold"),  # Larger font
    bg="#2c3e50", 
    fg="#ecf0f1"
)
header.pack(pady=30)

# Username field
username_label = tk.Label(root, text="Username:", font=("Arial", 14), bg="#2c3e50", fg="#ecf0f1")
username_label.pack(pady=10)
username_entry = tk.Entry(root, font=("Arial", 14), width=30)
username_entry.pack(pady=5)

# Password field
password_label = tk.Label(root, text="Password:", font=("Arial", 14), bg="#2c3e50", fg="#ecf0f1")
password_label.pack(pady=10)
password_entry = tk.Entry(root, font=("Arial", 14), show="*", width=30)
password_entry.pack(pady=5)

# Buttons
login_button = tk.Button(
    root, 
    text="Login", 
    font=("Arial", 14, "bold"), 
    bg="#27ae60", 
    fg="white", 
    width=15, 
    command=login
)
login_button.pack(pady=20)

reset_button = tk.Button(
    root, 
    text="Reset", 
    font=("Arial", 14, "bold"), 
    bg="#e74c3c", 
    fg="white", 
    width=15, 
    command=reset_fields
)
reset_button.pack(pady=10)

# Footer
footer = tk.Label(
    root, 
    text="Welcome to the system!", 
    font=("Arial", 12, "italic"), 
    bg="#2c3e50", 
    fg="#95a5a6"
)
footer.pack(side="bottom", pady=20)

# Run the application
root.mainloop()
