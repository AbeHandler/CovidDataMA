library(tidyverse)

valley <- read_csv("plotting/changes.csv")

# seven day avg of new confirmed cases

valley$county <- factor(valley$county, levels = c("Berkshire", "Hampden", "Franklin", "Hampshire"))

ggplot(valley) + geom_line(aes(x=date, y=avg, color=county), size = 1.5) + scale_color_manual(values = c("#1f77b4", "#FF7F0E", "#2CA02C", "#d62728")) + xlab("day") + ylab("Average new confirmed cases (over past 7 days)") +  ggtitle("Average new confirmed cases by county") + theme_light()

ggsave("site/changes.png")
