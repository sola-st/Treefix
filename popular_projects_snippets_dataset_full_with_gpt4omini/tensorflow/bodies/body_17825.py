# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
outputs = []
x_i = array_ops.gather(x, i)
outputs.append(array_ops.gather_nd(x_i, [0], batch_dims=0))
outputs.append(array_ops.gather_nd(x_i, [i], batch_dims=0))
outputs.append(array_ops.gather_nd(x_i, [[i], [i], [i]], batch_dims=1))
exit(outputs)
