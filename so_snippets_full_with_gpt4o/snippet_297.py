# Extracted from https://stackoverflow.com/questions/94935/what-is-the-difference-between-range-and-xrange-functions-in-python-2-x
python -m timeit "for i in xrange(10111):" " for k in range(100):" "  pass"
10 loops, best of 3: 59.4 msec per loop

python -m timeit "for i in xrange(10111):" " for k in xrange(100):" "  pass"
10 loops, best of 3: 46.9 msec per loop

