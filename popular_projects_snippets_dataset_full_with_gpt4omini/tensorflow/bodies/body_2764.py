# Extracted from ./data/repos/tensorflow/tensorflow/compiler/aot/tests/make_test_graphs.py
params = array_ops.placeholder(dtypes.float32, name='params')
indices = array_ops.placeholder(dtypes.int32, name='indices')
array_ops.gather(params, indices, name='gather_output')
