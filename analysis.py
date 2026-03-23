"""Energy Consumption Analysis
Analyzing energy consumption patterns from public data sources.

Author: eboekenh
Date: March 2026
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Set visualization style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (14, 6)

class EnergyAnalyzer:
    """Class for analyzing energy consumption data"""
    
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None
        
    def load_data(self):
        """Load energy consumption data from CSV"""
        try:
            self.df = pd.read_csv(self.data_path, parse_dates=['timestamp'])
            print(f"Data loaded successfully: {len(self.df)} records")
            return self.df
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
    
    def generate_sample_data(self, days=365):
        """Generate sample energy consumption data for demonstration"""
        dates = pd.date_range(end=datetime.now(), periods=days*24, freq='H')
        
        # Simulate realistic energy consumption patterns
        hourly_pattern = np.array([50, 45, 42, 40, 38, 40, 55, 75, 90, 95,
                                   100, 105, 110, 108, 105, 103, 100, 110,
                                   120, 115, 95, 80, 70, 60])  # 24 hours
        
        base_consumption = np.tile(hourly_pattern, days)
        seasonal_variation = 20 * np.sin(np.linspace(0, 2*np.pi, len(dates)))
        noise = np.random.normal(0, 5, len(dates))
        
        consumption = base_consumption + seasonal_variation + noise
        consumption = np.maximum(consumption, 0)  # Ensure non-negative
        
        self.df = pd.DataFrame({
            'timestamp': dates,
            'consumption_kwh': consumption,
            'temperature_c': 15 + 10 * np.sin(np.linspace(0, 2*np.pi, len(dates))) + np.random.normal(0, 3, len(dates)),
            'day_of_week': dates.dayofweek,
            'hour': dates.hour,
            'month': dates.month
        })
        
        print(f"Sample data generated: {len(self.df)} records")
        return self.df
    
    def basic_statistics(self):
        """Calculate basic statistics of energy consumption"""
        if self.df is None:
            print("No data loaded. Please load or generate data first.")
            return None
        
        stats = {
            'Total Consumption (kWh)': self.df['consumption_kwh'].sum(),
            'Average Daily Consumption (kWh)': self.df['consumption_kwh'].mean() * 24,
            'Peak Consumption (kWh)': self.df['consumption_kwh'].max(),
            'Minimum Consumption (kWh)': self.df['consumption_kwh'].min(),
            'Standard Deviation': self.df['consumption_kwh'].std()
        }
        
        print("\n=== Energy Consumption Statistics ===")
        for key, value in stats.items():
            print(f"{key}: {value:.2f}")
        
        return stats
    
    def hourly_pattern_analysis(self):
        """Analyze consumption patterns by hour of day"""
        hourly_avg = self.df.groupby('hour')['consumption_kwh'].mean()
        
        plt.figure(figsize=(14, 6))
        plt.plot(hourly_avg.index, hourly_avg.values, marker='o', linewidth=2)
        plt.title('Average Energy Consumption by Hour of Day', fontsize=16, fontweight='bold')
        plt.xlabel('Hour of Day', fontsize=12)
        plt.ylabel('Average Consumption (kWh)', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.xticks(range(0, 24))
        plt.tight_layout()
        plt.savefig('hourly_consumption_pattern.png', dpi=300, bbox_inches='tight')
        print("\nHourly pattern plot saved as 'hourly_consumption_pattern.png'")
        plt.close()
        
        return hourly_avg
    
    def monthly_trends(self):
        """Analyze monthly consumption trends"""
        monthly_consumption = self.df.groupby('month')['consumption_kwh'].sum()
        
        plt.figure(figsize=(14, 6))
        plt.bar(monthly_consumption.index, monthly_consumption.values, color='steelblue', alpha=0.7)
        plt.title('Total Energy Consumption by Month', fontsize=16, fontweight='bold')
        plt.xlabel('Month', fontsize=12)
        plt.ylabel('Total Consumption (kWh)', fontsize=12)
        plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.savefig('monthly_consumption.png', dpi=300, bbox_inches='tight')
        print("Monthly trend plot saved as 'monthly_consumption.png'")
        plt.close()
        
        return monthly_consumption
    
    def weekday_weekend_comparison(self):
        """Compare weekday vs weekend consumption"""
        self.df['is_weekend'] = self.df['day_of_week'].isin([5, 6])
        comparison = self.df.groupby('is_weekend')['consumption_kwh'].mean()
        
        plt.figure(figsize=(10, 6))
        labels = ['Weekday', 'Weekend']
        values = [comparison[False], comparison[True]]
        colors = ['#3498db', '#e74c3c']
        
        plt.bar(labels, values, color=colors, alpha=0.7)
        plt.title('Average Energy Consumption: Weekday vs Weekend', fontsize=16, fontweight='bold')
        plt.ylabel('Average Consumption (kWh)', fontsize=12)
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.savefig('weekday_weekend_comparison.png', dpi=300, bbox_inches='tight')
        print("Weekday/Weekend comparison saved as 'weekday_weekend_comparison.png'")
        plt.close()
        
        return comparison
    
    def temperature_correlation(self):
        """Analyze correlation between temperature and consumption"""
        if 'temperature_c' not in self.df.columns:
            print("Temperature data not available")
            return None
        
        correlation = self.df['consumption_kwh'].corr(self.df['temperature_c'])
        
        plt.figure(figsize=(12, 6))
        plt.scatter(self.df['temperature_c'], self.df['consumption_kwh'], 
                   alpha=0.3, s=10, color='steelblue')
        plt.title(f'Energy Consumption vs Temperature (Correlation: {correlation:.2f})',
                 fontsize=16, fontweight='bold')
        plt.xlabel('Temperature (°C)', fontsize=12)
        plt.ylabel('Consumption (kWh)', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('temperature_correlation.png', dpi=300, bbox_inches='tight')
        print(f"Temperature correlation plot saved (r={correlation:.2f})")
        plt.close()
        
        return correlation
    
    def run_full_analysis(self):
        """Run complete energy consumption analysis"""
        print("\n" + "="*60)
        print("   ENERGY CONSUMPTION ANALYSIS REPORT")
        print("="*60)
        
        if self.df is None:
            print("\nNo data found. Generating sample data...")
            self.generate_sample_data()
        
        # Run all analyses
        self.basic_statistics()
        self.hourly_pattern_analysis()
        self.monthly_trends()
        self.weekday_weekend_comparison()
        self.temperature_correlation()
        
        print("\n" + "="*60)
        print("   Analysis complete! Check output files for visualizations.")
        print("="*60 + "\n")


if __name__ == "__main__":
    # Initialize analyzer
    analyzer = EnergyAnalyzer('data/energy_data.csv')
    
    # Try to load data, if not available, generate sample data
    data = analyzer.load_data()
    if data is None:
        print("Using sample data for demonstration...")
        analyzer.generate_sample_data(days=365)
    
    # Run full analysis
    analyzer.run_full_analysis()
