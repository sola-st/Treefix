from typing import Set # pragma: no cover
from enum import Enum, auto # pragma: no cover
from collections import defaultdict # pragma: no cover

class TargetVersion(Enum):# pragma: no cover
    VERSION_1 = auto()# pragma: no cover
    VERSION_2 = auto() # pragma: no cover
VERSION_TO_FEATURES = defaultdict(set)# pragma: no cover
VERSION_TO_FEATURES[TargetVersion.VERSION_1] = {'feature1', 'feature2'}# pragma: no cover
VERSION_TO_FEATURES[TargetVersion.VERSION_2] = {'feature1', 'feature2', 'feature3'} # pragma: no cover
    return {'feature1', 'feature2'}  # Example set of features # pragma: no cover
node = None  # Placeholder for actual node object # pragma: no cover

from typing import Set, Dict # pragma: no cover
from enum import Enum, auto # pragma: no cover

class TargetVersion(Enum): # pragma: no cover
    VERSION_1 = auto() # pragma: no cover
    VERSION_2 = auto() # pragma: no cover
    VERSION_3 = auto() # pragma: no cover
 # pragma: no cover
VERSION_TO_FEATURES: Dict[TargetVersion, Set[str]] = { # pragma: no cover
    TargetVersion.VERSION_1: {'feature1'}, # pragma: no cover
    TargetVersion.VERSION_2: {'feature1', 'feature2'}, # pragma: no cover
    TargetVersion.VERSION_3: {'feature1', 'feature2', 'feature3', 'feature4'} # pragma: no cover
} # pragma: no cover
 # pragma: no cover
    return {'feature1', 'feature2'} # pragma: no cover
 # pragma: no cover
node = object() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Detect the version to target based on the nodes used."""
features = get_features_used(node, future_imports=future_imports)
_l_(15424)
aux = {
    version for version in TargetVersion if features <= VERSION_TO_FEATURES[version]
}
_l_(15425)
exit(aux)
