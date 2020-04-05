from datetime import datetime
from collections import defaultdict
import csv
import json

txt = open("package/templates/index.html", 'r').read()


def todt(x):
    y, m, d = x.split("-")
    return datetime(int(y), int(m), int(d))


with open("plotting/valley.csv", "r") as inf:
    reader = csv.reader(inf)
    head = next(reader)
    dates = set()
    county2data = defaultdict(list)
    for i in reader:
        date, county, state, fips, cases, deaths = i
        dates.add(date)
        county2data[county].append({"date": todt(date), "cases": cases})


dates = list(dates)

dates.sort(key=lambda x: todt(x))


def get_data(date, cases):
    date = todt(date)
    try:
        d = [o["cases"] for o in cases if o["date"] == date][0]
    except IndexError:
        d = 0
    return d


for c in county2data:
    data = county2data[c]
    data.sort(key=lambda x: x["date"])
    county2data[c] = [c] + [get_data(date, data) for date in dates]
    print(county2data[c])

x = datetime.now().strftime("%b %-d, %Y at %I:%M %p")

dates = ['x'] + dates

txt = txt.replace("NOW", x).replace("DATES", json.dumps(dates))

for c in county2data:
    txt = txt.replace(c.upper(), json.dumps(county2data[c]))

with open("site/index.html", "w") as of:
    of.write(txt)
