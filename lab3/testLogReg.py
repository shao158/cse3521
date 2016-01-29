import sys

def readTestFeatureFile(testFeatureFileName, D):
	print("Opening Test Feature File: " + testFeatureFileName)
	testFeatureFile = open(testFeatureFileName, 'r')
	testFeature = list()

	print("Reading Test Feature File ...")
	for line in testFeatureFile:
		try:
			sample = [int(num) for num in line.split(' ')]
		except ValueError:
			print("Error: there is a non-numeric value in this file! ")
			sys.exit()

		if len(sample) != int(D):
			print("Error: Exist a sample with wrong dimension! ")
			sys.exit()

		testFeature.append(sample)

	testFeatureFile.close()

	print("Obtain a test feature vector with " + str(len(testFeature)) + " samples")
	print("Each sample has dimension " + D)

	return testFeature

def writePredictToFile(predictLabelFileName, predictLabel):
	print("Creating Predict Label File: " + predictLabelFileName)
	predictLabelFile = open(predictLabelFileName, 'w')

	print("Writing to File ... ")
	for x in xrange(len(predictLabel)):
		if x == 0:
			predictLabelFile.write(repr(predictLabel[x]))
		else:
			predictLabelFile.write('\n' + repr(predictLabel[x]))

	predictLabelFile.close()

def main(argv):

	scriptName, modelFileName, testFeatureFileName, predictLabelFileName, D = argv

	modelFile = open(modelFileName, 'r')
	w = modelFile.readline()
	modelFile.close()
	w = [float(num) for num in w.split(' ')]

	testFeature = readTestFeatureFile(testFeatureFileName, D)

	D = int(D)

	predictLabel = list()

	for x in xrange(len(testFeature)):
		h = 0
		for y in xrange(D):
			h += w[y] * testFeature[x][y]

		if h > 0:
			predictLabel.append(1)
		else:
			if h == 0:
				print("Exist h value is zero!")
				sys.exit()
			predictLabel.append(0)

	writePredictToFile(predictLabelFileName, predictLabel)

if __name__ == "__main__":
	main(sys.argv)