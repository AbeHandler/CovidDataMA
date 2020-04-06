library(readr)
library(tidyr)
library(dplyr)
options(digits=3)
d=read_csv("plotting/latest.csv")
x = d %>% filter(state=='Massachusetts' & county %in% c("Hampshire","Hampden","Berkshire","Franklin")) %>% select(date,county,cases) %>% arrange(-as.integer(date)) %>% group_by(county) %>% summarise(now=date[1],now_cases=cases[1], lastweek=date[8], lastweek_cases=cases[8], weekly_growth=now_cases/lastweek_cases, daily_growth=weekly_growth^(1/7),doubling_time=log(2)/log(daily_growth))

y=data.frame(1,1,1,1); names(y)=x$county
y[1,] = sprintf("%d",x$now_cases)
row.names(y)[1] = sprintf("Current   (%s)", x$now[1])
y[2,] = sprintf("%d",x$lastweek_cases)
row.names(y)[2] = sprintf("Prev week (%s)", x$lastweek[1])
y[3,] = sapply(x$weekly_growth, function(x) if (x > 1.5) sprintf("%.1f",x) else sprintf("%.2f",x))
row.names(y)[3] = "7-day growth rate"

print(y)
