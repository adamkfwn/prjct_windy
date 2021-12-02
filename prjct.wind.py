import csv

with open("WindData.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    header = next(reader)
    for row in reader:
        timestamp = row[0]
        wind_direction = row[1]
        wind_speed = row[2]
        print(timestamp, wind_direction, wind_speed)