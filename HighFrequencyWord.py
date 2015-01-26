# coding=utf-8
import re

fileName = 'voca.txt';

vocabularyList 	= [];
vocabularyCount = [];

with open(fileName, 'r') as f:
	for line in f:
		words = re.findall('[a-z-]+', line.lower(), flags=re.I)

		for word in words:
			if word not in vocabularyList:
				vocabularyList.append(word);
				vocabularyCount.append(1);
			else:
				vocabularyCount[vocabularyList.index(word)]+=1;
				print vocabularyCount[vocabularyList.index(word)];

print vocabularyList;
print vocabularyCount;

wordList = 'wordList.txt';
count = len(vocabularyList);
with open(wordList, 'w') as f:
	for num in xrange(0,count):
		f.write("%s %d\n"%(vocabularyList[vocabularyCount.index(max(vocabularyCount))],max(vocabularyCount)));
		vocabularyCount[vocabularyCount.index(max(vocabularyCount))] = 0;

