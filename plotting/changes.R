library(tidyverse)

valley <- read_csv("plotting/changes.csv")

# seven day avg of new confirmed cases

ggplot(valley) + geom_line(aes(x=date, y=avg, color=county), size = 1.5) + xlab("day") + ylab("Average new confirmed cases") +  ggtitle("Average new confirmed COVID cases (over past 7 days)") + theme_light()

ggsave("plotting/changes.png")
