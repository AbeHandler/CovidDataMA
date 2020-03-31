valley <- read_csv("plotting/valley.csv")

ggplot(valley) + geom_line(aes(x=date, y=cases, color=county), size = 1.5) + scale_y_log10() + ggtitle("Confirmed COVID-19 cases by county, Pioneer Valley (updated daily)") + theme_light()

ggsave("plotting/valley.png")
