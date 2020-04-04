#!/usr/bin/env bash

set -e

source /home/ahandler/miniconda3/etc/profile.d/conda.sh
conda activate covid

wget https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv -O plotting/latest.csv

head -1 plotting/latest.csv > plotting/valley.csv

grep -f download/counties.txt plotting/latest.csv | grep Mass >> plotting/valley.csv

/usr/bin/Rscript plotting/plot.R

mv plotting/valley.png site/

python render.py

/home/ahandler/bin/aws cloudfront create-invalidation --distribution-id E2RT6I870YM5PU --paths "/*"

/home/ahandler/bin/aws s3 cp site/valley.png s3://www.wmasscovid.com/valley.png --acl public-read

/home/ahandler/bin/aws s3 cp site/index.html s3://www.wmasscovid.com/index.html --acl public-read
