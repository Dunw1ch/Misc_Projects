import tkinter as tk
import base64

def decrypt():
    input_str = input_entry.get()
    try:
        decoded_str = base64.b64decode(input_str).decode('utf-8')
        result_label.config(text=decoded_str)
    except:
        result_label.config(text="Invalid input")

root = tk.Tk()
root.title("Base64 Decrypter")

input_label = tk.Label(root, text="Enter base64 string:")
input_entry = tk.Entry(root)
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
result_label = tk.Label(root, text="")

input_label.pack()
input_entry.pack()
decrypt_button.pack()
result_label.pack()

root.mainloop()
