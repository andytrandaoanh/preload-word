import sys
import system_handler as sysHandle





def trim_and_sort(inputlist):
	result = inputlist
	result = list( dict.fromkeys(result))
	result.sort()
	return result

def filter_list(list1):

	list2 = list(filter(lambda s: s.islower(), list1))
	list3 =  [item for item in list1 if item not in list2]
	return(list2, list3)



def processText(pathIn, dirOut):
	pathOut = sysHandle.getRawPath(pathIn, dirOut)
	words = sysHandle.getWordFromTextFile(pathIn)
	cleanList = trim_and_sort(words)
	sysHandle.writeListToFile(cleanList, pathOut)
	sysHandle.openDir(dirOut)
	sys.exit()
