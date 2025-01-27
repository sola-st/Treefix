# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_segment_op_test.py
rt = ragged_factory_ops.constant([
    [[111, 112, 113, 114], [121],],  # row 0
    [],                              # row 1
    [[], [321, 322], [331]],         # row 2
    [[411, 412]]                     # row 3
])  # pyformat: disable
segment_ids1 = [0, 2, 2, 2]
segmented1 = ragged_math_ops.segment_sum(rt, segment_ids1, 3)
expected1 = [[[111, 112, 113, 114], [121]],     # row 0
             [],                                # row 1
             [[411, 412], [321, 322], [331]]    # row 2
            ]  # pyformat: disable
self.assertAllEqual(segmented1, expected1)

segment_ids2 = [1, 2, 1, 1]
segmented2 = ragged_math_ops.segment_sum(rt, segment_ids2, 3)
expected2 = [[],
             [[111+411, 112+412, 113, 114], [121+321, 322], [331]],
             []]  # pyformat: disable
self.assertAllEqual(segmented2, expected2)
