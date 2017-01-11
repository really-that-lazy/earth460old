## makeItFourier.py ############################################################
## smbc said it best ###########################################################
################################################################################
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack


def graph2dData(x, y, colour):
	fig, ax = plt.subplots()
	ax.plot(x, y, colour)
	plt.show()
	plt.close()

if(__name__ == "__main__"):
	# Number of samplepoints
	N = 600
	# sample spacing
	T = 1.0 / 800.0
	x = np.linspace(0.0, N*T, N)
	y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
	yf = scipy.fftpack.fft(y)
	xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

	##fig, ax = plt.subplots()
	graph2dData(xf, 2.0/N * np.abs(yf[:N//2]), 'b')
	graph2dData(x, y, 'g')
