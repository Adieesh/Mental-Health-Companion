from textblob import TextBlob
from datetime import date
import tkinter as tk
import os

today = date.today()

def analyze_mood():
    user_feeling = input_box.get("1.0", tk.END).strip()
    polarity = TextBlob(user_feeling).sentiment.polarity

    if polarity > 0.3:
        message = "😊 I'm really glad to hear that! Keep shining and spreading those good vibes."
    elif polarity < -0.3:
        message = "💙 I'm here for you. It's okay to feel this way — take things one step at a time."
    else:
        message = "😌 Thanks for sharing. Would you like to talk a bit more about how you're feeling?"

    response_label.config(text=message)

    with open("mood_diary.csv", "a") as file:
        file.write(f"{today},\"{user_feeling}\",{polarity}\n")

def open_diary():
    try:
        os.startfile("mood_diary.csv")  # Works on Windows
    except AttributeError:
        # For MacOS / Linux
        import subprocess
        subprocess.call(["open", "mood_diary.csv"])


# Window Setup
window = tk.Tk()
window.title("Mental Health Companion 🧠")
window.geometry("450x352")
window.config(bg="#1e1e1e")  # Dark background

# Title
title = tk.Label(window, text="🧠 Mental Health Companion", font=("Helvetica", 18, "bold"), bg="#1e1e1e", fg="#f0f0f0")
title.grid(row=0, column=0, columnspan=2, pady=20)

# Prompt
prompt = tk.Label(window, text="How are you feeling today?", font=("Helvetica", 12), bg="#1e1e1e", fg="#cccccc")
prompt.grid(row=1, column=0, padx=20, sticky="w")

# Input box (dark with light text)
input_box = tk.Text(window, width=50, height=2, font=("Helvetica", 11), bg="#2b2b2b", fg="#ffffff", insertbackground="white")
input_box.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

# Submit button (blue highlight)
submit_btn = tk.Button(window, text="Submit", font=("Helvetica", 11), command=analyze_mood,
                       bg="#007acc", fg="white", activebackground="#005f9e")
submit_btn.grid(row=3, column=0, columnspan=2, pady=15)

# Response label
response_label = tk.Label(window, text="", font=("Helvetica", 12), wraplength=460, bg="#1e1e1e", fg="#dcdcdc")
response_label.grid(row=5, column=0, columnspan=2, pady=10)

view_btn = tk.Button(window, text="📖 View Mood Diary", font=("Helvetica", 10),
                     command=open_diary, bg="#444", fg="white", activebackground="#666")
view_btn.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()
