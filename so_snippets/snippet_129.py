# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2846653/how-can-i-use-threading-in-python
from l3.Runtime import _l_
def sqr(val):
    _l_(2241)

    try:
        import time
        _l_(2238)

    except ImportError:
        pass
    time.sleep(0.1)
    _l_(2239)
    aux = val * val
    _l_(2240)
    return aux

def process_result(result):
    _l_(2243)

    print(result)
    _l_(2242)

def process_these_asap(tasks):
    _l_(2252)

    try:
        import concurrent.futures
        _l_(2245)

    except ImportError:
        pass

    with concurrent.futures.ProcessPoolExecutor() as executor:
        _l_(2251)

        futures = []
        _l_(2246)
        for task in tasks:
            _l_(2248)

            futures.append(executor.submit(sqr, task))
            _l_(2247)

        for future in concurrent.futures.as_completed(futures):
            _l_(2250)

            process_result(future.result())
            _l_(2249)

def main():
    _l_(2258)

    tasks = list(range(10))
    _l_(2253)
    print('Processing {} tasks'.format(len(tasks)))
    _l_(2254)
    process_these_asap(tasks)
    _l_(2255)
    print('Done')
    _l_(2256)
    aux = 0
    _l_(2257)
    return aux

if __name__ == '__main__':
    _l_(2262)

    try:
        import sys
        _l_(2260)

    except ImportError:
        pass
    sys.exit(main())
    _l_(2261)

