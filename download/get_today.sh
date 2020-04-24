#!/usr/bin/env bash

set -e

# download the data

wget https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv -O plotting/latest.csv

head -1 plotting/latest.csv > plotting/valley.csv

grep -f download/counties.txt plotting/latest.csv | grep Mass >> plotting/valley.csv

# process the data, make original static plot

/usr/bin/Rscript plotting/plot.R

/usr/bin/Rscript plotting/make_table.r

mv plotting/valley.png site/

# compute the 7 day changes

python compute_changes.py 

/usr/bin/Rscript plotting/changes.R

# render the plot

python render.py

# upload

/home/ahandler/bin/aws cloudfront create-invalidation --distribution-id E2RT6I870YM5PU --paths "/*"

/home/ahandler/bin/aws s3 cp site/valley.png s3://www.wmasscovid.com/valley.png --acl public-read

/home/ahandler/bin/aws s3 cp site/index.html s3://www.wmasscovid.com/index.html --acl public-read

/home/ahandler/bin/aws s3 cp plotting/valley.csv s3://www.wmasscovid.com/wmass.csv --acl public-read

/home/ahandler/bin/aws s3 cp site/changes.png s3://www.wmasscovid.com/wmass.csv --acl public-read

