import tempfile # pragma: no cover
import numpy as np # pragma: no cover
from unittest import TestCase # pragma: no cover

self = type('Mock', (TestCase,), {'get_temp_dir': lambda self: tempfile.mkdtemp(), 'cached_session': lambda self: self, 'assertEqual': TestCase().assertEqual}) # pragma: no cover
_create_checkpoints = lambda session, dir: None  # Mock implementation # pragma: no cover
checkpoint_utils = type('Mock', (object,), {'list_variables': lambda dir: [('useful_scope/var4', [9, 9]), ('var1', [1, 10]), ('var2', [10, 10]), ('var3', [100, 100])]}) # pragma: no cover

import tempfile # pragma: no cover
import numpy as np # pragma: no cover
from unittest import TestCase # pragma: no cover
from unittest.mock import Mock # pragma: no cover

class MockSession: # pragma: no cover
    def __enter__(self): # pragma: no cover
        return self # pragma: no cover
    def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
        pass # pragma: no cover
self = type('Mock', (TestCase,), {'get_temp_dir': Mock(return_value=tempfile.mkdtemp()), 'cached_session': Mock(return_value=MockSession()), 'assertEqual': TestCase().assertEqual})() # pragma: no cover
_create_checkpoints = Mock() # pragma: no cover
checkpoint_utils = type('Mock', (object,), {'list_variables': Mock(return_value=[('useful_scope/var4', [9, 9]), ('var1', [1, 10]), ('var2', [10, 10]), ('var3', [100, 100])])})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils_test.py
from l3.Runtime import _l_
checkpoint_dir = self.get_temp_dir()
_l_(21427)
with self.cached_session() as session:
    _l_(21429)

    _create_checkpoints(session, checkpoint_dir)
    _l_(21428)
self.assertEqual(
    checkpoint_utils.list_variables(checkpoint_dir),
    [("useful_scope/var4", [9, 9]), ("var1", [1, 10]), ("var2", [10, 10]),
     ("var3", [100, 100])])
_l_(21430)
