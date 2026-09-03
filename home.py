import tkinter as tk

from prediction import Prediction
from history import History
from admin import Admin


class Home:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Credit Card Fraud Detection System - Home"
        )

        self.root.geometry("1000x600")
        self.root.configure(bg="#172554")
        self.root.resizable(True, True)

        # Header
        header = tk.Frame(
            root,
            bg="#1e3a8a",
            height=90
        )

        header.pack(fill="x")

        tk.Label(
            header,
            text="CREDIT CARD FRAUD DETECTION SYSTEM",
            font=("Arial", 24, "bold"),
            bg="#1e3a8a",
            fg="white"
        ).pack(pady=25)

        # Welcome
        tk.Label(
            root,
            text="Welcome to Fraud Detection System",
            font=("Arial", 22, "bold"),
            bg="#172554",
            fg="white"
        ).pack(pady=50)

        # Buttons
        tk.Button(
            root,
            text="FRAUD PREDICTION",
            font=("Arial", 14, "bold"),
            width=25,
            height=2,
            bg="#2563eb",
            fg="white",
            command=self.open_prediction
        ).pack(pady=10)

        tk.Button(
            root,
            text="PREDICTION HISTORY",
            font=("Arial", 14, "bold"),
            width=25,
            height=2,
            bg="#0891b2",
            fg="white",
            command=self.open_history
        ).pack(pady=10)

        tk.Button(
            root,
            text="ADMIN",
            font=("Arial", 14, "bold"),
            width=25,
            height=2,
            bg="#7c3aed",
            fg="white",
            command=self.open_admin
        ).pack(pady=10)

        tk.Button(
            root,
            text="EXIT",
            font=("Arial", 14, "bold"),
            width=25,
            height=2,
            bg="#dc2626",
            fg="white",
            command=root.destroy
        ).pack(pady=10)

    def open_prediction(self):

        for widget in self.root.winfo_children():
            widget.destroy()

        Prediction(self.root)

    def open_history(self):

        for widget in self.root.winfo_children():
            widget.destroy()

        History(self.root)

    def open_admin(self):

        for widget in self.root.winfo_children():
            widget.destroy()

        Admin(self.root)
