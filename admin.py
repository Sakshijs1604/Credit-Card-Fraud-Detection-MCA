import tkinter as tk
from tkinter import messagebox

from database import get_history


class Admin:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Admin Dashboard"
        )

        self.root.geometry("1000x600")
        self.root.configure(bg="white")
        self.root.resizable(False, False)

        # =========================
        # TITLE
        # =========================

        tk.Label(
            root,
            text="ADMIN DASHBOARD",
            font=("Arial", 28, "bold"),
            bg="white",
            fg="black"
        ).pack(pady=40)

        # =========================
        # GET HISTORY
        # =========================

        records = get_history()

        total = len(records)

        fraud = 0
        legitimate = 0

        for record in records:

            if "FRAUDULENT" in str(record[3]).upper():
                fraud += 1
            else:
                legitimate += 1

        # =========================
        # CARDS CONTAINER
        # =========================

        cards_frame = tk.Frame(
            root,
            bg="white",
            width=850,
            height=220
        )

        cards_frame.pack(
            pady=55
        )

        # Prevent container from shrinking
        cards_frame.pack_propagate(False)

        # Equal columns
        cards_frame.grid_columnconfigure(
            0,
            weight=1
        )

        cards_frame.grid_columnconfigure(
            1,
            weight=1
        )

        cards_frame.grid_columnconfigure(
            2,
            weight=1
        )

        # =========================
        # TOTAL CARD
        # =========================

        self.create_card(
            cards_frame,
            "TOTAL PREDICTIONS",
            total,
            "#2563eb",
            0
        )

        # =========================
        # FRAUD CARD
        # =========================

        self.create_card(
            cards_frame,
            "FRAUD TRANSACTIONS",
            fraud,
            "#dc2626",
            1
        )

        # =========================
        # LEGITIMATE CARD
        # =========================

        self.create_card(
            cards_frame,
            "LEGITIMATE TRANSACTIONS",
            legitimate,
            "#16a34a",
            2
        )

        # =========================
        # BACK TO HOME BUTTON
        # =========================

        tk.Button(
            root,
            text="BACK TO HOME",
            font=("Arial", 12, "bold"),
            width=20,
            height=2,
            bg="#172554",
            fg="white",
            activebackground="#333333",
            activeforeground="white",
            cursor="hand2",
            command=self.back_home
        ).place(
            relx=0.5,
            y=500,
            anchor="center"
        )

    # =====================================
    # CREATE CARD
    # =====================================

    def create_card(
        self,
        parent,
        title,
        value,
        color,
        column
    ):

        # SAME WIDTH AND HEIGHT
        CARD_WIDTH = 250
        CARD_HEIGHT = 170

        frame = tk.Frame(
            parent,
            bg=color,
            width=CARD_WIDTH,
            height=CARD_HEIGHT
        )

        frame.grid(
            row=0,
            column=column,
            padx=15,
            pady=10
        )

        # Keep exact same size
        frame.grid_propagate(False)

        # =========================
        # CARD TITLE
        # =========================

        tk.Label(
            frame,
            text=title,
            font=("Arial", 12, "bold"),
            bg=color,
            fg="white",
            wraplength=220,
            justify="center"
        ).pack(
            pady=(30, 12)
        )

        # =========================
        # CARD VALUE
        # =========================

        tk.Label(
            frame,
            text=str(value),
            font=("Arial", 30, "bold"),
            bg=color,
            fg="white"
        ).pack()

    # =====================================
    # BACK TO HOME
    # =====================================

    def back_home(self):

        from home import Home

        for widget in self.root.winfo_children():
            widget.destroy()

        Home(self.root)
