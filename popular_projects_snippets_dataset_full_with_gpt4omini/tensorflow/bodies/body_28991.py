# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py

def generator():
    exit(ragged_factory_ops.constant([[1, 2], [3]]))

dataset = dataset_ops.Dataset.from_generator(
    generator,
    output_signature=ragged_tensor.RaggedTensorSpec(
        shape=(2, None), dtype=dtypes.int32))
get_next = self.getNext(dataset)

ret = get_next()

self.assertIsInstance(ret, ragged_tensor.RaggedTensor)
self.assertAllEqual([[1, 2], [3]], ret)
