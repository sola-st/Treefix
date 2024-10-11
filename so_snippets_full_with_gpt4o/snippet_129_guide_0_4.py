import sys # pragma: no cover
import time # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2846653/how-can-i-use-threading-in-python
from l3.Runtime import _l_
def sqr(val):
    _l_(14444)

    try:
        import time
        _l_(14441)

    except ImportError:
        pass
    time.sleep(0.1)
    _l_(14442)
    aux = val * val
    _l_(14443)
    return aux

def process_result(result):
    _l_(14446)

    print(result)
    _l_(14445)

def process_these_asap(tasks):
    _l_(14455)

    try:
        import concurrent.futures
        _l_(14448)

    except ImportError:
        pass

    with concurrent.futures.ProcessPoolExecutor() as executor:
        _l_(14454)

        futures = []
        _l_(14449)
        for task in tasks:
            _l_(14451)

            futures.append(executor.submit(sqr, task))
            _l_(14450)

        for future in concurrent.futures.as_completed(futures):
            _l_(14453)

            process_result(future.result())
            _l_(14452)

def main():
    _l_(14461)

    tasks = list(range(10))
    _l_(14456)
    print('Processing {} tasks'.format(len(tasks)))
    _l_(14457)
    process_these_asap(tasks)
    _l_(14458)
    print('Done')
    _l_(14459)
    aux = 0
    _l_(14460)
    return aux

if __name__ == '__main__':
    _l_(14465)

    try:
        import sys
        _l_(14463)

    except ImportError:
        pass
    sys.exit(main())
    _l_(14464)

