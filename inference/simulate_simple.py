from scipy import stats
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from pyfret import pyFRET as pft
import matplotlib
matplotlib.rcParams.update({'font.size': 16})

def make_data(n=100000):
	donor = []
	acceptor = []
	prob = 0.05
	for i in range(n):
		d = stats.poisson.rvs(mu=0.8)
		a = stats.poisson.rvs(mu=0.8)
		if random.random() < prob:
			d += stats.poisson.rvs(mu=40)
			a += stats.poisson.rvs(mu=40)
		donor.append(d)
		acceptor.append(a)
	maxval = max(max(donor), max(acceptor))
	#data_matrix = np.zeros((maxval+1, maxval+1))
	#for dv, av in zip(donor, acceptor):
	#	data_matrix[dv][av] += 1
	plt.hist2d(donor, acceptor, bins=np.arange(0, maxval+1, 1), norm=LogNorm())
	plt.colorbar()
	plt.xlabel("Donor Photons")
	plt.ylabel("Acceptor Photons")
	plt.xlim(0, 100)
	plt.ylim(0, 100)
	plt.plot((15, 15), (0, 100), c="k", linewidth="2")
	plt.plot((0, 100), (15, 15), c="k", linewidth="2")
	#plt.plot((0, 15), (15, 0), c="k", linewidth="2", linestyle="--")
	plt.savefig("idealised_AND.pdf")
	
	plt.show()

def plot_real_data():
	fpath = "/home/rebecca/Documents/repos/pyfret_release/bin/duplexes/10bp/FRET"
	n = 60
	data = []
	for i in range(n):
		data.append("DNA%04d.dat" % i)
	datas = pft.parse_bin(fpath, data)
	maxval = max(max(datas.donor), max(datas.acceptor))
	plt.hist2d(datas.donor, datas.acceptor, bins=np.arange(0, maxval+1, 1), norm=LogNorm())
	plt.xlim(0, 100)
	plt.ylim(0, 100)
	#plt.plot((10, 10), (0, 100), c="k", linewidth="2", linestyle="--")
	#plt.plot((0, 100), (10, 10), c="k", linewidth="2", linestyle="--")
	#plt.plot((0, 10), (10, 0), c="k", linewidth="2", linestyle="--")
	plt.colorbar()

	plt.xlabel("Donor Photons")
	plt.ylabel("Acceptor Photons")
	plt.xlim(0, 100)
	plt.ylim(0, 100)
	#plt.plot((15, 15), (0, 100), c="k", linewidth="2")
	#plt.plot((0, 100), (15, 15), c="k", linewidth="2")
	plt.plot((0, 15), (15, 0), c="k", linewidth="2", linestyle="--")
	plt.savefig("real_low_SUM.pdf")
	
	plt.show()



if __name__ == "__main__":
	#make_data()
	plot_real_data()

