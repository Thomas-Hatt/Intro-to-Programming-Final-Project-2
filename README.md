# 📦 Jake's Shipping Calculator

This Python script provides a simple command-line tool to calculate the estimated shipping cost for a package across multiple carriers and automatically find the best, lowest-cost shipping option.

-----

## ✨ Features

  * **Cost Calculation:** Calculates the total shipping price based on a **flat fee**, **rate per pound**, and **oversize charge**.
  * **Oversize Logic:** Automatically applies an extra percentage fee if the package's combined dimensions (Length + Width + Height) exceed a carrier's defined limit.
  * **Best Option Finder:** Compares prices across all supported carriers and identifies the **cheapest option** for your specific package.
  * **Interactive Interface:** A simple, menu-driven command-line interface for inputting package details and selecting carriers.
  * **Carrier Data Display:** Allows users to view all current carrier pricing and dimension data.

-----

## 🛠️ How to Use

### 📥 Download

To use the calculator, you need to download the Python script file (e.g., `shipping_calculator.py`) and have a Python interpreter installed on your system.

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/Thomas-Hatt/Intro-to-Programming-Final-Project-2.git
    cd Intro-to-Programming-Final-Project-2
    ```

2.  **Download Directly:**
    You can also download the Python file directly from the GitHub page and save it locally.

### 🚀 Running the Script

1.  Open your terminal or command prompt.

2.  Navigate to the directory where you saved the file.

3.  Run the script using the Python interpreter:

    ```bash
    python shipping_calculator.py
    ```

### 📋 Interactive Menu

Once running, you'll be greeted with the main menu:

1.  **Display Companies:** Shows the current flat fee, rate per pound, oversize dimension limit, and overcharge fee for each carrier.
2.  **Ship Package:** Prompts you to enter your package's **Length, Width, Height (inches)**, and **Weight (pounds)**. It then allows you to:
      * Select a specific carrier (1, 2, or 3) to get its cost.
      * Select **4: Calculate Best Option Automatically** to find the carrier with the lowest total price.

Enter **-1** at the main menu to exit the program.

-----

## ⚙️ Customization

The carrier and rate data is stored in lists at the beginning of the script:

```python
lstCompanies = ['Universal Package Sorters (UPS)', 'Federation Excelsior (FedEx)', 'Dependable, Honorable Logisticians (DHL)']
lstFlatFee = [5.74, 3.59, 15.47]
lstRatePerPound = [1.59, 2.05, 1.07]
lstOversizePackageDimensions = [165, 195, 215]
lstOverchargeFee = [0.2, 0.22, 0.1]
```

You can easily **modify or extend** these lists to add new carriers, update rates, or change oversize thresholds. **Ensure all lists maintain the same number of elements and that corresponding values are at the same index.**