from typing import List, Any # pragma: no cover

def split_func(line: str, features: List[str]) -> List[Any]: return [{'leaves': [word]} for word in line.split()] # pragma: no cover
line = 'This is a sample line.' # pragma: no cover
features = ['feature1', 'feature2'] # pragma: no cover
def normalize_prefix(word: str, inside_brackets: bool = False) -> None: print(f'Normalizing: {word}, Inside brackets: {inside_brackets}') # pragma: no cover

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
