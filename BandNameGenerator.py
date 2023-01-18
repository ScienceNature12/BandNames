#this will build you a playist for Spotify
import random

band_first= ["meaty", "vague", "nauseating", "high-pitched", "homeless", "curious", "ugliest", "acoustic", "screeching"]
band_last= ["eye liners", "cell phones", "credit cards", "air fresheners", "deodorants", "toe rings", "lamp shades",
             "nail clippers", "street lights", "sticky notes", "candy wrappers", "paint brush", "tooth picks", "rubber ducks"]

first= random.choice(band_first)
last= random.choice(band_last)
print(first + " " + last)

