import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", index_col=0, parse_dates=True)

    # Create scatter plot
    fig, ax = plt.subplots()
    years = [dt.year for dt in df.index]
    sea_levels = df['CSIRO Adjusted Sea Level']
    plt.scatter(x=years, y=sea_levels)

    # Create first line of best fit
    line = linregress(years, sea_levels)
    year_range = range(min(years), 2050 + 1)
    ax.plot(year_range, [line.slope * x + line.intercept for x in year_range], 'g')

    # Create second line of best fit
    line_2 = linregress(years[years.index(2000):], sea_levels[years.index(2000):])
    year_range_2 = range(2000, 2050 + 1)
    ax.plot(year_range_2, [line_2.slope * x + line_2.intercept for x in year_range_2], 'y')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()