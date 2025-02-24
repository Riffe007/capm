import tkinter as tk
from tkinter import messagebox
import logging
from functools import wraps
from typing import Callable

# Configure logging for detailed traceability
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def log_call(func: Callable) -> Callable:
    """
    Decorator to log function calls and their results.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__}...")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

class CAPMCalculator:
    """
    Encapsulates CAPM calculations.
    """
    @staticmethod
    @log_call
    def calculate_expected_return(risk_free_rate: float, beta: float, expected_market_return: float) -> float:
        """
        Calculate the expected return using the CAPM formula.
        
        Expected Return = Risk-Free Rate + Beta * (Expected Market Return - Risk-Free Rate)
        
        :param risk_free_rate: The risk-free rate.
        :param beta: Beta of the asset.
        :param expected_market_return: The expected market return.
        :return: The expected return of the asset.
        """
        return risk_free_rate + beta * (expected_market_return - risk_free_rate)

class CAPMApp(tk.Tk):
    """
    The main application window for the CAPM Calculator.
    """
    def __init__(self) -> None:
        super().__init__()
        self.title("CAPM Calculator")
        self.configure_gui()
        self.create_widgets()

    def configure_gui(self) -> None:
        self.geometry("400x300")
        self.resizable(False, False)

    def create_widgets(self) -> None:
        # Create sliders with grid layout for a more structured interface
        self.risk_free_rate_slider = tk.Scale(self, from_=0, to=1, resolution=0.01,
                                              orient=tk.HORIZONTAL, label="Risk-Free Rate")
        self.beta_slider = tk.Scale(self, from_=0, to=2, resolution=0.01,
                                    orient=tk.HORIZONTAL, label="Beta")
        self.expected_market_return_slider = tk.Scale(self, from_=0, to=1, resolution=0.01,
                                                      orient=tk.HORIZONTAL, label="Expected Market Return")

        self.calculate_button = tk.Button(self, text="Calculate Expected Return",
                                          command=self.calculate_and_display_expected_return)
        self.result_label = tk.Label(self, text="Expected Return: N/A", font=("Helvetica", 14))

        # Position widgets using grid
        self.risk_free_rate_slider.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.beta_slider.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.expected_market_return_slider.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        self.calculate_button.grid(row=3, column=0, padx=10, pady=10)
        self.result_label.grid(row=4, column=0, padx=10, pady=10)

    def calculate_and_display_expected_return(self) -> None:
        """
        Retrieve values from the sliders, calculate the expected return,
        and update the result label.
        """
        try:
            risk_free_rate = self.risk_free_rate_slider.get()
            beta = self.beta_slider.get()
            expected_market_return = self.expected_market_return_slider.get()

            expected_return = CAPMCalculator.calculate_expected_return(
                risk_free_rate, beta, expected_market_return
            )
            self.result_label.config(text=f"Expected Return: {expected_return:.2f}")
        except Exception as e:
            logging.error("Error calculating expected return", exc_info=True)
            messagebox.showerror("Error", "An error occurred while calculating the expected return.")

def main() -> None:
    app = CAPMApp()
    app.mainloop()

if __name__ == "__main__":
    main()
