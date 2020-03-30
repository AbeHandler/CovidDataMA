wget https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv -O latest.csv

grep -f counties.txt latest.csv | grep Mass
