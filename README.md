# Energy Consumption Analysis

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A comprehensive Python-based energy consumption analysis tool that processes, analyzes, and visualizes energy usage patterns from public data sources.

## 💡 Project Overview

This project provides data-driven insights into energy consumption patterns through statistical analysis and visualization. It's designed to work with real-world energy datasets from sources like SMARD (Bundesnetzagentur), Open Power System Data, and other public energy databases.

### Key Features

- **Automated Data Processing**: Load and process energy consumption data from CSV files
- **Statistical Analysis**: Calculate consumption statistics including peaks, averages, and trends
- **Temporal Pattern Analysis**: 
  - Hourly consumption patterns
  - Monthly trends
  - Weekday vs. weekend comparisons
- **Correlation Analysis**: Examine relationships between temperature and energy consumption
- **Visualization**: Generate publication-ready plots and charts
- **Sample Data Generation**: Built-in realistic sample data for testing and demonstration

## 🛠️ Tech Stack

- **Python 3.8+**
- **pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib**: Data visualization
- **Seaborn**: Statistical data visualization

## 📁 Project Structure

```
Energy_Consumption_Analysis/
├── analysis.py              # Main analysis script
├── requirements.txt         # Python dependencies
├── data/
│   ├── README.md            # Data sources and format documentation
│   └── energy_data.csv      # Your energy data (place here)
├── LICENSE
└── README.md
```

## 🚀 Getting Started

### Prerequisites

Python 3.8 or higher installed on your system.

### Installation

1. Clone the repository:
```bash
git clone https://github.com/eboekenh/Energy_Consumption_Analysis.git
cd Energy_Consumption_Analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

#### Option 1: Using Real Data

1. Download energy consumption data from one of the recommended sources (see `data/README.md`)
2. Save your CSV file as `data/energy_data.csv`
3. Run the analysis:
```bash
python analysis.py
```

#### Option 2: Using Sample Data

If no data file is found, the script automatically generates realistic sample data:
```bash
python analysis.py
```

### Output

The analysis generates:
- **Console output**: Statistical summaries and key findings
- **Visualizations**: PNG files for each analysis type
  - `hourly_consumption_pattern.png`
  - `monthly_consumption.png`
  - `weekday_weekend_comparison.png`
  - `temperature_correlation.png`

## 📊 Example Analysis Results

The tool provides insights such as:

- Total and average daily consumption
- Peak consumption hours
- Seasonal variations
- Impact of temperature on energy usage
- Weekday vs. weekend consumption differences

## 📚 Data Sources

Recommended public energy datasets:

### Germany
- **SMARD** (Bundesnetzagentur) - Electricity market data
- **Open Power System Data** - Open-licensed time series data
- **Agora Energiewende** - Real-time generation and consumption

### International
- **IEA** - International Energy Agency statistics
- **Eurostat** - European Union energy data
- **U.S. EIA** - Energy Information Administration

See `data/README.md` for detailed information and links.

## 📝 Use Cases

- **Energy Efficiency Research**: Identify consumption patterns and optimization opportunities
- **Data Science Portfolio**: Demonstrate data analysis and visualization skills
- **Sustainability Analysis**: Understand energy usage trends
- **Educational Tool**: Learn data analysis with real-world energy data

## 🛡️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**eboekenh**
- GitHub: [@eboekenh](https://github.com/eboekenh)
- Location: Berlin, Germany

## 🔧 Future Enhancements

- [ ] Add predictive modeling capabilities
- [ ] Interactive dashboard with Streamlit or Dash
- [ ] Support for additional data formats (JSON, XLSX)
- [ ] Automated report generation (PDF)
- [ ] API integration for real-time data fetching

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

*Built with ❤️ in Berlin | March 2026*
