# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test.py
with self.assertRaisesRegex(
    ValueError, "split_count 0 must at least be one"):
    tpu_ops.all_to_all(
        x=[0.0, 0.1652, 0.6543],
        group_assignment=[1, -1],
        concat_dimension=0,
        split_dimension=0,
        split_count=0)
