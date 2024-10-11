from typing import List # pragma: no cover
class SplitLine: # pragma: no cover
    def __init__(self, leaves: List[str]): # pragma: no cover
        self.leaves = leaves # pragma: no cover
def split_func(line: str, features: List[str]) -> List[SplitLine]: # pragma: no cover
    return [SplitLine([line])] * len(features) # pragma: no cover
def normalize_prefix(leaf: str, inside_brackets: bool) -> None: # pragma: no cover
    if inside_brackets: # pragma: no cover
        print('Normalized:', leaf) # pragma: no cover

split_func = lambda line: split_func(line, features) # pragma: no cover
line = 'example line for processing' # pragma: no cover
features = ['feature1', 'feature2'] # pragma: no cover
normalize_prefix = lambda leaf, inside_brackets: print(f'Normalized {leaf} with inside_brackets={inside_brackets}') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
for split_line in split_func(line, features):
    _l_(8768)

    normalize_prefix(split_line.leaves[0], inside_brackets=True)
    _l_(8766)
    aux = split_line
    _l_(8767)
    exit(aux)
