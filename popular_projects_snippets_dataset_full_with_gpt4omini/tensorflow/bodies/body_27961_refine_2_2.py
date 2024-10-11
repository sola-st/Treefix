import numpy as np # pragma: no cover

self = type('MockSelf', (), {'skipTest': lambda self, msg: print(msg), 'assertIn': lambda self, member, container: print(f'{member in container}'), 'evaluate': lambda self, x: x})() # pragma: no cover
prefetching_ops = type('MockPrefetchingOps', (), {'prefetch_to_device': lambda device: tf.data.experimental.prefetch_to_device(device)})() # pragma: no cover
ops = type('MockOps', (), {'colocate_with': lambda tensor: lambda op: print(f'Colocating with {tensor} and running {op}')})() # pragma: no cover
test_ops = type('MockTestOps', (), {'device_placement_op': lambda: tf.constant(b'/gpu:0')})() # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.skipTest = lambda msg: print(msg) # pragma: no cover
self.assertIn = lambda member, container: print(f'{member in container}') # pragma: no cover
self.evaluate = lambda x: x.numpy() if hasattr(x, 'numpy') else x # pragma: no cover
class MockDataset:# pragma: no cover
    @classmethod# pragma: no cover
    def range(cls, n):# pragma: no cover
        return tf.data.Dataset.from_tensor_slices(list(range(n)))# pragma: no cover
    @staticmethod# pragma: no cover
    def make_one_shot_iterator(dataset):# pragma: no cover
        return dataset._as_variant_tensor.__iter__()# pragma: no cover
# pragma: no cover
dataset_ops = type('DatasetOps', (object,), {'Dataset': MockDataset})() # pragma: no cover
class MockPrefetching:# pragma: no cover
    @staticmethod# pragma: no cover
    def prefetch_to_device(device):# pragma: no cover
        return lambda dataset: dataset.prefetch(1)# pragma: no cover
prefetching_ops = MockPrefetching() # pragma: no cover
class MockOps:# pragma: no cover
    @staticmethod# pragma: no cover
    def colocate_with(tensor):# pragma: no cover
        return lambda op: op# pragma: no cover
ops = MockOps() # pragma: no cover
class MockTestOps:# pragma: no cover
    @staticmethod# pragma: no cover
    def device_placement_op():# pragma: no cover
        return tf.constant(b'/gpu:0')# pragma: no cover
test_ops = MockTestOps() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/placement_test.py
from l3.Runtime import _l_
self.skipTest("TODO(b/169429285): tf.data.Dataset.make_one_shot_iterator "
              "does not support GPU placement.")
_l_(8106)

dataset = dataset_ops.Dataset.range(10)
_l_(8107)
dataset = dataset.apply(prefetching_ops.prefetch_to_device("/gpu:0"))
_l_(8108)
iterator = dataset_ops.make_one_shot_iterator(dataset)
_l_(8109)
data = iterator.get_next()
_l_(8110)
optional_data = iterator.get_next_as_optional()
_l_(8111)

with ops.colocate_with(dataset._variant_tensor):
    _l_(8113)

    dataset_device = test_ops.device_placement_op()
    _l_(8112)
self.assertIn(b"GPU:0", self.evaluate(dataset_device))
_l_(8114)

with ops.colocate_with(iterator._iterator_resource):
    _l_(8116)

    iterator_device = test_ops.device_placement_op()
    _l_(8115)
self.assertIn(b"GPU:0", self.evaluate(iterator_device))
_l_(8117)

with ops.colocate_with(data):
    _l_(8119)

    data_device = test_ops.device_placement_op()
    _l_(8118)
self.assertIn(b"GPU:0", self.evaluate(data_device))
_l_(8120)

with ops.colocate_with(optional_data.get_value()):
    _l_(8122)

    get_value_device = test_ops.device_placement_op()
    _l_(8121)
self.assertIn(b"GPU:0", self.evaluate(get_value_device))
_l_(8123)

with ops.colocate_with(optional_data.has_value()):
    _l_(8125)

    has_value_device = test_ops.device_placement_op()
    _l_(8124)
self.assertIn(b"GPU:0", self.evaluate(has_value_device))
_l_(8126)
