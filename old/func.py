#
import csv

a = []
with open(
        "C:\\Users\\zheng\\OneDrive\\Python\\code\\NGAP.csv",
        "r",
        encoding="utf-8") as f:
    line = csv.reader(f)
    # line = line.strip()
    for data in line:
        a = data
print("done")
a[0]
'''
def qu(a, b, c):
    return a + b * c


def t():
    a = int(input("a="))
    b = int(input("b="))
    c = int(input("c="))
    return [a, b, c]


def main():
    arr = t()
    return qu(arr[1], arr[2], arr[3])


a = int(input("a"))
'''
