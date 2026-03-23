# Data Directory

This directory is intended for storing energy consumption datasets used in the analysis.

## Recommended Public Data Sources

### Germany

1. **SMARD (Strommarktdaten)** - Bundesnetzagentur
   - URL: https://www.smard.de/en/downloadcenter/download-market-data
   - Data: Electricity generation, consumption, and prices in Germany
   - Format: CSV, XLSX
   - Free access

2. **Open Power System Data (OPSD)**
   - URL: https://open-power-system-data.org/
   - Data: Time series data on electricity consumption, generation, and prices
   - Format: CSV
   - Openly licensed

3. **Agora Energiewende**
   - URL: https://www.agora-energiewende.de/service/agorameter/chart/power_generation/
   - Data: Real-time electricity generation and consumption
   - Format: CSV export available

### International

4. **IEA (International Energy Agency)**
   - URL: https://www.iea.org/data-and-statistics
   - Data: Global energy statistics
   - Some datasets require registration

5. **Eurostat - Energy Statistics**
   - URL: https://ec.europa.eu/eurostat/web/energy/data
   - Data: European Union energy consumption and production
   - Format: Various

6. **U.S. Energy Information Administration (EIA)**
   - URL: https://www.eia.gov/opendata/
   - Data: U.S. energy consumption, production, and prices
   - API available

## Data Format

The `analysis.py` script expects a CSV file with the following columns:

- `timestamp`: Date and time (YYYY-MM-DD HH:MM:SS format)
- `consumption_kwh`: Energy consumption in kilowatt-hours
- `temperature_c` (optional): Temperature in Celsius

### Example data structure:

```csv
timestamp,consumption_kwh,temperature_c
2026-01-01 00:00:00,85.3,12.5
2026-01-01 01:00:00,78.2,11.8
2026-01-01 02:00:00,72.1,11.2
```

## Usage

1. Download data from one of the sources above
2. Save the CSV file as `energy_data.csv` in this directory
3. Ensure the file follows the expected format (or modify the script accordingly)
4. Run the analysis script: `python analysis.py`

## Note on Sample Data

If no data file is found, the `analysis.py` script will automatically generate sample data for demonstration purposes. This is useful for testing the analysis pipeline without downloading real data.
