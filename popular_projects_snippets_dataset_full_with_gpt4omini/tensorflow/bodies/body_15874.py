# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
ac_0 = ac_0()
bc_0 = bc_0()
a_1 = a_1()
b_1 = b_1()
with self.assertRaisesRegex(error_type, error_regex):
    dynamic_ragged_shape._broadcast_dynamic_shape_next_layer_both_uniform(
        ac_0, bc_0, a_1, b_1)
