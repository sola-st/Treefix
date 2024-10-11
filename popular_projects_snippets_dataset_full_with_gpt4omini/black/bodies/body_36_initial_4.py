from typing import List # pragma: no cover
class MockLeaf: pass # pragma: no cover

class MockLeaf: pass # pragma: no cover
line = 'example text' # pragma: no cover
features = ['feature1', 'feature2'] # pragma: no cover

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
