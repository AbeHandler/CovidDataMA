'''compute changes of past 7 days and write to csv'''

import csv
from datetime import datetime
from collections import defaultdict


def todt(x):
    y, m, d = x.split("-")
    return datetime(int(y), int(m), int(d))


def within_previous_days(a, b, K):
    '''true if a is within K prior days of b, including K'''
    if a < b:
        if (b - a).days <= K:
            return True
    return False


def last_K_datapoints(some_data, some_date, K):
    return [d for d in some_data if within_previous_days(d['date'], some_date, K)]


def mean_of_group(ou):
    '''get the mean number of cases for a group'''
    n = sum([i["new_cases"] for i in ou])
    d = len(ou)
    if len(ou) == 0:
        return 0
    return n/d


if __name__ == "__main__":

    with open("plotting/valley.csv", "r") as inf:
        reader = csv.reader(inf)
        head = next(reader)
        dates = set()
        county2data = defaultdict(list)
        for i in reader:
            date, county, state, fips, cases, deaths = i
            dates.add(date)
            county2data[county].append({"date": todt(date), "cases": cases})

    with open("plotting/changes.csv", "w") as of:
        writer = csv.writer(of)

        for c in county2data:
            some_data = county2data[c]
            some_data.sort(key=lambda x: x["date"])

            for itm in some_data[10:]:

                dt = itm["date"]

                a = last_K_datapoints(some_data=some_data, some_date=dt, K=7)

                for this_day in a:
                    prev_day = last_K_datapoints(some_data=some_data, some_date=this_day["date"], K=1)[0]
                    this_day["new_cases"] = int(this_day["cases"]) - int(prev_day["cases"])

                writer.writerow([dt.strftime("%Y-%m-%d"), c, mean_of_group(a)])