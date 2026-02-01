# 📊 Sales Forecasting App

> **Turning data into insights** 💡

A professional desktop application for analyzing historical sales data and forecasting future sales with an intuitive GUI. Built with Python and Tkinter, the app provides comprehensive sales insights and predictive analytics using advanced time series forecasting.

**Author:** SUSHIL.RK | **Last Updated:** February 2026

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📁 **Data Import** | Load sales data from CSV files or use the included sample dataset |
| 📈 **Sales Analysis** | Visualize monthly sales trends and identify top-performing products & customers |
| 🗺️ **Regional Insights** | Analyze sales distribution across different geographic regions |
| 🔮 **Sales Forecasting** | Predict the next 6 months using Holt-Winters Exponential Smoothing |
| 💡 **Key Insights** | Display important metrics and statistics in interactive popups |
| 🎨 **Interactive GUI** | User-friendly Tkinter interface with responsive, intuitive design |
| 🧹 **Data Cleaning** | Automatic removal of duplicates and comprehensive date validation |

---

## 📋 Prerequisites

| Requirement | Version |
|------------|---------|
| **Python** | 3.8 or higher |
| **pandas** | Data manipulation and analysis |
| **matplotlib** | Plotting and visualization |
| **seaborn** | Statistical data visualization |
| **statsmodels** | Time series forecasting |
| **tkinter** | GUI framework (included with Python) |

### 📦 Install Dependencies

```bash
pip install pandas matplotlib seaborn statsmodels
```

Or install all at once:

```bash
pip install -r requirements.txt
```

---

## 🚀 Quick Start

### Option 1: Run the GUI Application

#### Step 1️⃣ Clone/Download
```bash
git clone <repository-url>
cd Sales-Analysis-Project
```

#### Step 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 3️⃣ Launch the App
```bash
python Sales_Analysis_Project_app.py
```

✅ The app window will open automatically. Load your CSV file or use sample data to get started!

---

## 🔧 Build Standalone Desktop App with PyInstaller

Convert the Python application into a standalone Windows executable that doesn't require Python installation.

### 📥 Step 1: Install PyInstaller

```bash
pip install pyinstaller
```

### 🔨 Step 2: Build the Executable

Choose one of the following options:

#### Option A: Basic Build
```bash
pyinstaller --onefile --windowed Sales_Analysis_Project_app.py
```

#### Option B: Enhanced Build (with metadata)
```bash
pyinstaller --onefile --windowed --icon=icon.ico --name="Sales Forecasting App" Sales_Analysis_Project_app.py
```

#### Option C: Optimized Build (recommended)
```bash
pyinstaller --onefile --windowed --noconfirm --log-level=ERROR Sales_Analysis_Project_app.py
```

### 📍 Step 3: Locate Your Executable

The standalone `.exe` file will be created in:
```
dist/Sales_Analysis_Project_app.exe
```

### 📤 Step 4: Distribute

- ✅ Copy the `.exe` file from the `dist/` folder
- ✅ Users can run it directly without Python installation
- ✅ Include sample CSV files for easy data loading

---

## 📊 Sample CSV Format

Your sales data CSV file should have the following structure:

```csv
Date,Product,Customer,Quantity,Price,Region
2024-01-15,Laptop,Acme Corp,5,1200,North
2024-01-16,Mouse,Tech Solutions,20,25,South
2024-01-17,Keyboard,Global Industries,10,75,East
2024-01-18,Monitor,ABC Company,3,350,West
2024-01-19,Laptop,XYZ Corporation,2,1200,North
```

### Required Columns

| Column | Format | Description |
|--------|--------|-------------|
| `Date` | YYYY-MM-DD | Transaction date |
| `Product` | Text | Product name |
| `Customer` | Text | Customer name |
| `Quantity` | Number | Units sold |
| `Price` | Number | Price per unit |
| `Region` | Text | Geographic region/location |

---

## 📁 Project Structure

