from tkinter import *
import requests

def check_symptom():
    symptom = entry.get()

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3",
        "prompt": f"You are a helpful medical assistant. My symptom is: {symptom}. Give simple advice and suggest consulting a doctor.",
        "stream": False
    }

    try:
        response = requests.post(url, json=data)
        result_text = response.json()["response"]
        result.config(text=result_text)
    except:
        result.config(text="Ollama is not running. Please start Ollama.")

# Window
root = Tk()
root.title("AI Doctor App")
root.geometry("500x350")

title = Label(root, text="AI Doctor", font=("Arial",20))
title.pack(pady=10)

entry = Entry(root, width=40)
entry.pack(pady=10)

button = Button(root, text="Ask AI Doctor", command=check_symptom)
button.pack(pady=10)

result = Label(root, text="", wraplength=400, justify="left")
result.pack(pady=20)

root.mainloop()
