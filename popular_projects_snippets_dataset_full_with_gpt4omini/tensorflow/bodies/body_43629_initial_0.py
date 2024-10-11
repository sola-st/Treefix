from unittest.mock import Mock # pragma: no cover

self = Mock() # pragma: no cover
decorator_utils = Mock(get_qualified_name=Mock(return_value='_test_function')) # pragma: no cover
_test_function = lambda: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/util/decorator_utils_test.py
from l3.Runtime import _l_
self.assertEqual("_test_function",
                 decorator_utils.get_qualified_name(_test_function))
_l_(4431)
