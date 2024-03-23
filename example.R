(C) Yaacov Kopeliovich and Michael Pokojovy (2024)

setwd("???")

data = read.csv('BOMB.csv')

ntd = 252 # trading days per year

x = diff(log(data$Adj.Close)) # closing price log-differences

mu     = mean(x)*ntd
sigma  = sd(x)*sqrt(ntd)
lambda = 0.024

rf = 0.05

pi.classic = (mu - rf)/sigma^2
pi.our     = ((mu - rf + sigma^2) - sqrt((sigma^2 - mu + rf)^2 + 4*lambda*sigma^2))/(2*sigma^2)