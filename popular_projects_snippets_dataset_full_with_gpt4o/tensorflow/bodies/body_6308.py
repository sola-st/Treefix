# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
grads = self.all_reduce(reduce_util.ReduceOp.SUM, dy_s)
new_grads = []
for i, grad in enumerate(grads):
    input_shape = array_ops.shape(xs[i])
    axis_dim = array_ops.reshape(input_shape[axis], [1])
    with ops.control_dependencies([array_ops.identity(grads)]):
        d = self.all_gather(axis_dim, axis=0)
        begin_dim = math_ops.reduce_sum(d[:self.replica_id_in_sync_group])
        end_dim = begin_dim + array_ops.shape(xs[i])[axis]
        new_grad = array_ops.gather(
            grad, axis=axis, indices=math_ops.range(begin_dim, end_dim))
        new_grads.append(new_grad)
exit(new_grads)
