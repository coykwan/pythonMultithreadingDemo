import time
import operator
from concurrent.futures import ThreadPoolExecutor

from functools import reduce

info = open("/Users/coy/Development/WarAndPeace.txt","r")
data = list(info.read())
dataPairs = zip(data[::2], data[1::2])
dataTriplet = zip(data[::2], data[1::2], data[2::3])

def buildCharCount(dict, char):
    if (dict.keys().count(char) > 0):
        dict[char] = dict[char] + 1
    else:
        dict[char] = 1
    return dict
        
    
def calculateProbabilitiesForList(l):
    def calculateProbabilities(dict, next):
        key = next[0]
        value = next[1]
        dict[key] = str(round(float(value)/float(len(l)) * 100, 5))  + '%'
        return dict
    return calculateProbabilities

def buildProcess(arr, title):
    def process():
        start_time = time.time()

        count = reduce(buildCharCount, arr, {})
        reduce(calculateProbabilitiesForList(arr), list(count.items()), {})

        print(title + ' took:')
        print("--- %s Seconds ---" % (time.time() - start_time))

    return process


start_time = time.time()

executor = ThreadPoolExecutor(max_workers=16)

pairs = executor.submit(buildProcess(dataPairs, 'Pairs'))
# triplet = executor.submit(buildProcess(dataTriplet, 'Triplet'))
single = executor.submit(buildProcess(data, 'Single'))

# print('The total time was:')
# print("--- %s Seconds ---" % (time.time() - start_time))

