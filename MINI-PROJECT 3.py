"""
RECORD CHECK  -  my version
===========================

Name  : Bushra Mateen
Lane  : Cyber 
Date  : 7/10/2026

Run it:   python template.py


"""

def status_of(percent):
    if percent>=100:
        return "OVER LIMIT"
    elif percent>=90:
        return "WARNING"
    else:
        return "OK"

def check(value,limit):
    difference=value-limit
    percent=(value/limit)*100
    return difference, percent

def print_report(label, value, limit, difference,percent, status):
    print("="*34)
    print(f"RECORD CHECK - {label}")
    print("="*34)
    print(f"Failed logins: {value:>9.2f}")
    print(f"Total attempts: {limit:>8.2f}")
    print(f"Remaining: {difference:>13.2f}")
    print(f"Percent : {percent:>14.2f} %")
    print(f"Status: {status:>15}")
    print("="*34)


overlimit_count=0

while True:
    label = input("Enter the source IP: (or enter 'quit' to stop) ") 
    if label=='quit':
        break

    value = float(input("Enter failed logins: "))     
    limit = float(input("Enter total attempts: "))    

     

    diff,per= check(value,limit)
    status = status_of(per)         

    if status=='OVER LIMIT':
        overlimit_count+=1



    print_report(label, value, limit, diff,per, status)

print(f"\nTotal OVER LIMIT count: {overlimit_count}")

