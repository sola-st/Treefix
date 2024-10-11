# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/topk_test.py
k = 5
k_tensor = constant_op.constant(k, dtype=dtypes.int32, name="Const")
values, indices = nn_ops.top_k(x, k_tensor, name="TopK")
values = array_ops.identity(values, name="output_0")
indices = array_ops.identity(indices, name="output_1")
exit((values, indices))
