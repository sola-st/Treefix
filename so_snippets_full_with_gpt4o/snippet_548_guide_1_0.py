class MockDelayed: # pragma: no cover
    def __init__(self, val): # pragma: no cover
        self.val = val # pragma: no cover
    def __call__(self, *args): # pragma: no cover
        return self # pragma: no cover
    def compute(self): # pragma: no cover
        return self.val # pragma: no cover
delayed = MockDelayed # pragma: no cover

file = range(1000) # pragma: no cover
partial_result = delayed([]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1316767/how-can-i-explicitly-free-memory-in-python
from l3.Runtime import _l_
try:
    from dask import delayed
    _l_(15182)

except ImportError:
    pass
def f(storage, index, chunk_size):
    _l_(15184)

    aux = storage
    _l_(15183)
    # read the chunk of size chunk_size starting at index in the file
    # process it using data in storage if needed
    # append data needed for further computations  to storage 
    return aux

partial_result = delayed([])  # put into the delayed() the constructor for your data structure
_l_(15185)  # put into the delayed() the constructor for your data structure
# I personally use "delayed(nx.Graph())" since I am creating a networkx Graph
chunk_size = 100  # ideally you want this as big as possible while still enabling the computations to fit in memory
_l_(15186)  # ideally you want this as big as possible while still enabling the computations to fit in memory
for index in range(0, len(file), chunk_size):
    _l_(15188)

    # we indicates to dask that we will want to apply f to the parameters partial_result, index, chunk_size
    partial_result = delayed(f)(partial_result, index, chunk_size)
    _l_(15187)

# this launches all the computations
result = partial_result.compute()
_l_(15189)

# one thread is spawned for each "delayed" one at a time to compute its result
# dask then closes the tread, which solves the memory freeing issue
# the strange performance issue with gc.collect() is also avoided

