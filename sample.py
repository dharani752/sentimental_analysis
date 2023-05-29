import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
from input import inputt

window = tk.Tk()
window.title("Sentiment Analysis")
window.geometry("1350x850")
window.configure(background="lavender")
heading_label = tk.Label(window, text="Sentiment Analysis", font=("Arial", 24, "bold"), bg="lavender", fg="blue")
heading_label.pack(pady=10)
image = Image.open("sent_img.jpeg")
image = image.resize((400, 200))
photo = ImageTk.PhotoImage(image)

label = tk.Label(window, image=photo)
label.pack(pady=10)

text_widget = scrolledtext.ScrolledText(window, height=10, width=50)
text_widget.pack(pady=5)

scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_widget.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_widget.yview)

frame = tk.Frame(window)

def button1_fun():
    text = text_widget.get("1.0", tk.END).strip()  # Get the text from the ScrolledText widget and remove leading/trailing whitespace
    k = inputt(text)
    text_widget1.delete("1.0", tk.END)  # Clear the previous content of text_widget1
    text_widget1.insert(tk.END, k)  # Insert the value of k into text_widget1

bt1 = tk.Button(window, bg="pink", text="Prediction", command=button1_fun)
bt1.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

text_widget1 = scrolledtext.ScrolledText(window, height=5, width=50)
text_widget1.pack(pady=10)

scrollbar2 = tk.Scrollbar(window)
scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)
text_widget1.config(yscrollcommand=scrollbar2.set)
scrollbar2.config(command=text_widget1.yview)

small_paragraph = "0.Negitive\n 1.Postive \n 2.Netural"

label1 = tk.Label(window, text=small_paragraph, font=("Arial", 12), bg="lavender")
label1.pack(pady=10)


window.mainloop()

