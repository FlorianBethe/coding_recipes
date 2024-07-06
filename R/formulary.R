################################################################################
#  R - formulary                                                               #
#                                                                              #
# Growing collection of formulas and code snippets.                            #
#                                                                              #
#  @date:   03.07.2024                                                         #
#  @author: Florian Bethe                                                      #
################################################################################


################################################################################
# General basics                                                               #
################################################################################

# clear workspace
rm(list = ls())


# clear console
cat("\014")


# set working directory
setwd("C:\\Users\\")



################################################################################
# Packages                                                                     #
################################################################################

# check if library readxl is installed
"readxl" %in% installed.packages()

# check if library readxl is loaded
"readxl" %in% loadedNamespaces()

# install package readxml if not already installed using installed.packages()
if (!"readxl" %in% installed.packages())
  install.packages("readxl")

# load library readxml if not already loaded
if (!"readxl" %in% loadedNamespaces())
  library(readxl)

# install package readxml if not already installed using require()
# require() trys to load the library and returns false if not successfull
if (!require(readxl)) {
  install.packages("readxl")
  library(readxl)
}

# Bibliothek reshape2 laden, ggf. installieren
if (!require(reshape2)) {
  install.packages("reshape2")
  library(reshape2)
}

# detach a library
detach("package:readxl", unload=TRUE)


# Importiert das gesamte dplyr-Paket unter einem Alias-Namen
dplyr = import_package('dplyr')

# Verwendet die filter-Funktion aus dem importierten dplyr-Paket
cars %>% dplyr$filter(speed > 15)



# Verwendet die select-Funktion aus dem dplyr-Paket
dplyr::select(data, column_name)



# Das import-Paket bietet eine weitere Möglichkeit, spezifische Funktionen aus anderen Paketen zu importieren. Mit import::from() können Sie Funktionen aus einem Paket importieren und ihnen sogar neue Namen geben, falls gewünscht.
# !  Es ist wichtig zu beachten, dass das Laden spezifischer Teile eines Pakets oder das Importieren einzelner Funktionen sorgfältig durchgeführt werden sollte, um sicherzustellen, dass alle Abhängigkeiten korrekt behandelt werden und keine unerwarteten Nebenwirkungen auftreten. Die direkte Verwendung von Funktionen mit der Doppelpunkt-Notation ist oft die einfachste und sicherste Methode, um spezifische Funktionen aus einem Paket zu nutzen, ohne das gesamte Paket laden zu müssen.
import::from(dplyr, select, filter)

# Nun können Sie select und filter direkt aufrufen, ohne dplyr:: voranzustellen
select(data, column_name)
filter(data, condition)


# read spotify datasets from workingspaces subfolder "data"
spotify1 <- read_excel("data\\Spotify music_data1.xlsx")



################################################################################
# Poweranalysis                                                                #
################################################################################

### pwr
if (!require(pwr)) {
  install.packages("pwr")
  library(pwr)
}

# Poweranalysis for a t-test
pwr.t.test(d = 0.5, sig.level = 0.05, power = 0.8, type = "two.sample")

## further analyses
# ANOVA:
pwr.anova.test()
# Korrelation:
pwr.r.test()
# Chi-Quadrat-Test: 
pwr.chisq.test()
# Z-Test: 
pwr.2p.test()


### WebPower
if (!require(WebPower)) install.packages("WebPower")

## Poweranalyse für einen t-Test
wp.t(d = 0.5, power = 0.8, alpha = 0.05)

## weitere Funktionen
#ANOVA: 
wp.anova()
#Korrelation: 
wp.correlation()
#Regression: 
wp.regression()



### simr Paket
library(lme4)
library(simr)

# Einfache gemischte Modell
model <- lmer(y ~ x + (1|group), data = mydata)

# Poweranalyse
powerSim(model, nsim = 100)


###############################
# standard data sets

## mtcars

data(mtcars)

mtcars$am[mtcars$am == "0"] <- "aut"
mtcars$am[mtcars$am == "1"] <- "man"

