from typing import Set, Type, Dict, Any # pragma: no cover
from enum import Enum # pragma: no cover

class TargetVersion(Enum): version_a = 1; version_b = 2 # pragma: no cover
VERSION_TO_FEATURES: Dict[Type[TargetVersion], Set[str]] = {TargetVersion.version_a: {'feature1', 'feature2'}, TargetVersion.version_b: {'feature1'}} # pragma: no cover
node = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Detect the version to target based on the nodes used."""
features = get_features_used(node, future_imports=future_imports)
_l_(3879)
aux = {
    version for version in TargetVersion if features <= VERSION_TO_FEATURES[version]
}
_l_(3880)
exit(aux)
