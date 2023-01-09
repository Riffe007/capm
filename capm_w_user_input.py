# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 19:04:30 2023

@author: timot
"""

import tkinter as tk

def calculate_expected_return(risk_free_rate, beta, expected_market_return):
  """
  Calculates the expected return of an asset based on the CAPM formula:
  E(R) = Rf + Beta * (E(Rm) - Rf)

  Parameters:
  risk_free_rate (float): The risk-free rate of return.
  beta (float): The beta of the asset, which measures its risk in relation to the market.
  expected_market_return (float): The expected return of the market.

  Returns:
  float: The expected return of the asset.
  """
  expected_return = risk_free_rate + beta * (expected_market_return - risk_free_rate)
  return expected_return

# Create the main window
root = tk.Tk()
root.title("CAPM Calculator")

# Create the sliders for the risk-free rate, beta, and expected market return
risk_free_rate_slider = tk.Scale(root, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, label="Risk-Free Rate")
beta_slider = tk.Scale(root, from_=0, to=2, resolution=0.01, orient=tk.HORIZONTAL, label="Beta")
expected_market_return_slider = tk.Scale(root, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, label="Expected Market Return")

# Create a button to calculate the expected return
button = tk.Button(root, text="Calculate Expected Return", command=lambda: calculate_and_display_expected_return())

# Create a label to display the expected return
label = tk.Label(root)

# Define a function to calculate and display the expected return
def calculate_and_display_expected_return():
  risk_free_rate = risk_free_rate_slider.get()
  beta = beta_slider.get()
  expected_market_return = expected_market_return_slider.get()

  expected_return = calculate_expected_return(risk_free_rate, beta, expected_market_return)
  label.config(text=f"Expected Return: {expected_return:.2f}")

# Pack the widgets into the window
risk_free_rate_slider.pack()
beta_slider.pack()
expected_market_return_slider.pack()
button.pack()
label.pack()

# Run the main loop
root.mainloop()
