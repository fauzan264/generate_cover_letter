import csv
import random

dir = "./data/"
def load_file():
    csv_file = "input.csv"
    
    with open(dir+csv_file, "r") as file:
        csv_reader = csv.DictReader(file)
        rows = [row['template'] for row in csv_reader]
        return random.choice(rows)
    
# save to template/output.csv
def save_file(description):
    txt_file = "output.txt"

    with open(dir+txt_file, "w", newline="") as file:
        file.write(description)
        print("OK")