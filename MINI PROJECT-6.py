"""
RECORD CHECK  -  my version
===========================

Name  : Bushra Mateen
Lane  : Cyber 
Date  : 4/11/2026

Run it:   python template.py

"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cyber_records.csv")   


df["percent"] = (df["failed_logins"] / df["total_attempts"]) * 100


df["status"] = df["percent"].apply(
    lambda x: "OVER LIMIT" if x >= 100
    else "WARNING" if x >= 90
    else "OK"
)


print("FULL DATAFRAME:")
print(df)


#displays only those rows that are not OK
print("\nRECORDS NEEDING ATTENTION:")
print(df[df["status"] != "OK"])


print("\nSTATUS COUNTS:")
counts = df.groupby("status").size()
print(counts)


df.to_csv("cyber_records_checked.csv", index=False)


counts.plot(kind="bar", title="Cyber Security Record Status")
plt.xlabel("Status")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.savefig("cyber_status_chart.png")

print("\nCSV and chart saved successfully.")
