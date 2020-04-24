library(tidyverse)

valley <- read_csv("plotting/changes.csv")

# seven day avg of new confirmed cases

valley$county <- factor(valley$county, levels = c("Berkshire", "Hampden", "Franklin", "Hampshire"))

ggplot(valley) + geom_line(aes(x=date, y=avg, color=county), size = 1.5) + scale_color_manual(values = c("#1f77b4", "#FF7F0E", "#2CA02C", "#d62728")) + ylab("Average new confirmed cases (over past 7 days)") + xlab("") + theme_minimal() + facet_grid(cols = vars(county)) + theme(strip.background = element_blank(),
   strip.text.x = element_blank())

width = 10
height = (9/16) * width

ggsave("site/changes.png", width = width, height=height)
