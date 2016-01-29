import sys
import math

c = 1e-6

def readTrainingFeatureFile(trainingFeatureFileName, D):
	print("Opening Training Feature File: " + trainingFeatureFileName)
	trainingFeatureFile = open(trainingFeatureFileName, 'r')
	trainingFeature = list()

	print("Reading Training Feature File ...")
	for line in trainingFeatureFile:
		try:
			sample = [int(num) for num in line.split(' ')]
		except ValueError:
			print("Error: there is a non-numeric value in this file! ")
			sys.exit()

		if len(sample) != int(D):
			print("Error: Exist a sample with wrong dimension! ")
			sys.exit()

		trainingFeature.append(sample)

	trainingFeatureFile.close()

	print("Obtain a training feature vector with " + str(len(trainingFeature)) + " samples")
	print("Each sample has dimension " + D)

	return trainingFeature

def readTrainingLabelFile(trainingLabelFileName):
	print("Opening Training Label File: " + trainingLabelFileName)
	trainingLabelFile = open(trainingLabelFileName, 'r')
	trainingLabel = list()

	print("Reading Training Label File ...")
	for line in trainingLabelFile:
		try:
			label = int(line)
		except ValueError:
			print("Error: there is a non-numeric value in this file! ")
			sys.exit()

		trainingLabel.append(label)

	trainingLabelFile.close()

	print("Obtain a training Label vector with " + str(len(trainingLabel)) + " label")

	return trainingLabel

def computeLoss(trainingFeature, trainingLabel, w):
	h = float(0)

	y = -1
	if trainingLabel == 1:
		y = 1

	for x in xrange(len(w)):
		h += trainingFeature[x]*w[x]

	temp = float(math.exp(-1 * y * h))
	temp = -1 * y * temp / (1 + temp)

	loss = [temp * element for element in trainingFeature]

	print("Loss is: " + repr(loss) + "\n")

	return loss

def writeModelToFile(modelFileName, w):
	print("Creating Model File: " + modelFileName)
	modelFile = open(modelFileName, 'w')

	print("Writing to File ... ")
	for x in xrange(len(w)):
		if x == 0:
			modelFile.write(repr(w[x]))
		else:
			modelFile.write(' ' + repr(w[x]))

	modelFile.close()

def main(argv):

	scriptName, trainingFeatureFileName, trainingLabelFileName, modelFileName, D, Niter = argv

	trainingFeature = readTrainingFeatureFile(trainingFeatureFileName, D)
	trainingLabel = readTrainingLabelFile(trainingLabelFileName)

	D = int(D)
	Niter = int(Niter)
	t = 0
	w = [float(0)] * D

	print("Initially w is " + repr(w))

	for x in xrange(Niter):
		for i in xrange(len(trainingLabel)):
			t += 1
			loss = computeLoss(trainingFeature[i], trainingLabel[i], w)

			for y in xrange(D):
				w[y] -= c / t * loss[y]

			print(repr(w))

	writeModelToFile(modelFileName, w)

if __name__ == "__main__":
	main(sys.argv)