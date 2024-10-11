# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce_test.py
# 1 worker, 1 device
input_tensors, device_names = self._buildInput(1, 1)
pred_by_c_d, rank_by_c_d = ar._ring_permutations(1, 1, [0])
output_tensors = ar._build_ring_gather(input_tensors, device_names, 1,
                                       pred_by_c_d, rank_by_c_d,
                                       math_ops.add)
self.assertEqual(output_tensors, input_tensors)
# 1 worker, 4 devices, 2 subchunks
input_tensors, device_names = self._buildInput(1, 4)
pred_by_c_d, rank_by_c_d = ar._ring_permutations(1, 2, [0, 1, 2, 3])
output_tensors, pad_len = ar._build_ring_gather(
    input_tensors, device_names, 2, pred_by_c_d, rank_by_c_d, math_ops.add)
self.assertEqual(0, pad_len)
# same number outputs as inputs
self.assertEqual(len(output_tensors), len(input_tensors))
num_chunks = 2 * len(input_tensors)
tlen = tensor_shape.dimension_value(input_tensors[0].shape[0])
for otl in output_tensors:
    self.assertEqual(len(otl), num_chunks)
    for ot in otl:
        self.assertEqual(ot.shape, [tlen//num_chunks])
