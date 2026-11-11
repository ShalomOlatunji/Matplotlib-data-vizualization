This is my Module 3 assignment using Matplotlib and Seaborn to explore monthly airline passenger numbers.

I used Seaborn's public flights dataset, covering 1949–1960. Passenger totals are measured in thousands.
Charts
- [Line plot](line_plot.png): monthly passenger totals in 1960.
- [Scatter plot](scatter_plot.png): monthly passenger totals across all years.
- [Histogram](histogram.png): how often different passenger-count ranges occur.
- [Box plots](box_plot.png): the median and spread of monthly counts for each year.
Passenger numbers generally increased over the years, with greater variation between months in later years. July had the highest passenger count in 1960.
How to run
Open a terminal in the project folder and run:
python -m pip install matplotlib seaborn
python matplotlib_assignment.py
The first run needs internet to download the dataset. Close each graph window to see the next one. The script also saves all four graphs as PNG images.
