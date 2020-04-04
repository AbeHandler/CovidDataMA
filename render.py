from datetime import datetime
from collections import defaultdict
import csv

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

dates = ['x'] + dates

print(dates)

for c in county2data:
    data = county2data[c]
    data.sort(key=lambda x: x["date"])
    cases = [c] + [o["cases"] for o in data]
    print(cases)

x = datetime.now().strftime("%b %-d, %Y at %I:%M %p")


with open("site/index.html", "w") as of:
    of.write(txt.replace("NOW", x))
