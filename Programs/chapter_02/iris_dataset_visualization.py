from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

# load the iris data set with load_iris from sklearn
data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']
target_names = data['target_names']

count = 1

for feature_1 in xrange(4):
	for feature_2 in xrange(feature_1 + 1, 4):
		plt.subplot(2, 3, count)
		count = count + 1
		
		for clas, marker, color in zip(xrange(3), ">ox", "rgb"):
			plt.scatter(features[target == clas, feature_1],
						features[target == clas, feature_2],
						marker=marker,
						c=color)
		
		plt.xlabel(feature_names[feature_1])
		plt.ylabel(feature_names[feature_2])
		plt.legend(["%s" % clas for clas in target_names])
		plt.grid()

# shows all the six plots by selecting two features out of four in a single plot
plt.show()

# from the plots it can observed that setosa can be differentiated from the other two by either using petal length or petal width
# here we are considering the petal length to differentiate the class
# now to differentiate versicolor and virginica we'll plot only these two categories and visualize the plots

isSetosa = (target == 0) # 0 is for setosa
features = features[~isSetosa]
target = target[~isSetosa]
target_names = target_names[target_names != 'setosa']

count = 1

for feature_1 in xrange(4):
	for feature_2 in xrange(feature_1 + 1, 4):
		plt.subplot(2, 3, count)
		count = count + 1
		
		for clas, marker, color in zip(xrange(1, 3), "ox", "rgb"):
			plt.scatter(features[target == clas, feature_1],
						features[target == clas, feature_2],
						marker=marker,
						c=color)
		
		plt.xlabel(feature_names[feature_1])
		plt.ylabel(feature_names[feature_2])
		plt.legend(["%s" % clas for clas in target_names])
		plt.grid()

# shows all the six plots by selecting two features out of four in a single plot
plt.show()

