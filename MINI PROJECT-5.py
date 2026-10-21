"""
RECORD CHECK  -  my version
===========================

Name  : Bushra Mateen
Lane  : Cyber 
Date  : 21/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


class Record:
    def __init__(self, source_ip, failed_logins, total_attempts):
        """Initialize a record with its IP, failed logins and total attempts."""
        self.source_ip = source_ip
        self.failed_logins = int(failed_logins)
        self.total_attempts = int(total_attempts)

    def status(self):
        """Return the status based on the failed login percentage."""
        percentage = (self.failed_logins / self.total_attempts) * 100

        if percentage >= 100:
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"


def load_records(path):
    """Read records from a file and return Record objects."""
    records_list = []

    with open(path, "r") as file:
        for line in file:
            line = line.strip()

            if line:
                source_ip, failed, total = line.split(",")

                records_list.append(Record(source_ip.strip(),failed.strip(),total.strip()))

    return records_list


records = load_records("records.txt")

overlimit_count = 0

for record in records:
    current_status = record.status()

    if current_status == "OVER LIMIT":
        overlimit_count += 1

    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.source_ip}")
    print("=" * 34)
    print(f"Source IP:           {record.source_ip}")
    print(f"Failed Logins:       {record.failed_logins}")
    print(f"Total Attempts:      {record.total_attempts}")
    print(f"Status:              {current_status}")
    print("=" * 34)

print(f"\nTotal records OVER LIMIT: {overlimit_count}")