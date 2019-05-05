import csv
import math
import operator
import numpy
import itertools

# function to import data from csv
def import_data(file_name, dataset):
	with open(file_name,'r') as csvfile:
		lines = csv.reader(csvfile, delimiter=',')
		for row in lines:
			dataset.append([float(row[1]), float(row[2]), int(row[3])])

# as all the citizens hight and weight are numeric and have same units we can use euclidean distance
def euclidean_distance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

def get_neighbors(training_set, test_instance, k):
	distances = []
	length = len(test_instance)-1
	for x in range(len(training_set)):
		dist = euclidean_distance(test_instance, training_set[x], length)
		distances.append((training_set[x], dist))
	# sorting w.r.t distance
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

# returns the maximum voted gender in the neighbors
def get_response(neighbors):
	gender_vote = {}
	for x in range(len(neighbors)):
		gender = neighbors[x][-1]
		if gender in gender_vote:
			gender_vote[gender] += 1
		else:
			gender_vote[gender] = 1
	# sorting gender votes on maximum votes
	sorted_votes = sorted(gender_vote.items(), key=operator.itemgetter(1), reverse=True)
	return sorted_votes[0][0]

# calculates the accuracy of predictions with the test set
def get_accuracy(test_set, predictions):
	correct = 0
	for x in range(len(test_set)):
		if test_set[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(test_set))) * 100.0

# the main function
def main():

	training_set = []
	test_set = []

	# importing training data set
	import_data('data/DWH_Training.csv', training_set)

	# importing test data set
	import_data('data/DWH_test.csv', test_set)

	predictions=[]

	k = 3

	for x in range(len(test_set)):
		neighbors = get_neighbors(training_set, test_set[x], k)
		result = get_response(neighbors)
		predictions.append(result)
		print('Predicted=' + repr(result) + ', Actual=' + repr(test_set[x][-1]))

	accuracy = get_accuracy(test_set, predictions)

	print('Accuracy: ' + repr(accuracy) + '%')

main()