class MockTest: # pragma: no cover
    def skipTest(self, message): # pragma: no cover
        pass # pragma: no cover
    def assertIn(self, a, b): # pragma: no cover
        assert a in b # pragma: no cover
    def evaluate(self, tensor): # pragma: no cover
        with tf.compat.v1.Session() as sess: # pragma: no cover
            return sess.run(tensor) # pragma: no cover
self = MockTest() # pragma: no cover
class MockOptional: # pragma: no cover
    def get_value(self): # pragma: no cover
        return tf.constant(0) # pragma: no cover
    def has_value(self): # pragma: no cover
        return tf.constant(True) # pragma: no cover
optional_data = MockOptional() # pragma: no cover

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
