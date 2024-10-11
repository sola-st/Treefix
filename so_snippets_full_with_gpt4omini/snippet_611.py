# Extracted from https://stackoverflow.com/questions/7286365/print-a-list-in-reverse-order-with-range
python -m timeit "[9-i for i in range(10)]"
1000000 loops, best of 3: 1.54 usec per loop

python -m timeit "range(10)[::-1]"
1000000 loops, best of 3: 0.743 usec per loop

python -m timeit "reversed(range(10))"
1000000 loops, best of 3: 0.538 usec per loop

python -m timeit "range(9,-1,-1)"
1000000 loops, best of 3: 0.401 usec per loop

