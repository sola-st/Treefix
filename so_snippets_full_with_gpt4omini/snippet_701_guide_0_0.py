import yaml # pragma: no cover
from unittest.mock import mock_open, patch # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5055042/whats-the-best-practice-using-a-settings-file-in-python
from l3.Runtime import _l_
try:
    import yaml
    _l_(2431)

except ImportError:
    pass
config = yaml.safe_load(open("path/to/config.yml"))
_l_(2432)

