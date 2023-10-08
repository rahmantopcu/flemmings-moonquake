import csv
import json

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 30]
lmonth_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 30]
dictionary = dict({})

headers = []
rows = []

years = []
months = []
days = []
daysu = []
hours = []
mins = []
secs = []
lats = []
longs = []
magns = []

with open("unprocessed\\nakamura_1979_sm_locations.csv", 'r') as csvfile1:
    csvreader1 = csv.reader(csvfile1)
    headers = next(csvreader1)

    for row in csvreader1:
        year = int(row[0])
        day = int(row[1])
        hour = int(row[2])
        min = int(row[3])
        sec = int(row[4])
        lat = int(row[5])
        long = int(row[6])
        magn = float(row[7])

        dayp = day

        if year % 4 == 0:
            for month_num, i in enumerate(lmonth_days):
                if dayp>i:
                    dayp = dayp-i
                else:
                    month = month_num+1
                    break
        else: 
            for month_num, i in enumerate(month_days):
                if dayp>i:
                    dayp = dayp-i
                else:
                    month = month_num+1
                    break

        years.append(year)
        months.append(month)
        daysu.append(day)
        days.append(dayp)
        hours.append(hour)
        mins.append(min)
        secs.append(sec)
        longs.append(360+long if long<0 else long)
        lats.append(180+lat if lat<0 else lat)
        magns.append(magn)


dictionary["Years"] = years
dictionary["Months"] = months
dictionary["Days"] = days
dictionary["Hours"] = hours
dictionary["Minutes"] = mins
dictionary["Seconds"] = secs
dictionary["Longitudes"] = longs
dictionary["Latitudes"] = lats
dictionary["Magnitudes"] = magns

print(json.dumps(dictionary))