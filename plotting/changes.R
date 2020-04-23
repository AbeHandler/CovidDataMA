library(tidyverse)

valley <- read_csv("plotting/changes.csv")

ggplot(valley) + geom_line(aes(x=date, y=avg, color=county), size = 1.5) + ggtitle("7-day average, New confirmed COVID-19 cases by county, Western MA") + theme_light()

ggsave("plotting/changes.png")