mtcars$vs[mtcars$vs == "0"] <- "Inline-Zylinder"
mtcars$vs[mtcars$vs == "1"] <- "V-förmige Zylinder"

# Zurücksetzen des Faktors
airquality$Month <- as.factor(airquality$Month)

# Neues Definieren der Levels
airquality$Month[which(airquality$Month ==  "1")] <- "01 Januar"
airquality$Month[which(airquality$Month ==  "2")] <- "02 Februar"
airquality$Month[which(airquality$Month ==  "3")] <- "03 März"
airquality$Month[which(airquality$Month ==  "4")] <- "04 April"
airquality$Month[which(airquality$Month ==  "5")] <- "05 Mai"
airquality$Month[which(airquality$Month ==  "6")] <- "06 Juni"
airquality$Month[which(airquality$Month ==  "7")] <- "07 Juli"
airquality$Month[which(airquality$Month ==  "8")] <- "08 August"
airquality$Month[which(airquality$Month ==  "9")] <- "09 September"
airquality$Month[which(airquality$Month == "10")] <- "10 Oktober"
airquality$Month[which(airquality$Month == "11")] <- "11 November"
airquality$Month[which(airquality$Month == "12")] <- "12 Dezember"

levels(airquality$Month) <- c("Januar", "Februar", "März", "April", "Mai", "Juni", 
                              "Juli", "August", "September", "Oktober", "November", "Dezember")

levels(airquality$Month) <- c("Mai", "Juni", "Juli", "August", "September")

# Ändern des spezifischen Wertes
airquality$Month[which(airquality$Month == "12")] <- "12 Dezember"

# Überprüfen der aktualisierten Werte
unique(airquality$Month)


## diamonds (ggplot2)
if (!require(ggplot2)) {
  install.packages("ggplot2")
  library(ggplot2)
}
data(diamonds)


## msleep (ggplot2)
# Data: Mammals Sleep
# https://seandavi.github.io/ITR/dplyr_intro_msleep.html#Data:_Mammals_Sleep
data(msleep)

## UCBAdmissions

# load standard data set
data("UCBAdmissions")


View(UCBAdmissions)
str(UCBAdmissions)
summary(UCBAdmissions)
head(UCBAdmissions)


## HairEyeColor
data("HairEyeColor")


## Fehlende Werte auschließen
airquality_clean <- na.omit(airquality[, c("Temp", "Ozone", "Month")])


###################################
# Kreuztabellen
#
# Die Kreuztabelle zeigt die Häufigkeiten des gemeinsamen Auftretens der Ausprägungen von Getriebeart und Zylinderanzahl. Hierbei haben wir zwei mögliche Getriebearten (0 = Automatik, 1 = Manuell) und drei mögliche Zylinderanzahlen (4, 6 und 8).

# table()
table(mtcars$am, mtcars$cyl)


# xtabs()
xtabs(~ mtcars$am + mtcars$cyl)


# gmodels::CrossTable()
if (!require(gmodels)) {
  install.packages("gmodels")
  library(gmodels)
}

gmodels::CrossTable(
  mtcars$am,
  mtcars$cyl,
  prop.c = FALSE,
  prop.r = FALSE,
  prop.t = FALSE,
  expected=TRUE,
  fisher=TRUE) 



##################################
# Pearson-Korrelation
#
# Die Pearson-Korrelation misst den linearen Zusammenhang zwischen zwei intervallskalierten Variablen. In diesem Fall analysieren wir den Zusammenhang zwischen "mpg" und "hp". Der Korrelationskoeffizient variiert zwischen -1 und 1, wobei Werte nahe 0 auf einen schwachen Zusammenhang hindeuten, negative Werte auf eine negative Korrelation (wenn eine Variable steigt, sinkt die andere) und positive Werte auf eine positive Korrelation (beide Variablen steigen oder sinken gemeinsam) hinweisen.

cor(airquality[, c("Solar.R", "Temp", "Wind", "Ozone")])

cor(mtcars$mpg, mtcars$hp, method = "pearson")

