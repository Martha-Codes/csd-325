"""
Sitka Weather Program
Modified by Martha Guzman

Changes:
1. Added a menu for Highs, Lows, or Exit.
2. Added low temperature graph (blue).
3. Program loops until Exit is selected.
4. Added exit message.
"""

import csv
import sys
from datetime import datetime

from matplotlib import pyplot as plt


while True:

    print("\n===== Sitka Weather Menu =====")
    print("1. Highs")
    print("2. Lows")
    print("3. Exit")

    choice = input("MG: ").lower()

    if choice == "3" or choice == "exit":
        print("Thank you for using the Sitka Weather Program!")
        sys.exit()

    filename = 'sitka_weather_2018_simple.csv'

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dates = []
        temps = []

        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)

            if choice == "1" or choice == "highs":
                temps.append(int(row[5]))

            elif choice == "2" or choice == "lows":
                temps.append(int(row[6]))

            else:
                print("Invalid choice. Please select Highs, Lows, or Exit.")
                break

        else:

            fig, ax = plt.subplots()

            if choice == "1" or choice == "highs":
                ax.plot(dates, temps, c="red")
                plt.title("Daily High Temperatures - 2018", fontsize=24)

            else:
                ax.plot(dates, temps, c="blue")
                plt.title("Daily Low Temperatures - 2018", fontsize=24)

            plt.xlabel("", fontsize=16)
            fig.autofmt_xdate()
            plt.ylabel("Temperature (F)", fontsize=16)
            plt.tick_params(axis='both', which='major', labelsize=16)

            plt.show()