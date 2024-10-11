self = type('Mock', (), {'get_temp_dir': lambda: '/tmp', 'assertTrue': lambda x: x, 'assertFalse': lambda x: not x})() # pragma: no cover
util = type('MockUtil', (), {'Checkpoint': lambda: None})() # pragma: no cover
checkpoint_management = type('MockCheckpointManagement', (), {'CheckpointManager': lambda checkpoint, temp_dir, max_to_keep: type('MockManager', (), {'save': lambda: '/path/to/checkpoint', '__init__': lambda self: None})(), 'checkpoint_exists': lambda path: path in ['/path/to/checkpoint', '/path/to/checkpoint', '/path/to/checkpoint']})() # pragma: no cover

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
