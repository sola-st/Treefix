# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/from_list_test.py
elements = [(np.tile(np.array([[0], [1]], dtype=np.uint8), 2),
             np.tile(np.array([[2], [256]], dtype=np.uint16), 2),
             np.tile(np.array([[4], [65536]], dtype=np.uint32), 2),
             np.tile(np.array([[8], [4294967296]], dtype=np.uint64), 2))]
dataset = from_list.from_list(elements)
self.assertEqual(
    (dtypes.uint8, dtypes.uint16, dtypes.uint32, dtypes.uint64),
    dataset_ops.get_legacy_output_types(dataset))
self.assertDatasetProduces(dataset, elements)
