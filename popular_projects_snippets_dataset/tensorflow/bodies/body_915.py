# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stack_ops_test.py
h = gen_data_flow_ops.stack_v2(5, dtypes.float32, stack_name="foo")
gen_data_flow_ops.stack_close_v2(h)
