# Extracted from https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings
slist = list(filter(None, slist))

slist = ' '.join(slist).split()

slist = list(filter(str.strip, slist))

## Build test-data
#
import random, string
nwords = 10000
maxlen = 30
null_ratio = 0.1
rnd = random.Random(0)                  # deterministic results
words = [' ' * rnd.randint(0, maxlen)
         if rnd.random() > (1 - null_ratio)
         else
         ''.join(random.choices(string.ascii_letters, k=rnd.randint(0, maxlen)))
         for _i in range(nwords)
        ]

## Test functions
#
def nostrip_filter(slist):
    return list(filter(None, slist))

def nostrip_comprehension(slist):
    return [s for s in slist if s]

def strip_filter(slist):
    return list(filter(str.strip, slist))

def strip_filter_map(slist): 
    return list(filter(None, map(str.strip, slist))) 

def strip_filter_comprehension(slist):  # waste memory
    return list(filter(None, [s.strip() for s in slist]))

def strip_filter_generator(slist):
    return list(filter(None, (s.strip() for s in slist)))

def strip_join_split(slist):  # words without(!) spaces
    return ' '.join(slist).split()

## Benchmarks
#
%timeit nostrip_filter(words)
142 µs ± 16.8 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%timeit nostrip_comprehension(words)
263 µs ± 19.1 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%timeit strip_filter(words)
653 µs ± 37.5 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%timeit strip_filter_map(words)
642 µs ± 36 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%timeit strip_filter_comprehension(words)
693 µs ± 42.2 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%timeit strip_filter_generator(words)
750 µs ± 28.6 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%timeit strip_join_split(words)
796 µs ± 103 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

