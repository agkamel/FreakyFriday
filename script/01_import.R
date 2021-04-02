# Importing dataset

# This script imports, cleans and exports data

# Packages
library(readr)
library(dplyr)
library(lubridate)
library(ggplot2)

# Functions
# s/o

# Settings
# a. Directory where to save datasets
data_dir <- "data"
# b. Path to save datasets
data_path <- "data/activity.csv"

# 1 Importing data
my_data <- read_rds(data_path)

# 2 Generating graph

# TO BE CONTINUED...

#my_data %>% arrange(button_pushed)
#  

#  filter(
#  month(button_pushed) == 3
#)


#ggplot(my_data) +
#  geom_col(mapping = aes(x = ms(button_pushed), y = ))
