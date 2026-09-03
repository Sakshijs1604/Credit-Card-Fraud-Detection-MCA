import tkinter as tk
from tkinter import ttk, messagebox

from database import get_history, delete_history


class History:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Prediction History"
        )

        self.root.geometry("1000x600")
        self.root.configure(bg="#eff6ff")
        self.root.resizable(False, False)

        # ==============================
        # TITLE
        # ==============================

        tk.Label(
            root,
            text="PREDICTION HISTORY",
            font=("Arial", 24, "bold"),
            bg="#eff6ff",
            fg="#172554"
        ).pack(pady=20)

        # ==============================
        # TABLE STYLE
        # ==============================

        style = ttk.Style()

        # Use clam theme for better borders
        style.theme_use("clam")

        # Table body
        style.configure(
            "Treeview",
            background="white",
            foreground="black",
            rowheight=35,
            fieldbackground="white",
            font=("Arial", 10),
            borderwidth=1,
            relief="solid"
        )

        # Table heading
        style.configure(
            "Treeview.Heading",
            background="#172554",
            foreground="white",
            font=("Arial", 11, "bold"),
            borderwidth=1,
            relief="solid"
        )

        # Selected row
        style.map(
            "Treeview",
            background=[
                ("selected", "#bfdbfe")
            ],
            foreground=[
                ("selected", "black")
            ]
        )

        # ==============================
        # TABLE COLUMNS
        # ==============================

        columns = (
            "ID",
            "Transaction Time",
            "Amount",
            "Prediction",
            "Probability"
        )

        self.table = ttk.Treeview(
            root,
            columns=columns,
            show="headings",
            height=10
        )

        # ==============================
        # COLUMN HEADINGS
        # ==============================

        self.table.heading(
            "ID",
            text="ID"
        )

        self.table.heading(
            "Transaction Time",
            text="Transaction Time"
        )

        self.table.heading(
            "Amount",
            text="Amount"
        )

        self.table.heading(
            "Prediction",
            text="Prediction"
        )

        self.table.heading(
            "Probability",
            text="Probability"
        )

        # ==============================
        # COLUMN WIDTH
        # ==============================

        self.table.column(
            "ID",
            width=70,
            anchor="center"
        )

        self.table.column(
            "Transaction Time",
            width=230,
            anchor="center"
        )

        self.table.column(
            "Amount",
            width=150,
            anchor="center"
        )

        self.table.column(
            "Prediction",
            width=200,
            anchor="center"
        )

        self.table.column(
            "Probability",
            width=200,
            anchor="center"
        )

        # ==============================
        # TABLE PACK
        # ==============================

        self.table.pack(
            padx=20,
            pady=10
        )

        # ==============================
        # DELETE BUTTON
        # ==============================

        tk.Button(
            root,
            text="DELETE SELECTED",
            font=("Arial", 11, "bold"),
            bg="#dc2626",
            fg="white",
            activebackground="#b91c1c",
            activeforeground="white",
            width=20,
            cursor="hand2",
            command=self.delete
        ).pack(pady=10)

        # ==============================
        # BACK BUTTON
        # ==============================

        tk.Button(
            root,
            text="BACK TO HOME",
            font=("Arial", 11, "bold"),
            bg="#172554",
            fg="white",
            activebackground="#1e3a8a",
            activeforeground="white",
            width=20,
            cursor="hand2",
            command=self.back_home
        ).pack()

        # ==============================
        # LOAD HISTORY
        # ==============================

        self.load_data()

    # ==================================
    # LOAD DATA
    # ==================================

    def load_data(self):

        # Delete old rows
        for item in self.table.get_children():
            self.table.delete(item)

        try:

            records = get_history()

            if records:

                for record in records:

                    self.table.insert(
                        "",
                        tk.END,
                        values=record
                    )

            else:

                messagebox.showinfo(
                    "History",
                    "No prediction history found."
                )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                f"Unable to load history.\n\n{e}"
            )

    # ==================================
    # DELETE SELECTED RECORD
    # ==================================

    def delete(self):

        selected = self.table.selection()

        if not selected:

            messagebox.showwarning(
                "Warning",
                "Please select a record."
            )

            return

        # Get selected row
        item = self.table.item(
            selected[0]
        )

        # First column = ID
        history_id = item["values"][0]

        # Confirmation
        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this record?"
        )

        if not confirm:
            return

        try:

            delete_history(history_id)

            messagebox.showinfo(
                "Success",
                "Record deleted successfully."
            )

            # Refresh table
            self.load_data()

        except Exception as e:

            messagebox.showerror(
                "Delete Error",
                f"Unable to delete record.\n\n{e}"
            )

    # ==================================
    # BACK TO HOME
    # ==================================

    def back_home(self):

        from home import Home

        # Remove all widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Open Home page
        Home(self.root)
