from unittest.mock import Mock # pragma: no cover

self = type('MockSelf', (object,), {'device_scope': Mock(return_value=None)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_test.py
from l3.Runtime import _l_
"""Deprecated alias of `device_scope`.

    This should be avoided as the name starts with `test`, so test runners
    treat it as a test. This interferes with class decorators that operate on
    each test method.
    """
aux = self.device_scope()
_l_(4380)
exit(aux)
