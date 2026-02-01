# ═══════════════════════════════════════════════════════════════════════════
# 📊 SALES ANALYSIS & FORECASTING APP (GUI)
# ═══════════════════════════════════════════════════════════════════════════
#
# A professional desktop application for sales analysis and forecasting
# using Tkinter GUI with interactive visualizations.
#
# Features:
#   ✓ Load CSV data or use sample dataset
#   ✓ View monthly sales trends
#   ✓ Analyze top products, customers, and regions
#   ✓ Generate 6-month sales forecasts
#   ✓ Display comprehensive business insights
#   ✓ Beautiful, responsive user interface
#
# Author: SUSHIL.RK | Last Updated: February 2026
# ═══════════════════════════════════════════════════════════════════════════
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import tkinter as tk
from tkinter import filedialog, messagebox
from io import StringIO

sns.set_style('whitegrid')


class SalesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📊 Sales Analysis & Forecasting")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.df = None
        self.monthly_sales = None
        self.top_products = None
        self.region_sales = None
        self.top_customers = None
        self.forecast = None

        self.create_start_page()

    # ---------------- START PAGE ----------------
    def create_start_page(self):
        self.start_frame = tk.Frame(self.root, bg="#f0f4f8")
        self.start_frame.pack(fill="both", expand=True)

        title = tk.Label(
            self.start_frame,
            text="📊 Sales Analysis & Forecasting",
            font=("Helvetica", 24, "bold"),
            bg="#f0f4f8",
            fg="#2c3e50"
        )
        title.pack(pady=40)

        subtitle = tk.Label(
            self.start_frame,
            text="Analyze your sales data and forecast future trends\nwith just a few clicks!",
            font=("Helvetica", 14),
            bg="#f0f4f8",
            fg="#34495e"
        )
        subtitle.pack(pady=20)

        start_button = tk.Button(
            self.start_frame,
            text="🚀 Start",
            font=("Helvetica", 16, "bold"),
            bg="#3498db",
            fg="white",
            activebackground="#2980b9",
            activeforeground="white",
            padx=20,
            pady=10,
            command=self.show_main_dashboard
        )
        start_button.pack(pady=40)

    # ---------------- DASHBOARD ----------------
    def show_main_dashboard(self):
        self.start_frame.destroy()

        self.dashboard_frame = tk.Frame(self.root, bg="#ecf0f1")
        self.dashboard_frame.pack(fill="both", expand=True, padx=20, pady=20)

        heading = tk.Label(
            self.dashboard_frame,
            text="📈 Sales Dashboard",
            font=("Helvetica", 20, "bold"),
            bg="#ecf0f1",
            fg="#2c3e50"
        )
        heading.pack(pady=10)

        btn_style = {
            "font": ("Helvetica", 12),
            "width": 32,
            "bg": "#3498db",
            "fg": "white",
            "activebackground": "#2980b9",
            "activeforeground": "white",
            "bd": 0,
            "pady": 5
        }

        tk.Button(self.dashboard_frame, text="Load CSV", command=self.load_csv, **btn_style).pack(pady=5)
        tk.Button(self.dashboard_frame, text="Load Sample CSV", command=self.load_sample_csv, **btn_style).pack(pady=5)
        tk.Button(self.dashboard_frame, text="Monthly Sales Trend", command=self.plot_monthly_sales, **btn_style).pack(pady=5)
        tk.Button(self.dashboard_frame, text="Top 10 Products", command=self.plot_top_products, **btn_style).pack(pady=5)
        tk.Button(self.dashboard_frame, text="Sales by Region", command=self.plot_region_sales, **btn_style).pack(pady=5)
        tk.Button(self.dashboard_frame, text="Top 10 Customers", command=self.plot_top_customers, **btn_style).pack(pady=5)
        tk.Button(self.dashboard_frame, text="Forecast Next 6 Months", command=self.plot_forecast, **btn_style).pack(pady=5)
        tk.Button(self.dashboard_frame, text="Show Insights", command=self.show_insights, **btn_style).pack(pady=5)

    # ---------------- LOAD CSV ----------------
    def load_csv(self):
        file_path = filedialog.askopenfilename(title="Select Sales CSV", filetypes=[("CSV files", "*.csv")])
        if not file_path:
            messagebox.showwarning("Warning", "No file selected!")
            return
        try:
            self.df = pd.read_csv(file_path, encoding='utf-8')
            self.process_dataframe()
            messagebox.showinfo("Success", f"CSV loaded successfully! {self.df.shape[0]} rows processed.")
            self.plot_monthly_sales()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV:\n{str(e)}")

    # ---------------- LOAD SAMPLE CSV ----------------
    def load_sample_csv(self):
        csv_data = """Date,Sales,Product,Region,Customer ID
2023-01-05,1200,Product A,North,1001
2023-01-12,800,Product B,South,1002
2023-01-18,950,Product C,East,1003
2023-02-02,1300,Product A,North,1004
2023-02-11,700,Product B,West,1001
2023-02-20,1650,Product D,South,1005
2023-03-03,2000,Product C,East,1002
2023-03-15,1550,Product E,North,1006
2023-03-26,900,Product A,West,1003
2023-04-05,2200,Product B,South,1005
2023-04-18,1100,Product D,East,1007
2023-04-27,1400,Product C,North,1004
2023-05-08,1750,Product E,West,1008
2023-05-17,1300,Product A,North,1002
2023-05-29,1600,Product B,South,1009
2023-06-05,2100,Product C,East,1003
2023-06-13,950,Product D,West,1010
2023-06-25,1250,Product E,North,1001
2023-07-02,1800,Product A,South,1011
2023-07-14,1400,Product B,East,1008
2023-07-28,1750,Product C,West,1004
2023-08-03,2300,Product D,North,1006
2023-08-17,900,Product A,South,1009
2023-08-26,1500,Product E,East,1012
2023-09-04,1950,Product B,North,1003
2023-09-16,1700,Product C,West,1001
2023-09-29,2100,Product D,South,1010
2023-10-07,1600,Product E,East,1002
2023-10-20,1300,Product A,North,1007
2023-10-30,2000,Product B,West,1011
2023-11-05,2200,Product C,South,1005
2023-11-18,1800,Product D,East,1004
2023-11-28,1400,Product E,North,1008
2023-12-02,2500,Product A,West,1012
2023-12-14,1950,Product B,East,1009
2023-12-27,1650,Product C,South,1010"""
        try:
            self.df = pd.read_csv(StringIO(csv_data))
            self.process_dataframe()
            messagebox.showinfo("Success", f"Sample CSV loaded successfully! {self.df.shape[0]} rows.")
            self.plot_monthly_sales()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load sample CSV:\n{str(e)}")

    # ---------------- PROCESS DATAFRAME ----------------
    def process_dataframe(self):
        self.df.drop_duplicates(inplace=True)
        self.df['Date'] = pd.to_datetime(self.df['Date'].astype(str).str.strip(), errors='coerce')
        self.df.dropna(subset=['Date'], inplace=True)
        self.df['Sales'] = pd.to_numeric(self.df['Sales'], errors='coerce')
        self.df.dropna(subset=['Sales'], inplace=True)

        self.monthly_sales = self.df.groupby(self.df['Date'].dt.to_period('M'))['Sales'].sum()
        self.monthly_sales.index = self.monthly_sales.index.to_timestamp()
        self.monthly_sales = self.monthly_sales.asfreq('MS')

        self.top_products = self.df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(10)
        self.region_sales = self.df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
        self.top_customers = self.df.groupby('Customer ID')['Sales'].sum().sort_values(ascending=False).head(10)

        n = len(self.monthly_sales)
        if n >= 24:
            model = ExponentialSmoothing(self.monthly_sales, trend='add', seasonal='add', seasonal_periods=12).fit()
        elif n >= 2:
            model = ExponentialSmoothing(self.monthly_sales, trend='add', seasonal=None).fit()
        else:
            self.forecast = None
            return

        self.forecast = model.forecast(6)

    # ---------------- PLOTS ----------------
    def plot_monthly_sales(self):
        if self.monthly_sales is None:
            messagebox.showwarning("Warning", "Load a CSV first!")
            return
        plt.figure(figsize=(10, 5), num="Monthly Sales Trend")
        self.monthly_sales.plot(marker='o', title="Monthly Sales Trend")
        plt.xlabel("Month")
        plt.ylabel("Sales")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def plot_top_products(self):
        if self.top_products is None:
            messagebox.showwarning("Warning", "Load a CSV first!")
            return
        plt.figure(figsize=(10, 5), num="Top Products")
        sns.barplot(x=self.top_products.values, y=self.top_products.index.tolist(), palette='viridis')
        plt.title("Top 10 Products by Sales")
        plt.xlabel("Sales")
        plt.ylabel("Product")
        plt.tight_layout()
        plt.show()

    def plot_region_sales(self):
        if self.region_sales is None:
            messagebox.showwarning("Warning", "Load a CSV first!")
            return
        plt.figure(figsize=(8, 6), num="Sales by Region")
        self.region_sales.plot(kind='pie', autopct='%1.1f%%')
        plt.title("Sales by Region")
        plt.ylabel("")
        plt.tight_layout()
        plt.show()

    def plot_top_customers(self):
        if self.top_customers is None:
            messagebox.showwarning("Warning", "Load a CSV first!")
            return
        plt.figure(figsize=(10, 5), num="Top Customers")
        sns.barplot(x=self.top_customers.values, y=[str(c) for c in self.top_customers.index], palette='magma')
        plt.title("Top 10 Customers by Purchase Amount")
        plt.xlabel("Sales")
        plt.ylabel("Customer ID")
        plt.tight_layout()
        plt.show()

    def plot_forecast(self):
        if self.forecast is None:
            messagebox.showwarning("Warning", "Not enough data to forecast. Need at least 2 months of sales.")
            return
        plt.figure(figsize=(10, 5), num="Sales Forecast")
        self.monthly_sales.plot(label='Historical Sales', marker='o')
        self.forecast.plot(label='Forecast', marker='o', linestyle='--')
        plt.title("Sales Forecast for Next 6 Months")
        plt.xlabel("Month")
        plt.ylabel("Sales")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    # ---------------- INSIGHTS ----------------
    def show_insights(self):
        if self.df is None:
            messagebox.showwarning("Warning", "Load a CSV first!")
            return
        insights = "--- Key Insights ---\n\n"
        insights += f"Top Products:\n{self.top_products}\n\n"
        insights += f"Sales by Region:\n{self.region_sales}\n\n"
        insights += f"Top Customers:\n{self.top_customers}\n\n"
        if self.forecast is not None:
            insights += f"Forecast for Next 6 Months:\n{self.forecast}\n"
        else:
            insights += "Forecast: Not enough data (need at least 2 months).\n"
        messagebox.showinfo("Insights", insights)


if __name__ == "__main__":
    root = tk.Tk()
    app = SalesApp(root)
    root.mainloop()
