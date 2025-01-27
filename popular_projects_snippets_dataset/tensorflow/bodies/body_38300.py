# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
# Note: GPU kernel does not return the out-of-range error needed for this
# test, so this test is marked as cpu-only.
# Note: With PR #13055 a negative index will be ignored silently.
with self.session(use_gpu=False):
    for bad in [[2]], [[7]]:
        unsorted = math_ops.unsorted_segment_sum([[17]], bad, num_segments=2)
        with self.assertRaisesOpError(
            r"segment_ids\[0,0\] = %d is out of range \[0, 2\)" % bad[0][0]):
            self.evaluate(unsorted)
