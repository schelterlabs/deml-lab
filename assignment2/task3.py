from components.mapreduce import MapReduceEngine

partitioned_documents = [
    [(1, "Hello World"), (2, "hello universe")],
    [(3, "Hello Galaxy")]
]



def tokenize_document(_key, document):
    return [(word.lower(), 1) for word in document.split(" ")]

def count_per_word(word, counts):
    return word, sum(counts)



engine = MapReduceEngine(f_m=tokenize_document, f_r=count_per_word, num_reducers=2)

results = engine.execute(partitioned_documents)

print(results)

assert(len(results) == 4)

assert('hello' in results)
assert(results['hello'] == 3)

assert('world' in results)
assert(results['world'] == 1)

assert('universe' in results)
assert(results['universe'] == 1)

assert('galaxy' in results)
assert(results['galaxy'] == 1)
