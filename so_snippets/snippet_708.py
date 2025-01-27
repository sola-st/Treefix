# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9786102/how-do-i-parallelize-a-simple-python-loop
from l3.Runtime import _l_
try:
    from tqdm.contrib.concurrent import thread_map, process_map
    _l_(1737)

except ImportError:
    pass


def calc_stuff(num, multiplier):
    _l_(1742)

    try:
        import time
        _l_(1739)

    except ImportError:
        pass

    time.sleep(1)
    _l_(1740)
    aux = num, num * multiplier
    _l_(1741)

    return aux


if __name__ == "__main__":
    _l_(1747)


    # let's parallelize this for loop:
    # results = [calc_stuff(i, 2) for i in range(64)]

    loop_idx = range(64)
    _l_(1743)
    multiplier = [2] * len(loop_idx)
    _l_(1744)

    # either with threading:
    results_threading = thread_map(calc_stuff, loop_idx, multiplier)
    _l_(1745)

    # or with multi-processing:
    results_processes = process_map(calc_stuff, loop_idx, multiplier)
    _l_(1746)

