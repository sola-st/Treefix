import os # pragma: no cover
import tempfile # pragma: no cover

util = type('util', (), {'Checkpoint': type('Checkpoint', (object,), {})})() # pragma: no cover
checkpoint_management = type('checkpoint_management', (), {'CheckpointManager': type('CheckpointManager', (object,), {'__init__': lambda self, checkpoint, dir, max_to_keep: None, 'save': lambda self: os.path.join(tempfile.gettempdir(), 'checkpoint_{:02d}'.format(hash(self) % 1000))}), 'checkpoint_exists': lambda path: os.path.exists(path)})() # pragma: no cover
self = type('Mock', (object,), {'get_temp_dir': lambda self: tempfile.gettempdir(), 'assertTrue': lambda self, condition: print('assertTrue:', condition), 'assertFalse': lambda self, condition: print('assertFalse:', condition)})() # pragma: no cover

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
