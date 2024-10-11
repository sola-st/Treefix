# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_segment_op_test.py
rt = ragged_factory_ops.constant([
    [[111, 112, 113, 114], [121],],  # row 0
    [],                              # row 1
    [[], [321, 322], [331]],         # row 2
    [[411, 412]]                     # row 3
])  # pyformat: disable
segment_ids = ragged_factory_ops.constant([[1, 2], [], [1, 1, 2], [2]])
segmented = ragged_math_ops.segment_sum(rt, segment_ids, 3)
expected = [[],
            [111+321, 112+322, 113, 114],
            [121+331+411, 412]]  # pyformat: disable
self.assertAllEqual(segmented, expected)
