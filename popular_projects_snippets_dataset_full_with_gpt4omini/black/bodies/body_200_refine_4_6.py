from typing import List, Dict, Set, Union # pragma: no cover

node = 'example_node' # pragma: no cover
TargetVersion = {'2.0', '3.0', '3.6', '3.10'} # pragma: no cover
VERSION_TO_FEATURES = {'2.0': {'feature1'}, '3.0': {'feature1', 'feature2'}, '3.6': {'feature1', 'feature2', 'feature3'}, '3.10': {'feature1', 'feature2', 'feature3', 'feature4'}} # pragma: no cover

from typing import Set, Dict # pragma: no cover

node = 'example_node' # pragma: no cover
TargetVersion = {'version_1', 'version_2', 'version_3'} # pragma: no cover
VERSION_TO_FEATURES = {'version_1': {'feature_a'}, 'version_2': {'feature_a', 'feature_b'}, 'version_3': {'feature_a', 'feature_b', 'feature_c'}} # pragma: no cover

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
