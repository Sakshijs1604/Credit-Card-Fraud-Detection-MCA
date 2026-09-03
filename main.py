import tkinter as tk

from login import Login


def main():

    root = tk.Tk()

    root.title(
        "Credit Card Fraud Detection System"
    )

    root.geometry("1000x600")

    root.configure(
        bg="#172554"
    )

    root.resizable(
        True,
        True
    )

    Login(root)

    root.mainloop()


if __name__ == "__main__":
    main()