cor.test(mtcars$mpg, mtcars$hp)





####################################
# Diagramme

## Streudiagramm

plot(airquality$Solar.R, airquality$Temp)

plot(
  airquality$Solar.R,
  airquality$Temp,

  xlab  = "Sonneneinstrahlungszeit",
  ylab  = "Temperatur", 

  main  = "Streudiagramm",
  pch   = 21,
  cex   = 2,
  bg    = "steelblue",
  color = "black")

## Histogramm

ggplot(
  data = diamonds,
  aes(
    x = price,
    y = ..density..)) +
  
  geom_histogram(
    binwidth = 500,
    fill = "steelblue",
    color = "white") +
  
  geom_density(
    size = 1, 
    color = "red") +
  
  labs(
    x = "Preis",
    y = "Dichte") +
  
  ggtitle("Histogramm der Diamantenpreise mit Dichtefunktion") +
  
  theme(
    plot.title = element_text(
      hjust = 0.5))


## Säulendiagramm

admissions_table <- as.data.frame.table(UCBAdmissions)

if (!require(ggplot2)) {
  install.packages("ggplot2")
  library(ggplot2)
}

ggplot(
  data = admissions_table,
  aes(
    x     = Dept,
    y     = Freq,
    fill  = Admit,
    group = Gender)) +
  
  geom_bar(
    stat     = "identity",
    position = "dodge") +
  
  facet_grid(. ~ Gender)

  labs(
    x = "Department",
    y = "Number of Applicants",
    title = "UCB Admissions by Department and Gender") +
  
  theme(
    plot.title = element_text(hjust = 0.5)) +
  
  scale_fill_manual(
    values = c("red", "blue"),
    labels = c("Rejected", "Admitted"))


  
# (A) Gestapelte Säulen – Farben werden je Geschlecht gestapelt
barplot(
  table(
    data$Lieblingsfarbe,
    data$Geschlecht),
  col = c("blue", "yellow", "green", "red", "black"))

# (B) Gestapelte Säulen – Je Farbe werden die Anzahl der Geschlechtsausprägungen
#     gestapelt
barplot(
  table(
    data$Geschlecht,
    data$Lieblingsfarbe),
  col = c("darkblue", "darkred"))

# (C) Gruppierte Säulen – Je Geschlecht hat jede Farbe eine Säule
barplot(
  table(
    data$Lieblingsfarbe,
    data$Geschlecht),
  beside = TRUE,
  col = c("blue", "yellow", "green", "red", "black"))

# (D) Gruppierte Säulen – Je Farbe werden die Anzahl der 
#     Geschlechtsausprägungen in einer separaten Säule abgetragen
barplot(
  table(
    data$Geschlecht,
    data$Lieblingsfarbe),
  beside = TRUE,
  col = c("darkblue", "darkred"))



## Balkendiagramm
# Basisversion von R
barplot(
  table(data$Lieblingsfarbe), 
  xlab = "Häufigkeit",
  ylab = "Farben", 
  main = "Lieblingsfarben", 
  horiz = TRUE)

# ggplot2
ggplot(
  data = ozone_average_by_month,
  aes(
    x = Month,
    y = Ozone)) +
  
  geom_bar(
    stat = "identity",
    fill = "steelblue") +
  
  coord_flip() +
  
  labs(
    title = "Durchschnittliche Ozonkonzentration nach Monat",
    x     = "Monat",
    y     = "Durchschnittliche Ozonkonzentration (ppb)")


## Boxplot

ggplot(
  data = airquality,
  aes(
    x = factor(Month),
    y = Temp)) +
  
  stat_boxplot(
    geom   = "errorbar",
    width  = 0.25,
    colour = "blue") +
  
  geom_boxplot(
    outlier.color = "red",
    notch = TRUE) +
  
  #  geom_boxplot(
  #    outlier.color = "red") +
  
  geom_jitter(size = 1) +
  
  labs(
    title = "Boxplot der Temperatur nach Monat",
    x     = "Monat",
    y     = "Temperatur [°F]") 
