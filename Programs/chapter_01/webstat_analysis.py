import scipy as sp
import matplotlib.pyplot as plt

colors = ['g', 'k', 'b', 'm', 'r']
linestyles = ['-', '-.', '--', ':', '-']

def error(f, x, y):
	return sp.sum((f(x) - y)**2)

def plot_models(x, y, models=None):
	plt.scatter(x, y)
	plt.title("Web traffic over the last month")
	plt.xlabel("Time")
	plt.ylabel("Hits/hour")
	plt.xticks([w * 7 * 24 for w in range(10)], ['week %i'%w for w in range(10)])
	
	fx = sp.linspace(0, x[-1], 1000)

	for model, style, color in zip(models, linestyles, colors):
		plt.plot(fx, model(fx), linestyle=style, linewidth=2, c=color)

	plt.legend(["d=%i" % model.order for model in models], loc="upper left")

	plt.autoscale(tight=False)
	plt.grid()
	plt.show()

# reading the data
data = sp.genfromtxt("data/web_traffic.tsv", delimiter="\t")

# prints the first 10 rows of the dataset
print data[:10] 

# prints the dimensions of the dataset
print data.shape

# preprocessing and cleaning the data
x = data[:,0]
y = data[:,1]

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

fp1, res1, rank1, sv1, rcond1 = sp.polyfit(x, y, 1, full=True)
print "Model parameters : %s" % fp1
print "Model error : %s" % res1

fp2, res2, rank2, sv2, rcond2 = sp.polyfit(x, y, 2, full=True)
print "Model parameters : %s" % fp2
print "Model error : %s" % res2

fp3 = sp.polyfit(x, y, 3)
fp10 = sp.polyfit(x, y, 10)
fp100 = sp.polyfit(x, y, 100) 

f1 = sp.poly1d(fp1)
f2 = sp.poly1d(fp2)
f3 = sp.poly1d(fp3)
f10 = sp.poly1d(fp10)
f100 = sp.poly1d(fp100)

plot_models(x, y, [f1, f2, f3, f10, f100])
