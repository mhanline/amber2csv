Amber2csv

Calls the Amber API to request and manipulate the general and feed-in rates.

Used in conjunction with cron. Recommended settings are as follows:

Every 5 minutes: Requests the estimated rate
Every 6 minutes: Requests the actual rate

main.py

This Python script calls the Amber Electric API and requests the current feed-in and general price, and records whether it's an estimate or actual. It then appends it to a CSV file.

merge.py

This script takes the generated CSV files as inputs, and generates new CSV files with the estimate and actual values for the 5-minute period on the same line.
