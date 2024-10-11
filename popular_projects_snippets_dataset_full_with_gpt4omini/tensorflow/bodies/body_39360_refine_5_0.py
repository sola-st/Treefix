self = type('Mock', (), {'get_temp_dir': lambda: '/tmp/checkpoints', 'assertTrue': lambda x: x, 'assertFalse': lambda x: not x})() # pragma: no cover

import os # pragma: no cover

class MockCheckpoint: pass # pragma: no cover
util = type('MockUtil', (), {'Checkpoint': MockCheckpoint})() # pragma: no cover
class MockCheckpointManager: # pragma: no cover
    def __init__(self, checkpoint, temp_dir, max_to_keep): # pragma: no cover
        self.checkpoint = checkpoint # pragma: no cover
        self.temp_dir = temp_dir # pragma: no cover
        self.saved_checkpoints = [] # pragma: no cover
        self.max_to_keep = max_to_keep # pragma: no cover
        self.counter = 0 # pragma: no cover
    def save(self): # pragma: no cover
        checkpoint_path = os.path.join(self.temp_dir, f'checkpoint_{self.counter}.ckpt') # pragma: no cover
        self.saved_checkpoints.append(checkpoint_path) # pragma: no cover
        self.counter += 1 # pragma: no cover
        return checkpoint_path # pragma: no cover
checkpoint_management = type('MockCheckpointManagement', (), {'CheckpointManager': MockCheckpointManager, 'checkpoint_exists': lambda path: path in ['/tmp/checkpoints/checkpoint_0.ckpt', '/tmp/checkpoints/checkpoint_1.ckpt', '/tmp/checkpoints/checkpoint_2.ckpt']})() # pragma: no cover
self = type('MockSelf', (), {'get_temp_dir': lambda: '/tmp/checkpoints', 'assertTrue': lambda condition: print('Assertion True:', condition), 'assertFalse': lambda condition: print('Assertion False:', condition)})() # pragma: no cover

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
