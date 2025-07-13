import re
import json
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog

class TokenizerApp:
    def __init__(self, window):
        self.vocab = {}

        self.file_btn = ttk.Button(window, text="Select Text file", command=self.open_file)
        self.file_btn.pack(pady=5)

        self.tokenize_btn = ttk.Button(window, text="Tokenize", command=self.tokenize)
        self.tokenize_btn.pack(pady=20)

        self.info_label = ttk.Label(window, text="No file selected.")
        self.info_label.pack()


    def open_file(self):
        file_path = filedialog.askopenfilename(
            title="Select a Text File", filetypes=[("Text Files", "*.txt")]
        )
        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                raw_text = f.read()

            preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
            preprocessed = [item for item in preprocessed if item.strip()]
            all_tokens = sorted(list(set(preprocessed)))
            all_tokens.extend(["<|endoftext|>", "<|unk|>"])
            self.vocab = {token: integer for integer, token in enumerate(all_tokens)}

    def tokenize(self):
        print(self.vocab)
        with open('vocabulary.json', 'w') as f:
            json.dump(self.vocab, f, indent=4)
        self.info_label.config(
            text=f"{len(self.vocab)} unique tokens created."
        )


# tkinter window
window = ttk.Window()
window.title("SimpleTokenizer")
window.geometry("800x500")

app = TokenizerApp(window)

window.mainloop()




