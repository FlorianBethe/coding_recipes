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
# Arbeitsverzeichnis                                                           #
################################################################################
# Phind: https://www.phind.com/search?cache=qnus6o24izgmdxkd10279vta

getwd()


## Innerhalb von RStudio

# Ändere das Arbeitsverzeichnis auf den Pfad der aktuellen Datei
# - für Quelle und Knit
srcdir <- getSrcDirectory(function(){})[1]
if (srcdir == "") {
  # - für Ausführen
  srcdir <- dirname(rstudioapi::getActiveDocumentContext()$path)
}
setwd(srcdir)
rm(srcdir)

## Ohne RStudio

# Ermittle das Verzeichnis des aktuellen Skripts
script.dir <- dirname(sys.frame(1)$ofile)

# Setze das Arbeitsverzeichnis auf das Verzeichnis des Skripts
setwd(script.dir)


getwd()





################################################################################
# Packages                                                                     #
################################################################################

# check if library readxl is installed
"readxl" %in% installed.packages()

# check if library readxl is loaded
"readxl" %in% loadedNamespaces()


# install multiple packages within one install.packages() method call
install.packages(c("ggplot2", "dplyr"))


# install package readxml if not already installed using installed.packages()
if (!"readxl" %in% installed.packages())
  install.packages("readxl")

# load library readxml if not already loaded
if (!"readxl" %in% loadedNamespaces())
  library(readxl)

# Bibliothek RTools laden, ggf. installieren
if (!require(RTools)) {
  install.packages("RTools")
  library(apaTables)
}

# load library ggplot2 if not already loaded
if (!require(ggplot2)) {
  install.packages("ggplot2")
  library(ggplot2)
}

# load library corrplot if not already loaded
if (!require(corrplot)) {
  install.packages("corrplot")
  library(corrplot)
}

# load library dplyr if not already loaded
if (!require(dplyr)) {
  install.packages("dplyr")
  library(dplyr)
}

# load library tidyr if not already loaded
if (!require(tidyr)) {
  install.packages("tidyr")
  library(tidyr)
}

# install package readxml if not already installed using require()
# require() trys to load the library and returns false if not successfull
if (!require(readxl)) {
  install.packages("readxl")
  library(readxl)
}

# Bibliothek import laden, ggf. installieren
if (!require(import)) {
  install.packages("import")
  library(import)
}

# Bibliothek lme4 laden, ggf. installieren
if (!require(lme4)) {
  install.packages("lme4")
  library(lme4)
}

# Bibliothek simr laden, ggf. installieren
if (!require(simr)) {
  install.packages("simr")
  library(simr)
}

# Bibliothek WebPower laden, ggf. installieren
if (!require(WebPower)) {
  install.packages("WebPower")
  library(WebPower)
}

# Bibliothek datasets laden, ggf. installieren
if (!require(datasets)) {
  install.packages("datasets")
  library(datasets)
}

# Bibliothek apaTables laden, ggf. installieren
if (!require(apaTables)) {
  install.packages("apaTables")
  library(apaTables)
}

# Bibliothek lsr (Companion to "Learning Statistics with R") laden, ggf. installieren
if (!require(lsr)) {
  install.packages("lsr")
  library(lsr)
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
# Bibliothek lme4 laden, ggf. installieren
if (!require(lme4)) {
  install.packages("lme4")
  library(lme4)
}

# Bibliothek simr laden, ggf. installieren
if (!require(simr)) {
  install.packages("simr")
  library(simr)
}

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
if (!require(ggplot2)) {
  install.packages("ggplot2")
  library(ggplot2)
}
data(msleep)


## economics (ggplot2)
if (!require(ggplot2)) {
  install.packages("ggplot2")
  library(ggplot2)
}
data(economics)


## UCBAdmissions

# load standard data set
data("UCBAdmissions")


View(UCBAdmissions)
str(UCBAdmissions)
summary(UCBAdmissions)
head(UCBAdmissions)


## HairEyeColor
data("HairEyeColor")


## CO2
data(CO2)


## UKgas
data(UKgas)


## USAccDeats
data(USAccDeaths)


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


## Kreisdiagramm

data("HairEyeColor")

hair <- as.table(apply(HairEyeColor, c(1), sum))

prozent_hair <- round(prop.table(hair) * 100, 2)

beschriftung_hair <- paste(names(hair), prozent_hair, "%", sep = " ")


#par(mfrow = c(1, 2))

pie(hair, labels = beschriftung_hair, main = "Haarfarben")


## Liniendiagramm

# Liniendiagramm mit einer Variablen unter Verwendung von ggplot2
# load library ggplot2 if not already loaded
if (!require(ggplot2)) {
  install.packages("ggplot2")
  library(ggplot2)
}

ggplot(
  data = arbeit,
  aes(
    x = Datum,
    y = Erwerbstätige..Mio.)) +

  geom_line()


## Liniendiagram mit manuell erstelltem Datensatz
library(ggplot2)

# Beispiel-Datensatz
df <- data.frame(
  Jahr = rep(2020:2023, each = 2),
  Wert = c(3.2, 4.1, 11, 21, 31.1, 53.5, 78.3, 120),
  Person = rep(c("Erika", "Hans"), times = 4)
)

# Liniendiagramm mit angepasster y-Achse
ggplot(df, aes(x = Jahr, y = Wert, color = Person)) +
  geom_line() +
  geom_point() +
  scale_y_continuous(
    labels = scales::comma,  # Zahlenwerte mit Komma formatieren
    breaks = seq(0, 120, by = 20)  # Achsenbeschriftungen in 20er-Schritten
  ) +
  labs(
    title = "Wertentwicklung nach Jahr",
    x = "Jahr",
    y = "Wert"
  )


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






### Power-Analyse

# Alle Zeilen mit fehlenden Daten ausgeben
# Beispiel-Datensatz erstellen
data <- data.frame(
  A = c(1, NA, 3, 4),
  B = c(1, 2, 3, 4),
  C = c(1, 2, NA, 4)
)

# Zeilen mit mindestens einem NA-Wert finden
rows_with_na <- data[rowSums(is.na(data)) > 0, ]

# Zeilen ausgeben
print(rows_with_na)

# OR
nrow(data[rowSums(is.na(data)) > 0, ])
