# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/approx_topk_test.py
row = np.arange(row_size, dtype=np.float32)
db = np.stack(list(self._rng.permutation(row) for _ in range(num_rows)))
db_op = constant_op.constant(db, dtype=dtype)
out_grads = self._rng.random([num_rows, k])
out_grads_op = constant_op.constant(out_grads, dtype=dtype)

# Must jit-compile to access the xla kernel.
@function(jit_compile=True)
def ann_with_grads(db, out_grads):
    with backprop.GradientTape() as tape:
        tape.watch(db)
        val, idx = nn_ops.approx_max_k(db, k)
    result_in_grads = tape.gradient(val, db, out_grads)
    lifted_k_idx = array_ops.reshape(idx, [num_rows, k, 1])
    iota_idx = array_ops.broadcast_to(
        array_ops.reshape(math_ops.range(num_rows), [num_rows, 1, 1]),
        [num_rows, k, 1])
    lifted_idx = array_ops.concat([iota_idx, lifted_k_idx], axis=2)
    k_idx_s = array_ops.reshape(lifted_idx, [num_rows * k, 2])
    k_gra_s = array_ops.reshape(out_grads, [num_rows * k])
    expected_in_grads = array_ops.scatter_nd(k_idx_s, k_gra_s,
                                             [num_rows, row_size])
    exit([expected_in_grads, result_in_grads])

expected_in_grads, result_in_grads = self.evaluate(
    ann_with_grads(db_op, out_grads_op))
self.assertAllClose(expected_in_grads, result_in_grads)
