import sys

def readLabelFile(fileName):
	print("Reading Label file: " + fileName)
	f = open(fileName, 'r')

	labelList = list()
	for line in f:
		label = int(line)
		labelList.append(label)

	f.close()

	return labelList

def main(argv):
	scriptFile, predictLabelFileName, truthLabelFileName = argv

	predictLabel= readLabelFile(predictLabelFileName)
	truthLabel = readLabelFile(truthLabelFileName)

	if len(predictLabel) != len(truthLabel):
		print("Error: the size of predict labels and the size of true labels are mismatched! ")
		sys.exit()

	truePositive = 0
	for x in xrange(len(predictLabel)):
		if predictLabel[x] == truthLabel[x]:
			truePositive += 1

	print("The accuracy is " + repr(float(truePositive) / len(predictLabel) * 100) + "%\n")


if __name__ == "__main__":
	main(sys.argv)