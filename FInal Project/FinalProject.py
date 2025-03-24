import os
import csv
import tkinter as tk
from tkinter import messagebox

# Define the absolute path for the records.csv file
FILE_NAME = r"C:\Users\Joss\Documents\HTML practice\Kapebara Alpha\IT0011_TUAZON\Final Project\records.csv"

# Ensure the file exists and has a header
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["First Name", "Middle Name", "Last Name", "Birthday (MM-DD-YYYY)", "Gender"])

# Function to sign up (add a new record)
def sign_up():
    def save_record():
        first_name = entry_first.get().strip()
        middle_name = entry_middle.get().strip()
        last_name = entry_last.get().strip()
        birthday = entry_birthday.get().strip()
        gender = gender_var.get()

        if not (first_name and last_name and birthday and gender):
            messagebox.showerror("Error", "All fields except middle name are required!")
            return

        # Validate birthday format (MM-DD-YYYY)
        try:
            month, day, year = map(int, birthday.split("-"))
            if not (1 <= month <= 12 and 1 <= day <= 31 and 1900 <= year <= 2100):
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Invalid Birthday format! Use MM-DD-YYYY.")
            return

        try:
            with open(FILE_NAME, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([first_name, middle_name, last_name, birthday, gender])
            messagebox.showinfo("Success", "Record saved successfully!")
            sign_up_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save record: {e}")

    sign_up_window = tk.Toplevel(root)
    sign_up_window.title("Sign Up")

    tk.Label(sign_up_window, text="First Name:").grid(row=0, column=0, padx=5, pady=5)
    entry_first = tk.Entry(sign_up_window)
    entry_first.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(sign_up_window, text="Middle Name:").grid(row=1, column=0, padx=5, pady=5)
    entry_middle = tk.Entry(sign_up_window)
    entry_middle.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(sign_up_window, text="Last Name:").grid(row=2, column=0, padx=5, pady=5)
    entry_last = tk.Entry(sign_up_window)
    entry_last.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(sign_up_window, text="Birthday (MM-DD-YYYY):").grid(row=3, column=0, padx=5, pady=5)
    entry_birthday = tk.Entry(sign_up_window)
    entry_birthday.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(sign_up_window, text="Gender:").grid(row=4, column=0, padx=5, pady=5)
    gender_var = tk.StringVar(value="Male")
    tk.OptionMenu(sign_up_window, gender_var, "Male", "Female", "Other").grid(row=4, column=1, padx=5, pady=5)

    tk.Button(sign_up_window, text="Save", command=save_record).grid(row=5, column=0, columnspan=2, pady=10)

# Function to view all records
def view_records():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)
            records = list(reader)

            if len(records) <= 1:
                messagebox.showinfo("Records", "No records found.")
                return

            display_text = "\n".join([", ".join(row) for row in records[1:]])
            messagebox.showinfo("All Records", display_text)

    except FileNotFoundError:
        messagebox.showerror("Error", "The records file was not found. Check the file path.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to search for a record
def search_record():
    def perform_search():
        query = search_entry.get().strip().lower()
        if not query:
            messagebox.showinfo("Search Results", "Please enter a name to search.")
            return
        
        try:
            with open(FILE_NAME, "r", newline="") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                results = [", ".join(row) for row in reader if any(query in field.lower() for field in row)]
            
            if results:
                messagebox.showinfo("Search Results", "\n".join(results))
            else:
                messagebox.showinfo("Search Results", "No matching record found.")

        except FileNotFoundError:
            messagebox.showerror("Error", "The records file was not found. Check the file path.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    search_window = tk.Toplevel(root)
    search_window.title("Search Record")

    tk.Label(search_window, text="Enter name to search:").pack(pady=5)
    search_entry = tk.Entry(search_window)
    search_entry.pack(pady=5)

    tk.Button(search_window, text="Search", command=perform_search).pack(pady=5)

# Create the main GUI
root = tk.Tk()
root.title("Student Record Management")

tk.Label(root, text="Menu", font=("Arial", 14, "bold")).pack(pady=10)
tk.Button(root, text="Sign Up", command=sign_up, width=20).pack(pady=5)
tk.Button(root, text="View All Records", command=view_records, width=20).pack(pady=5)
tk.Button(root, text="Search Record", command=search_record, width=20).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit, width=20).pack(pady=10)

root.mainloop()
