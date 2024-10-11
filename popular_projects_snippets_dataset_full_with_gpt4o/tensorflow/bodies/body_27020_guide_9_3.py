import tempfile # pragma: no cover
import os # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
self._test_dir = tempfile.mkdtemp() # pragma: no cover
self.evaluate = lambda x: x.numpy() if ops.is_dense_tensor_like(x) else x # pragma: no cover
self.assertEqual = lambda a, b: (lambda: (_ for _ in ()).throw(AssertionError(f'{a} != {b}')))() if a != b else None # pragma: no cover
def mock_save(dataset, path): # pragma: no cover
    return experimental_save_dataset(dataset._variant_tensor, tf.constant(path), dataset_ops.DatasetSpec(dataset.element_spec)._serialize()) # pragma: no cover
def mock_load(path, element_spec): # pragma: no cover
    return dataset_ops._VariantDataset(experimental_load_dataset(tf.constant(path), tf.constant(element_spec._serialize())), element_spec) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/io_test.py
from l3.Runtime import _l_
dataset = dataset_ops.Dataset.range(42)
_l_(21308)
io.save(dataset, self._test_dir)
_l_(21309)
dataset2 = io.load(self._test_dir, dataset.element_spec)
_l_(21310)
self.assertEqual(self.evaluate(dataset2.cardinality()), 42)
_l_(21311)
