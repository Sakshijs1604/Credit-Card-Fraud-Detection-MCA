import os
import tkinter as tk
from tkinter import messagebox

import joblib
import numpy as np

from database import save_prediction


# ==========================================
# PROJECT PATH
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


# ==========================================
# MODEL FILES
# ==========================================

MODEL_FILE = os.path.join(
    BASE_DIR,
    "fraud_model_6.pkl"
)

SCALER_FILE = os.path.join(
    BASE_DIR,
    "scaler_6.pkl"
)


# ==========================================
# PREDICTION PAGE
# ==========================================

class Prediction:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Credit Card Fraud Detection - Prediction"
        )

        self.root.geometry(
            "900x650"
        )

        self.root.configure(
            bg="#eff6ff"
        )

        self.root.resizable(
            False,
            False
        )


        # ==========================================
        # CHECK MODEL FILE
        # ==========================================

        if not os.path.exists(MODEL_FILE):

            messagebox.showerror(
                "Model Not Found",
                "fraud_model_6.pkl not found.\n\n"
                "Please run model.py first."
            )

            return


        # ==========================================
        # CHECK SCALER FILE
        # ==========================================

        if not os.path.exists(SCALER_FILE):

            messagebox.showerror(
                "Scaler Not Found",
                "scaler_6.pkl not found.\n\n"
                "Please run model.py first."
            )

            return


        # ==========================================
        # LOAD MODEL
        # ==========================================

        try:

            self.model = joblib.load(
                MODEL_FILE
            )

            self.scaler = joblib.load(
                SCALER_FILE
            )

        except Exception as e:

            messagebox.showerror(
                "Model Error",
                str(e)
            )

            return


        # ==========================================
        # EXACTLY 6 INPUT FEATURES
        # ==========================================

        self.fields = [
            "Time",
            "V1",
            "V2",
            "V3",
            "V4",
            "Amount"
        ]


        self.entries = {}


        # ==========================================
        # TITLE
        # ==========================================

        title = tk.Label(

            self.root,

            text="FRAUD TRANSACTION PREDICTION",

            font=(
                "Arial",
                24,
                "bold"
            ),

            bg="#eff6ff",

            fg="#172554"
        )

        title.pack(
            pady=25
        )


        # ==========================================
        # SUBTITLE
        # ==========================================

        subtitle = tk.Label(

            self.root,

            text="Enter transaction details",

            font=(
                "Arial",
                13
            ),

            bg="#eff6ff",

            fg="#475569"
        )

        subtitle.pack(
            pady=5
        )


        # ==========================================
        # INPUT FRAME
        # ==========================================

        input_frame = tk.Frame(

            self.root,

            bg="white",

            bd=2,

            relief="groove"
        )

        input_frame.pack(
            padx=30,
            pady=20
        )


        # ==========================================
        # CREATE 6 INPUT BOXES
        # ==========================================

        for i, field in enumerate(
            self.fields
        ):

            row = i // 2

            column = i % 2


            field_frame = tk.Frame(

                input_frame,

                bg="white"
            )

            field_frame.grid(

                row=row,

                column=column,

                padx=35,

                pady=15
            )


            label = tk.Label(

                field_frame,

                text=field,

                font=(
                    "Arial",
                    12,
                    "bold"
                ),

                bg="white",

                fg="#172554"
            )

            label.pack(
                anchor="w"
            )


            entry = tk.Entry(

                field_frame,

                font=(
                    "Arial",
                    12
                ),

                width=25,

                bd=2,

                relief="solid"
            )

            entry.pack(
                pady=5
            )


            self.entries[field] = entry


        # ==========================================
        # PREDICT BUTTON
        # ==========================================

        predict_button = tk.Button(

            self.root,

            text="PREDICT",

            font=(
                "Arial",
                13,
                "bold"
            ),

            bg="#2563eb",

            fg="white",

            activebackground="#1d4ed8",

            activeforeground="white",

            width=20,

            height=2,

            command=self.predict
        )

        predict_button.pack(
            pady=8
        )


        # ==========================================
        # CLEAR BUTTON
        # ==========================================

        clear_button = tk.Button(

            self.root,

            text="CLEAR",

            font=(
                "Arial",
                11,
                "bold"
            ),
            bg="#dc2626",
            fg="white",


            width=20,

            command=self.clear
        )

        clear_button.pack(
            pady=5
        )


        # ==========================================
        # BACK TO HOME
        # ==========================================

        back_button = tk.Button(

            self.root,

            text="BACK TO HOME",

            font=(
                "Arial",
                11,
                "bold"
            ),
            bg="#172554",
            fg="white",

            width=20,

            command=self.back_home
        )

        back_button.pack(
            pady=5
        )


        # ==========================================
        # RESULT LABEL
        # ==========================================

        self.result_label = tk.Label(

            self.root,

            text="",

            font=(
                "Arial",
                17,
                "bold"
            ),

            bg="#eff6ff"
        )

        self.result_label.pack(
            pady=15
        )


    # =================================================
    # PREDICTION FUNCTION
    # =================================================

    def predict(self):

        try:

            values = []


            # ==========================================
            # GET 6 VALUES
            # ==========================================

            for field in self.fields:

                value = self.entries[
                    field
                ].get().strip()


                # Empty value
                if value == "":

                    messagebox.showwarning(

                        "Missing Value",

                        f"Please enter {field}."
                    )

                    self.entries[
                        field
                    ].focus()

                    return


                # Convert to float
                try:

                    number = float(
                        value
                    )

                except ValueError:

                    messagebox.showerror(

                        "Invalid Input",

                        f"{field} must contain "
                        "a numeric value."
                    )

                    self.entries[
                        field
                    ].focus()

                    return


                values.append(
                    number
                )


            # ==========================================
            # INPUT ORDER
            # ==========================================
            #
            # 1. Time
            # 2. V1
            # 3. V2
            # 4. V3
            # 5. V4
            # 6. Amount
            #
            # ==========================================

            input_data = np.array(
                values,
                dtype=float
            ).reshape(
                1,
                6
            )


            # ==========================================
            # SCALE INPUT
            # ==========================================

            input_scaled = self.scaler.transform(
                input_data
            )


            # ==========================================
            # PREDICT
            # ==========================================

            prediction = self.model.predict(
                input_scaled
            )[0]


            # ==========================================
            # FRAUD PROBABILITY
            # ==========================================

            probability = self.model.predict_proba(
                input_scaled
            )[0][1]


            probability_percent = (
                probability * 100
            )


            # ==========================================
            # TRANSACTION AMOUNT
            # ==========================================

            amount = values[5]


            # ==========================================
            # FRAUD TRANSACTION
            # ==========================================

            if prediction == 1:

                result = (
                    "FRAUDULENT TRANSACTION"
                )


                self.result_label.config(

                    text=(
                        "⚠ FRAUDULENT TRANSACTION\n\n"
                        "Fraud Probability: "
                        f"{probability_percent:.2f}%"
                    ),

                    fg="#dc2626"
                )


            # ==========================================
            # LEGITIMATE TRANSACTION
            # ==========================================

            else:

                result = (
                    "LEGITIMATE TRANSACTION"
                )


                self.result_label.config(

                    text=(
                        "✓ LEGITIMATE TRANSACTION\n\n"
                        "Fraud Probability: "
                        f"{probability_percent:.2f}%"
                    ),

                    fg="#16a34a"
                )


            # ==========================================
            # SAVE RESULT TO MYSQL
            # ==========================================

            try:

                save_prediction(

                    amount,

                    result,

                    probability_percent
                )

            except Exception as database_error:

                messagebox.showwarning(

                    "Database Warning",

                    "Prediction completed, "
                    "but result could not be "
                    "saved to database.\n\n"
                    + str(database_error)
                )


            # ==========================================
            # SHOW RESULT
            # ==========================================

            messagebox.showinfo(

                "Prediction Result",

                f"Result:\n\n"
                f"{result}\n\n"
                f"Fraud Probability: "
                f"{probability_percent:.2f}%"
            )


        except Exception as e:

            messagebox.showerror(

                "Prediction Error",

                str(e)
            )


    # =================================================
    # CLEAR FUNCTION
    # =================================================

    def clear(self):

        for entry in self.entries.values():

            entry.delete(
                0,
                tk.END
            )


        self.result_label.config(
            text=""
        )


    # =================================================
    # BACK TO HOME
    # =================================================

    def back_home(self):

        from home import Home


        for widget in self.root.winfo_children():

            widget.destroy()


        Home(
            self.root
        )
