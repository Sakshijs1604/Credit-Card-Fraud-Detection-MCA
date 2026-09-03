import tkinter as tk
from tkinter import messagebox

from prediction import Prediction
from history import History
from admin import Admin


class Dashboard:

    def __init__(self, root, username):

        self.root = root
        self.username = username

        self.root.title(
            "Credit Card Fraud Detection System - Dashboard"
        )

        self.root.geometry("1200x700")

        self.root.configure(
            bg="#0F172A"
        )

        self.root.resizable(False, False)

        self.create_dashboard()


    def create_dashboard(self):

        header = tk.Frame(
            self.root,
            bg="#172554",
            height=100
        )

        header.pack(
            fill="x"
        )


        tk.Label(
            header,
            text="Credit Card Fraud Detection System",
            font=("Arial", 25, "bold"),
            bg="#172554",
            fg="white"
        ).pack(
            pady=30
        )


        tk.Label(
            self.root,
            text="Welcome, " + self.username,
            font=("Arial", 18, "bold"),
            bg="#0F172A",
            fg="white"
        ).pack(pady=40)


        button_frame = tk.Frame(
            self.root,
            bg="#0F172A"
        )

        button_frame.pack()


        tk.Button(
            button_frame,
            text="Fraud Prediction",
            font=("Arial", 15, "bold"),
            width=22,
            height=3,
            bg="#2563EB",
            fg="white",
            command=self.open_prediction
        ).grid(
            row=0,
            column=0,
            padx=20,
            pady=20
        )


        tk.Button(
            button_frame,
            text="Prediction History",
            font=("Arial", 15, "bold"),
            width=22,
            height=3,
            bg="#059669",
            fg="white",
            command=self.open_history
        ).grid(
            row=0,
            column=1,
            padx=20,
            pady=20
        )


        tk.Button(
            button_frame,
            text="Admin Panel",
            font=("Arial", 15, "bold"),
            width=22,
            height=3,
            bg="#7C3AED",
            fg="white",
            command=self.open_admin
        ).grid(
            row=1,
            column=0,
            padx=20,
            pady=20
        )


        tk.Button(
            button_frame,
            text="Logout",
            font=("Arial", 15, "bold"),
            width=22,
            height=3,
            bg="#DC2626",
            fg="white",
            command=self.logout
        ).grid(
            row=1,
            column=1,
            padx=20,
            pady=20
        )


    def open_prediction(self):

        win = tk.Toplevel(
            self.root
        )

        Prediction(
            win,
            self.username
        )


    def open_history(self):

        win = tk.Toplevel(
            self.root
        )

        History(
            win
        )


    def open_admin(self):

        win = tk.Toplevel(
            self.root
        )

        Admin(
            win
        )


    def logout(self):

        answer = messagebox.askyesno(
            "Logout",
            "Do you want to logout?"
        )

        if answer:

            self.root.destroy()

            root = tk.Tk()

            from login import Login

            Login(root)

            root.mainloop()
