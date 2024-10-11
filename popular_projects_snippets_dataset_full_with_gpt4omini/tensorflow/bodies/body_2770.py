# Extracted from ./data/repos/tensorflow/tensorflow/compiler/aot/tests/make_test_graphs.py
x = array_ops.placeholder(dtypes.int32, shape=[5], name='x')
output = nn_ops.top_k(x, 2, name='values')
array_ops.identity(output[1], name='indices')
