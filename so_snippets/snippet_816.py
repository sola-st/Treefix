# Extracted from https://stackoverflow.com/questions/1115313/cost-of-len-function
python -m timeit -s "l = range(10);" "len(l)"
10000000 loops, best of 3: 0.0677 usec per loop

python -m timeit -s "l = range(1000000);" "len(l)"
10000000 loops, best of 3: 0.0688 usec per loop

python -m timeit -s "t = (1,)*10;" "len(t)"
10000000 loops, best of 3: 0.0712 usec per loop

python -m timeit -s "t = (1,)*1000000;" "len(t)"
10000000 loops, best of 3: 0.0699 usec per loop

python -m timeit -s "s = '1'*10;" "len(s)"
10000000 loops, best of 3: 0.0713 usec per loop

python -m timeit -s "s = '1'*1000000;" "len(s)"
10000000 loops, best of 3: 0.0686 usec per loop

python -mtimeit -s"d = {i:j for i,j in enumerate(range(10))};" "len(d)"
10000000 loops, best of 3: 0.0711 usec per loop

python -mtimeit -s"d = {i:j for i,j in enumerate(range(1000000))};" "len(d)"
10000000 loops, best of 3: 0.0727 usec per loop

python -mtimeit -s"import array;a=array.array('i',range(10));" "len(a)"
10000000 loops, best of 3: 0.0682 usec per loop

python -mtimeit -s"import array;a=array.array('i',range(1000000));" "len(a)"
10000000 loops, best of 3: 0.0753 usec per loop

python -mtimeit -s"s = {i for i in range(10)};" "len(s)"
10000000 loops, best of 3: 0.0754 usec per loop

python -mtimeit -s"s = {i for i in range(1000000)};" "len(s)"
10000000 loops, best of 3: 0.0713 usec per loop

python -mtimeit -s"from collections import deque;d=deque(range(10));" "len(d)"
100000000 loops, best of 3: 0.0163 usec per loop

python -mtimeit -s"from collections import deque;d=deque(range(1000000));" "len(d)"
100000000 loops, best of 3: 0.0163 usec per loop

