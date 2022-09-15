from mrjob.job import MRJob   # MRJob version

# Change the class name!!
class WordCounter(MRJob):  #MRJob version
    def mapper(self, key, line):
     _txt=line.split()
    _dict={}
    for word in _txt:
        x=0
        for letter in word:
               x++
        _dict[x]=_dict.get(x,0)+ 1
    return _dict

    def reducer(self, key, values):
        yield (key, sum(values))

if __name__ == '__main__':
    WordCounter.run()   # MRJob version
