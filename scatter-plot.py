import matplotlib.pyplot as plt
import csv

male_x = []
male_y = []
female_x = []
female_y = []

with open('data/DWH_Training.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if int(row[3]) == 1:
            male_x.append(float(row[1]))
            male_y.append(float(row[2]))
        else:
            female_x.append(float(row[1]))
            female_y.append(float(row[2]))

plt.plot(male_x, male_y,'o', c='blue', label='Male')
plt.plot(female_x, female_y,'o', c='red', label='Female')

# horizontal line
# plt.plot([160, 180], [65, 65], c='lightgreen')

# vertical line
# plt.plot([170.8, 170.8], [40, 90], c='lightgreen')

# best seperating line
plt.plot([174.5, 168.5], [40, 90], c='lightgreen')

plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Disneyland population')
plt.legend()
plt.show()