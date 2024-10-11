import os # pragma: no cover

util = type('MockUtil', (), {'Checkpoint': lambda: None})() # pragma: no cover
checkpoint_management = type('MockCheckpointManagement', (), {'CheckpointManager': lambda checkpoint, temp_dir, max_to_keep: type('MockManager', (), {'save': lambda self: os.path.join(temp_dir, 'checkpoint_{}.ckpt'.format(self.counter)), 'counter': 0})(), 'checkpoint_exists': lambda path: os.path.exists(path)})() # pragma: no cover
os.mkdir('/tmp') if not os.path.exists('/tmp') else None # pragma: no cover
self = type('MockSelf', (), {'get_temp_dir': lambda: '/tmp', 'assertTrue': lambda condition: print('Assertion True:', condition), 'assertFalse': lambda condition: print('Assertion False:', condition)})() # pragma: no cover

import os # pragma: no cover

class MockCheckpoint: pass # pragma: no cover

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
