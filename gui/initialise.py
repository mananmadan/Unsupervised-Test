import csv 
with open('Record.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["UName", "Log Time"])