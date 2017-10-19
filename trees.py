from math import log
import numpy
import operator
def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    # change to discrete values
    return dataSet, labels

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet: 
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2) #log base 2
    return shannonEnt

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[: axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


#choose best feature
def chooseBestFeatureToSplit(dataSet):
##    print(dataSet)
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
####    print(uniqueVals)
        newEntropy = 0.0
        for value in uniqueVals:
####        print(value)
            subDataSet = splitDataSet(dataSet, i, value)
####        print(subDataSet)
            prob = len(subDataSet)/float(len(dataSet))
####        print(str(prob)+"   "+str(calcShannonEnt(subDataSet)))
            newEntropy += prob * calcShannonEnt(subDataSet)
####        print("Num"+str(i)+"'s shannonEnt is"+ str(newEntropy))
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature
##
dataSet, labels = createDataSet()
##shannonEnt = calcShannonEnt(dataSet)
##print(shannonEnt)
##
##print(chooseBestFeatureToSplit(dataSet))

def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), \
                              key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]



def createTree(dataSet, labels):
##    print(dataSet)
##    print(labels)
    classList = [example[-1] for example in dataSet]
##    print(classList)
    if classList.count(classList[0]) == len(classList):
##        print('i = '+str(i))
##        i += 1
##        print(classList)
        return classList[0]
    if len(dataSet[0]) == 1:
##        print('j = '+str(i))
##        i += 1
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
##    print(bestFeat)
    bestFeatLabel = labels[bestFeat]
##    print(bestFeatLabel)
    myTree = {bestFeatLabel: {}}
##    print(myTree)
    del(labels[bestFeat])
##    print(labels)
    featValues = [example[bestFeat] for example in dataSet]
##    print(featValues)
    uniqueVals = set(featValues)
##    print(uniqueVals)
##    print("ok")
    for value in uniqueVals:
        subLabels = labels[:]
##        print("循环一次",end = ' ')
##        print(myTree)
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, \
                                            bestFeat, value), subLabels)
    return myTree
 

def classify(inputTree, featLabels, testVec):
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]) == dict:
                classLabel = classify(secondDict[key],
                                      featLabels, testVec)
            else: classLabel = secondDict[key]
    return classLabel


myTree = {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}

print(classify(myTree, labels, [1,1]))

def storeTree(inputTree, filename):
    import pickle
    inputTree = str(inputTree)
    fw = open(filename, mode = 'wb')
    pickle.dump(inputTree, fw)
    fw.close()

def grabTree(filename):
    import pickle
    fr = open(filename,'rb')
    return pickle.load(fr)


##filename = 'classifierStorage.txt'
##filename1 = 'classifierStorage1.txt'
##storeTree(myTree, filename)
##fr = open('lenses.txt')
##lenses = [inst.strip().split('\t') for inst in fr.readlines()]
##lensesLabels = ['age', 'prescript', 'astigmatic', 'trarRate']
##lensesTree = createTree(lenses, lensesLabels)
##storeTree(lensesTree, filename1)
##grabTree(filename)
##print(grabTree(filename1))
##
