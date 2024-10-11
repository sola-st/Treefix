from typing import List # pragma: no cover
from dataclasses import dataclass # pragma: no cover

@dataclass # pragma: no cover
class Line: # pragma: no cover
    content: str = 'default_content' # pragma: no cover
 # pragma: no cover
class MockBase: # pragma: no cover
    def __post_init__(self): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
self = type('Mock', (MockBase,), {'mode': 'default_mode', 'features': ['feature1', 'feature2'], 'current_line': Line()})() # pragma: no cover
mode = 'default_mode' # pragma: no cover
features = ['feature1', 'feature2'] # pragma: no cover
Line = Line # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
self.mode = mode
_l_(19734)
self.features = features
_l_(19735)
self.current_line: Line
_l_(19736)
self.__post_init__()
_l_(19737)
