import pandas as panda, statistics, csv

framed_data = panda.read_csv(r"C:\Swarup\WhiteHat Jr\Python\Projects\AveragingData\SOCR-HeightWeight.csv")
mean = statistics.mean(framed_data["Weight(Pounds)"])
mode = statistics.mode(framed_data["Weight(Pounds)"])
median = statistics.median(framed_data["Weight(Pounds)"])

print("--------------------------\n", mean, "\n", "--------------------------\n", median, "\n", "--------------------------\n", mode, "\n")