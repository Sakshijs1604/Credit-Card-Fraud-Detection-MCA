import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

from database import check_login
from home import Home


class Login:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Credit Card Fraud Detection System - Login"
        )

        self.root.geometry("1000x600")
        self.root.resizable(True, True)

        # BACKGROUND IMAGE

        image_path = os.path.join(
            os.path.dirname(__file__),
            "login_bg.jpg"
        )

        try:

            self.bg_image = Image.open(image_path)

            self.bg_image = self.bg_image.resize(
                (1000, 600),
                Image.Resampling.LANCZOS
            )

            self.bg_photo = ImageTk.PhotoImage(
                self.bg_image
            )

            self.bg_label = tk.Label(
                self.root,
                image=self.bg_photo
            )

            self.bg_label.place(
                x=0,
                y=0,
                relwidth=1,
                relheight=1
            )

            # Keep background behind all widgets
            self.bg_label.lower()

        except Exception as e:

            # If image is not found,
            # use normal background color
            self.root.configure(
                bg="#172554"
            )

            print(
                "Background image error:",
                e
            )


        # TITLE

        title = tk.Label(
            self.root,
            text="CREDIT CARD FRAUD DETECTION SYSTEM",
            font=("Arial", 24, "bold"),
            bg="#172554",
            fg="white"
        )

        title.pack(
            pady=50
        )


        # LOGIN FRAME

        frame = tk.Frame(
            self.root,
            bg="white",
            width=400,
            height=330
        )

        frame.place(
            relx=0.5,
            rely=0.55,
            anchor="center"
        )

        frame.pack_propagate(False)


        # LOGIN TITLE

        tk.Label(
            frame,
            text="ADMIN LOGIN",
            font=("Arial", 22, "bold"),
            bg="white",
            fg="#172554"
        ).pack(
            pady=25
        )


        # USERNAME

        tk.Label(
            frame,
            text="Username",
            font=("Arial", 12),
            bg="white"
        ).pack()


        self.username = tk.Entry(
            frame,
            font=("Arial", 13),
            width=28
        )

        self.username.pack(
            pady=8
        )

        # PASSWORD

        tk.Label(
            frame,
            text="Password",
            font=("Arial", 12),
            bg="white"
        ).pack()


        self.password = tk.Entry(
            frame,
            font=("Arial", 13),
            width=28,
            show="*"
        )

        self.password.pack(
            pady=8
        )

        # LOGIN BUTTON

        tk.Button(
            frame,
            text="LOGIN",
            font=("Arial", 12, "bold"),
            bg="#2563EB",
            fg="white",
            width=20,
            command=self.login
        ).pack(
            pady=20
        )

    # LOGIN FUNCTION

    def login(self):

        username = self.username.get().strip()
        password = self.password.get().strip()


        if username == "" or password == "":

            messagebox.showwarning(
                "Warning",
                "Please enter username and password."
            )

            return


        try:

            result = check_login(
                username,
                password
            )


            if result:

                # Remove login widgets
                for widget in self.root.winfo_children():
                    widget.destroy()


                # Open Home page
                Home(
                    self.root
                )


            else:

                messagebox.showerror(
                    "Login Failed",
                    "Invalid username or password."
                )


        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )
