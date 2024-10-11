# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9786102/how-do-i-parallelize-a-simple-python-loop
from l3.Runtime import _l_
try:
    from tqdm.contrib.concurrent import thread_map, process_map
    _l_(13860)

except ImportError:
    pass


def calc_stuff(num, multiplier):
    _l_(13865)

    try:
        import time
        _l_(13862)

    except ImportError:
        pass

    time.sleep(1)
    _l_(13863)
    aux = num, num * multiplier
    _l_(13864)

    return aux


if __name__ == "__main__":
    _l_(13870)


    # let's parallelize this for loop:
    # results = [calc_stuff(i, 2) for i in range(64)]

    loop_idx = range(64)
    _l_(13866)
    multiplier = [2] * len(loop_idx)
    _l_(13867)

    # either with threading:
    results_threading = thread_map(calc_stuff, loop_idx, multiplier)
    _l_(13868)

    # or with multi-processing:
    results_processes = process_map(calc_stuff, loop_idx, multiplier)
    _l_(13869)

