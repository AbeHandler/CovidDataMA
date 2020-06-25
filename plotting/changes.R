library(tidyverse)

valley <- read_csv("plotting/changes.csv")

# seven day avg of new confirmed cases

valley$county <- factor(valley$county, levels = c("Berkshire", "Hampden", "Franklin", "Hampshire"))

ggplot(valley) + geom_line(aes(x=date, y=avg, color=county), size = 1.5) + 
scale_color_manual(values = c("#1f77b4", "#FF7F0E", "#2CA02C", "#d62728")) + 
ylab("7-day average") + 
xlab("") + 
theme_minimal() + 
facet_grid(cols = vars(county)) + 
scale_x_date(date_labels=c("%m/%d","%m/%d"), breaks=c(as.Date("2020-05-01"), Sys.Date())) + 
ggtitle('Avg. # new confirmed cases') + 
theme(legend.position = "none", text = element_text(size=10), plot.title = element_text(hjust = 0.5), strip.background = element_blank())

width = 4
height = (9/16) * width

ggsave("site/changes.png", width = width, height=height)
