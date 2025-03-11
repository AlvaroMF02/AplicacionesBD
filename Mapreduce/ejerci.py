from mrjob.job import MRJob
import json

class WordCount(MRJob):
    
    def mapper(self,_,line):
        # ejecuta linea a linea
        text = json.loads(line)
        # hay que hacer un filtro pq no todos tienen
        for word in text["reviewText"].split():
            yield (word, 1)
        
    
    def reducer(self,word,count):
        # sumar los valores
        yield (word, sum(count))


if __name__=="__main__":
    WordCount.run()
    