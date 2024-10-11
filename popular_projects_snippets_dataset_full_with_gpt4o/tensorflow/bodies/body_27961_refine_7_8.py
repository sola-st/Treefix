self = type('Mock', (object,), { # pragma: no cover
    'skipTest': lambda self, msg: None, # pragma: no cover
    'assertIn': lambda self, x, y: None, # pragma: no cover
    'evaluate': lambda self, x: x # pragma: no cover
})() # pragma: no cover
dataset_ops = type('Mock', (object,), { # pragma: no cover
    'Dataset': type('MockDataset', (object,), { # pragma: no cover
        'range': lambda x: None # pragma: no cover
    }), # pragma: no cover
    'make_one_shot_iterator': lambda x: type('MockIterator', (object,), { # pragma: no cover
        'get_next': lambda: None, # pragma: no cover
        'get_next_as_optional': lambda: type('MockOptional', (object,), { # pragma: no cover
            'get_value': lambda: None, # pragma: no cover
            'has_value': lambda: None # pragma: no cover
        })()})() # pragma: no cover
})() # pragma: no cover
prefetching_ops = type('Mock', (object,), { # pragma: no cover
    'prefetch_to_device': lambda device: None # pragma: no cover
})() # pragma: no cover
ops = type('Mock', (object,), { # pragma: no cover
    'colocate_with': lambda x: None # pragma: no cover
})() # pragma: no cover
test_ops = type('Mock', (object,), { # pragma: no cover
    'device_placement_op': lambda: b'GPU:0' # pragma: no cover
})() # pragma: no cover

class MockSelf: # pragma: no cover
    @staticmethod # pragma: no cover
    def skipTest(reason): # pragma: no cover
        print(f"Skipping test: {reason}") # pragma: no cover
    @staticmethod # pragma: no cover
    def assertIn(a, b): # pragma: no cover
        assert a in b, f'{a} not in {b}' # pragma: no cover
    @staticmethod # pragma: no cover
    def evaluate(tensor): # pragma: no cover
        with tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(log_device_placement=True)) as sess: # pragma: no cover
            return sess.run(tensor) # pragma: no cover
self = MockSelf() # pragma: no cover
dataset_ops = type('Mock', (object,), { # pragma: no cover
    'Dataset': type('MockDataset', (object,), { # pragma: no cover
        'range': lambda n: type('MockDatasetInstance', (object,), { # pragma: no cover
            'apply': lambda self, fn: fn(self) # pragma: no cover
        })() # pragma: no cover
    }), # pragma: no cover
    'make_one_shot_iterator': lambda dataset: type('MockIterator', (object,), { # pragma: no cover
        'get_next': lambda: tf.constant(0), # pragma: no cover
        'get_next_as_optional': lambda: type('MockOptional', (object,), { # pragma: no cover
            'get_value': lambda: tf.constant(0), # pragma: no cover
            'has_value': lambda: tf.constant(True) # pragma: no cover
        })() # pragma: no cover
    })() # pragma: no cover
}) # pragma: no cover
prefetching_ops = type('Mock', (object,), {'prefetch_to_device': lambda device: lambda dataset: dataset}) # pragma: no cover
ops = type('Mock', (object,), {'colocate_with': lambda x: (lambda fn: fn)}) # pragma: no cover
test_ops = type('Mock', (object,), {'device_placement_op': lambda: b'GPU:0'}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/placement_test.py
from l3.Runtime import _l_
self.skipTest("TODO(b/169429285): tf.data.Dataset.make_one_shot_iterator "
              "does not support GPU placement.")
_l_(21227)

dataset = dataset_ops.Dataset.range(10)
_l_(21228)
dataset = dataset.apply(prefetching_ops.prefetch_to_device("/gpu:0"))
_l_(21229)
iterator = dataset_ops.make_one_shot_iterator(dataset)
_l_(21230)
data = iterator.get_next()
_l_(21231)
optional_data = iterator.get_next_as_optional()
_l_(21232)

with ops.colocate_with(dataset._variant_tensor):
    _l_(21234)

    dataset_device = test_ops.device_placement_op()
    _l_(21233)
self.assertIn(b"GPU:0", self.evaluate(dataset_device))
_l_(21235)

with ops.colocate_with(iterator._iterator_resource):
    _l_(21237)

    iterator_device = test_ops.device_placement_op()
    _l_(21236)
self.assertIn(b"GPU:0", self.evaluate(iterator_device))
_l_(21238)

with ops.colocate_with(data):
    _l_(21240)

    data_device = test_ops.device_placement_op()
    _l_(21239)
self.assertIn(b"GPU:0", self.evaluate(data_device))
_l_(21241)

with ops.colocate_with(optional_data.get_value()):
    _l_(21243)

    get_value_device = test_ops.device_placement_op()
    _l_(21242)
self.assertIn(b"GPU:0", self.evaluate(get_value_device))
_l_(21244)

with ops.colocate_with(optional_data.has_value()):
    _l_(21246)

    has_value_device = test_ops.device_placement_op()
    _l_(21245)
self.assertIn(b"GPU:0", self.evaluate(has_value_device))
_l_(21247)
