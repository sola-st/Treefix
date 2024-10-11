import tempfile # pragma: no cover
import os # pragma: no cover

util = type('MockUtil', (object,), {'Checkpoint': lambda: 'checkpoint_instance'})() # pragma: no cover
checkpoint_management = type('MockCheckpointManagement', (object,), {'CheckpointManager': lambda checkpoint, temp_dir, max_to_keep: MockCheckpointManager(checkpoint, temp_dir, max_to_keep)})() # pragma: no cover
class MockCheckpointManager: # pragma: no cover
    def __init__(self, checkpoint, temp_dir, max_to_keep): # pragma: no cover
        self.checkpoint = checkpoint # pragma: no cover
        self.temp_dir = temp_dir # pragma: no cover
        self.max_to_keep = max_to_keep # pragma: no cover
        self.paths = [] # pragma: no cover
    def save(self): # pragma: no cover
        path = os.path.join(self.temp_dir, f'checkpoint_{len(self.paths) + 1}') # pragma: no cover
        self.paths.append(path) # pragma: no cover
        return path # pragma: no cover
    @staticmethod # pragma: no cover
    def checkpoint_exists(path): # pragma: no cover
        return path in self.paths # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
    'get_temp_dir': lambda: tempfile.gettempdir(), # pragma: no cover
    'assertTrue': lambda condition: None if condition else Exception('Assertion failed: Condition is not true'), # pragma: no cover
    'assertFalse': lambda condition: None if not condition else Exception('Assertion failed: Condition is not false') # pragma: no cover
})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
from l3.Runtime import _l_
checkpoint = util.Checkpoint()
_l_(21599)
manager = checkpoint_management.CheckpointManager(
    checkpoint, self.get_temp_dir(), max_to_keep=3)
_l_(21600)
first_path = manager.save()
_l_(21601)
second_path = manager.save()
_l_(21602)
third_path = manager.save()
_l_(21603)
fourth_path = manager.save()
_l_(21604)
self.assertTrue(checkpoint_management.checkpoint_exists(fourth_path))
_l_(21605)
self.assertTrue(checkpoint_management.checkpoint_exists(third_path))
_l_(21606)
self.assertTrue(checkpoint_management.checkpoint_exists(second_path))
_l_(21607)
self.assertFalse(checkpoint_management.checkpoint_exists(first_path))
_l_(21608)
