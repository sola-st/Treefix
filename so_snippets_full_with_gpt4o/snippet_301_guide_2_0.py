import multiprocessing as mp # pragma: no cover
from multiprocessing.dummy import Pool # pragma: no cover

text = 'sample_text' # pragma: no cover
case = ['case1', 'case2'] # pragma: no cover
def harvester(text, case_item): # pragma: no cover
    return text + ' processed with ' + case_item # pragma: no cover
MockPool = type('MockPool', (object,), { # pragma: no cover
    'map': lambda self, func, iterable, chunksize: [func(item) for item in iterable], # pragma: no cover
    'apply_async': lambda self, func, iterable, chunksize: None # pragma: no cover
}) # pragma: no cover
pool = MockPool() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5442910/how-to-use-multiprocessing-pool-map-with-multiple-arguments
from l3.Runtime import _l_
try:
    import multiprocessing as mp
    _l_(12829)

except ImportError:
    pass

def foo(q, h, w):
    _l_(12832)

    q.put(h + ' ' + w)
    _l_(12830)
    print(h + ' ' + w)
    _l_(12831)

if __name__ == '__main__':
    _l_(12839)

    ctx = mp.get_context('spawn')
    _l_(12833)
    q = ctx.Queue()
    _l_(12834)
    p = ctx.Process(target=foo, args=(q,'hello', 'world'))
    _l_(12835)
    p.start()
    _l_(12836)
    print(q.get())
    _l_(12837)
    p.join()
    _l_(12838)

pool.map(harvester(text, case), case, 1)
_l_(12840)

pool.apply_async(harvester(text, case), case, 1)
_l_(12841)

