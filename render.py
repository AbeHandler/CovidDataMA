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

with open("plotting/table.csv", "r") as inf:
    reader = csv.reader(inf)
    next(reader)
    for rno, r in enumerate(reader):
        if(rno == 0):
            # ['Current   (2020-04-03)', '240', '89', '661', '114']
            y, m, d = r[0].split()[1].replace("(", "").replace(")", "").split("-")
            dt = datetime(int(y), int(m), int(d)).strftime("%b %e")
            txt = txt.replace('CURRENT', "Latest counts (" + dt + ")")
            berkshire, franklin, hampden, hampshire = r[1], r[2], r[3], r[4]
            txt = txt.replace('CA', berkshire)
            txt = txt.replace('CB', franklin)
            txt = txt.replace('CC', hampden)
            txt = txt.replace('CD', hampshire)

        if(rno == 1):
            # ['Prev week (2020-03-29)', '151', '41', '201', '37']
            y, m, d = r[0].split()[2].replace("(", "").replace(")", "").split("-")
            dt = datetime(int(y), int(m), int(d)).strftime("%b %e")
            txt = txt.replace('PREV', "Last week counts (" + dt + ")")
            berkshire, franklin, hampden, hampshire = r[1], r[2], r[3], r[4]
            txt = txt.replace('PA', berkshire)
            txt = txt.replace('PB', franklin)
            txt = txt.replace('PC', hampden)
            txt = txt.replace('PD', hampshire)

        if(rno == 2):
            # ['Current   (2020-04-03)', '240', '89', '661', '114']
            berkshire, franklin, hampden, hampshire = r[1], r[2], r[3], r[4]
            txt = txt.replace('7A', berkshire + "x")
            txt = txt.replace('7B', franklin + "x")
            txt = txt.replace('7C', hampden + "x")
            txt = txt.replace('7D', hampshire + "x")


with open("site/index.html", "w") as of:
    of.write(txt)
