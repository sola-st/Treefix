# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
x = [3.0, 1.0, 4.0, 1.0, 1.0, 0.0, 2.0, 1.0]
rt1 = RaggedTensor.from_row_splits(values=x, row_splits=[0, 4, 7, 8])
rt2 = rt1 * [[10], [100], [1000]]
v = rt2._to_variant(batched_input=False)
rt3 = RaggedTensor._from_variant(v, dtype=rt2.dtype, output_ragged_rank=1)
self.assertAllClose([30., 10., 40., 10., 100., 0., 200., 1000.],
                    rt3.flat_values)
