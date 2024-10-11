import multiprocessing as mp # pragma: no cover
from multiprocessing import Pool # pragma: no cover

text = 'sample text' # pragma: no cover
case = ['case1', 'case2'] # pragma: no cover
pool = Pool(processes=2) # pragma: no cover
def harvester(text, case): return f'{text} processed with {case}' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5442910/how-to-use-multiprocessing-pool-map-with-multiple-arguments
from l3.Runtime import _l_
try:
    import multiprocessing as mp
    _l_(834)

except ImportError:
    pass

def foo(q, h, w):
    _l_(837)

    q.put(h + ' ' + w)
    _l_(835)
    print(h + ' ' + w)
    _l_(836)

if __name__ == '__main__':
    _l_(844)

    ctx = mp.get_context('spawn')
    _l_(838)
    q = ctx.Queue()
    _l_(839)
    p = ctx.Process(target=foo, args=(q,'hello', 'world'))
    _l_(840)
    p.start()
    _l_(841)
    print(q.get())
    _l_(842)
    p.join()
    _l_(843)

pool.map(harvester(text, case), case, 1)
_l_(845)

pool.apply_async(harvester(text, case), case, 1)
_l_(846)