```
Sales-Analysis-Project/
├── src/
│   ├── Sales_Analysis_Project_app.py    # Main GUI application
│   ├── Sales_Analysis_Project.py        # Core analysis functions
│   └── sales_data.csv                    # Sample dataset (35 transactions)
├── requirements.txt                      # Python dependencies
├── README.md                              # Project documentation
└── LICENSE                                # License file

```

---

## 🔄 Typical Workflow

```
1. Load Data
   ↓
2. View Monthly Trends & Insights
   ↓
3. Analyze Top Products/Customers/Regions
   ↓
4. Generate Forecast for Next 6 Months
   ↓
5. Export or Print Results
```

### Step-by-Step Usage

| Step | Action | Description |
|------|--------|-------------|
| 1 | **Load Data** | Click "Load CSV File" or use sample data provided |
| 2 | **Analyze Trends** | View monthly sales, top products, and regional data |
| 3 | **Generate Insights** | Display key metrics and important statistics |
| 4 | **Forecast Sales** | Predict the next 6 months using time series analysis |
| 5 | **Review Results** | Study the visualizations and metrics |

---

## 🛠️ Technologies Used

```
Technology        : Purpose
----------------------------
🐍 Python 3.8+    : Programming Language
🪟 Tkinter        : Desktop GUI Framework
📊 Pandas         : Data Processing
📈 Matplotlib     : Visualization
📉 Seaborn        : Statistical Graphics
🔮 Statsmodels    : Time Series Forecasting
🔧 PyInstaller    : Executable Bundling


```

---

## 📝 Usage Examples

### Running the GUI Application
```bash
python Sales_Analysis_Project_app.py
```

### Using Core Functions Programmatically
```python
from Sales_Analysis_Project import *
import pandas as pd

# Load your data
df = pd.read_csv('sales_data.csv')

# Perform analysis
monthly_sales = analyze_monthly_sales(df)
top_products = get_top_products(df)
region_sales = analyze_regional_sales(df)

# Generate forecast
forecast = forecast_sales(monthly_sales)
```

---

## 🐛 Troubleshooting

### Problem: ModuleNotFoundError
**Error:** `ModuleNotFoundError: No module named 'pandas'`

**Solution:** Install all dependencies:
```bash
pip install -r requirements.txt
```

### Problem: GUI Won't Open
**Error:** Window doesn't appear when running the app

**Solution:** Ensure Tkinter is installed:
- **Windows:** Already included with Python
- **Linux:** Run `sudo apt-get install python3-tk`
- **macOS:** Run `brew install python3-tk`

### Problem: CSV File Won't Load
**Error:** File loads but data is incorrect

**Solution:** Verify:
- ✓ CSV format matches the required columns
- ✓ Date column is in YYYY-MM-DD format
- ✓ No empty rows in the middle of data
- ✓ File encoding is UTF-8

### Problem: Forecast Won't Generate
**Error:** Error during forecasting

**Solution:**
- ✓ Ensure you have at least 12 months of data
- ✓ Check for missing/NaN values in Sales column
- ✓ Verify data is properly cleaned

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License - Free to use, modify, and distribute
```

---

## 👤 Author & Contact

**SUSHIL.RK**

> *Transforming raw sales data into actionable business intelligence*

📧 For questions, feedback, or contributions, feel free to reach out!

---

## 🎯 Roadmap & Future Enhancements

- [ ] ✨ Support for Excel files (.xlsx, .xls)
- [ ] 🤖 Advanced forecasting models (ARIMA, Prophet, LSTM)
- [ ] 📅 Custom date range selection for forecasting
- [ ] 📄 Export reports as PDF/Excel
- [ ] 🔄 Real-time data updates from APIs
- [ ] 🌐 Multi-language support (EN, ES, FR, etc.)
- [ ] 🎨 Theme customization (dark mode, light mode)
- [ ] 📱 Web-based dashboard version
- [ ] 💾 Database integration (SQLite, PostgreSQL)
- [ ] 🔔 Automated email reports

---

## ⭐ Show Your Support

If you find this project helpful, please:
- ⭐ Give it a star on GitHub
- 🍴 Fork the repository
- 📢 Share with your network
- 💬 Provide feedback and suggestions

---

**Made with ❤️ using Python** 
