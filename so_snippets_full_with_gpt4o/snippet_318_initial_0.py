text = 'some example text that needs to be split' # pragma: no cover
tokens = [' ', 'e', 't'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1059559/split-strings-into-words-with-multiple-word-boundary-delimiters
from l3.Runtime import _l_
join = lambda x: sum(x,[])  # a.k.a. flatten1([[1],[2,3],[4]]) -> [1,2,3,4]
_l_(13525)  # a.k.a. flatten1([[1],[2,3],[4]]) -> [1,2,3,4]
# ...alternatively...
join = lambda lists: [x for l in lists for x in l]
_l_(13526)

fragments = [text]
_l_(13527)
for token in tokens:
    _l_(13529)

    fragments = join(f.split(token) for f in fragments)
    _l_(13528)

