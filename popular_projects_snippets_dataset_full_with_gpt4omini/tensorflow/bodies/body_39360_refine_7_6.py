self = type('MockSelf', (), {'get_temp_dir': lambda self: 'temp_directory', 'assertTrue': lambda self, x: None, 'assertFalse': lambda self, x: None})() # pragma: no cover

from unittest.mock import Mock # pragma: no cover

util = Mock() # pragma: no cover
util.Checkpoint = Mock() # pragma: no cover
checkpoint_management = Mock() # pragma: no cover
checkpoint_management.CheckpointManager = Mock() # pragma: no cover
checkpoint_management.CheckpointManager.return_value.save.return_value = 'checkpoint_path' # pragma: no cover
checkpoint_management.checkpoint_exists = Mock(side_effect=lambda path: path in ['checkpoint_path']) # pragma: no cover
self = Mock() # pragma: no cover
self.get_temp_dir = Mock(return_value='/tmp') # pragma: no cover
self.assertTrue = Mock() # pragma: no cover
self.assertFalse = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
from l3.Runtime import _l_
checkpoint = util.Checkpoint()
_l_(9241)
manager = checkpoint_management.CheckpointManager(
    checkpoint, self.get_temp_dir(), max_to_keep=3)
_l_(9242)
first_path = manager.save()
_l_(9243)
second_path = manager.save()
_l_(9244)
third_path = manager.save()
_l_(9245)
fourth_path = manager.save()
_l_(9246)
self.assertTrue(checkpoint_management.checkpoint_exists(fourth_path))
_l_(9247)
self.assertTrue(checkpoint_management.checkpoint_exists(third_path))
_l_(9248)
self.assertTrue(checkpoint_management.checkpoint_exists(second_path))
_l_(9249)
self.assertFalse(checkpoint_management.checkpoint_exists(first_path))
_l_(9250)
