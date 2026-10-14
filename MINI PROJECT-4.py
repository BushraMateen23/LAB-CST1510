"""
RECORD CHECK  -  my version
===========================

Name  : Bushra Mateen
Lane  : Cyber
Date  : 14/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


def load_records(path):
    """Load records from a file."""
    records = []

    with open(path, "r") as file:
        for line in file:
            ip, failed, total = line.strip().split(",")

            records.append({
                "source_ip": ip,
                "failed_logins": int(failed),
                "total_attempts": int(total)
            })

    return records


def check_record(record):
    """Check the failed login percentage."""
    percentage = record["failed_logins"] / record["total_attempts"] * 100

    if percentage > 20:
        return "OVER LIMIT"
    elif percentage >= 10:
        return "WARNING"
    else:
        return "OK"


def print_report(record, status):
    """Print a formatted report."""
    percentage = record["failed_logins"] / record["total_attempts"] * 100

    print(
        f"{record['source_ip']:<16}"
        f"{record['failed_logins']:>5}/"
        f"{record['total_attempts']:<6}"
        f"{percentage:>7.1f}%   "
        f"{status}"
    )


def save_results(path, results):
    """Save results to a file."""
    with open(path, "w") as file:
        for ip, status in results:
            file.write(f"{ip},{status}\n")


try:
    records = load_records(
        "/Users/bushramateen/Downloads/Week 04 - Lists, Dictionaries and Files/LAB/cyber_records.txt"
    )
except FileNotFoundError:
    print("Error: cyber_records.txt was not found.")
    records = []


results = []
over_limit_count = 0

print("\nCYBER SECURITY LOGIN REPORT")
print("-" * 55)
print(f"{'SOURCE IP':<16}{'FAILED/TOTAL':<15}{'RATE':<10}STATUS")
print("-" * 55)

for record in records:
    status = check_record(record)
    print_report(record, status)

    results.append((record["source_ip"], status))

    if status == "OVER LIMIT":
        over_limit_count += 1

save_results(
    "/Users/bushramateen/Downloads/Week 04 - Lists, Dictionaries and Files/LAB/cyber_results.txt",
    results
)

print("-" * 55)
print("Total OVER LIMIT records:", over_limit_count)
print("Results saved successfully.")
