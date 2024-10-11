from typing import List # pragma: no cover
from collections import namedtuple # pragma: no cover

line = 'example input line' # pragma: no cover
features = ['feature1', 'feature2'] # pragma: no cover
def split_func(line: str, features: List[str]):# pragma: no cover
    SplitLine = namedtuple('SplitLine', ['leaves'])# pragma: no cover
    return [SplitLine(leaves=line.split())] # pragma: no cover
class MockNormalizer:# pragma: no cover
    def __call__(self, text: str, inside_brackets: bool = False):# pragma: no cover
        pass# pragma: no cover
normalize_prefix = MockNormalizer() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
for split_line in split_func(line, features):
    _l_(20310)

    normalize_prefix(split_line.leaves[0], inside_brackets=True)
    _l_(20308)
    aux = split_line
    _l_(20309)
    exit(aux)
