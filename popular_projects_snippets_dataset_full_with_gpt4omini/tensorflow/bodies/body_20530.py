# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test.py
with self.assertRaisesRegex(
    ValueError, "input dimension 3 not divisible by split_count 2"):
    tpu_ops.all_to_all(
        x=[[0.0], [0.1652], [0.6543]],
        group_assignment=[[0, 1], [2, 3]],
        concat_dimension=1,
        split_dimension=0,
        split_count=2)
