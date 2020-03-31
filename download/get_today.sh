#!/usr/bin/env bash

wget https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv -O plotting/latest.csv

head -1 plotting/latest.csv > plotting/valley.csv

grep -f download/counties.txt plotting/latest.csv | grep Mass >> plotting/valley.csv

Rscript plotting/plot.R

mv plotting/valley.png site/

aws cloudfront create-invalidation --distribution-id E2RT6I870YM5PU --paths "/*"
