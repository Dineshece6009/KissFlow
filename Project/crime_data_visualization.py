import numpy as np
import matplotlib.pyplot as plt

train_percentage = 91.9
test_percentage = 8.1

plt.figure(figsize=(8, 5))
plt.pie(x=np.array([train_percentage, test_percentage]), autopct="%.1f%%", explode=[0.1, 0.1],
        labels=["Training Data", "Test Data"], pctdistance=0.5, colors=['yellow', 'green'])
plt.title("Train and Test Images", fontsize=18)
plt.show()

crimes = {
    "Shoplifting": 200000,
    "Fighting": 400000,
    "Vandalism": 600000,
    "Stealing": 800000,
    "RoadAccidents": 1000000,
    "Abuse": 1200000,
    "Assault": 1400000,
    "Burglary": 1600000,
    "Bugoous": 1800000,
    "Explosion": 2000000,
    "Robbery": 2200000,
    "Arrest": 2400000,
    "Arson": 2600000,
    "NormalVideos": 2800000
}

plt.figure(figsize=(15, 5))
plt.bar(list(crimes.keys()), list(crimes.values()), width=0.4, align="center", edgecolor='red', color='orange')
plt.xticks(rotation=90)
plt.xlabel("Reported Crimes")
plt.ylabel("Number of Reported Crimes")
plt.show()
