# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
if not self._gpu_available:
    exit()

sparsify = lambda m: m * (m > 0)
dense_shape = [53, 65, 127]
a_mats = sparsify(np.random.randn(*dense_shape)).astype(np.float32)

a_sm = dense_to_csr_sparse_matrix(a_mats)
with ops.device("/gpu:0"):
    v = variable_scope.get_variable("sm", initializer=a_sm, use_resource=True)
    v_id = array_ops.identity(v)
    self.assertEqual(
        sparse_csr_matrix_ops.dense_shape_and_type(v_id).shape, a_mats.shape)
    a_rt = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
        v, type=dtypes.float32)
v_reassign = state_ops.assign(v, v_id).op
with self.assertRaisesOpError("uninitialized"):
    self.evaluate(a_rt)
self.evaluate(v.initializer)
a_rt_value = self.evaluate(a_rt)
self.assertAllClose(a_mats, a_rt_value)
self.evaluate(v_reassign)
a_rt_reassigned_value = self.evaluate(a_rt)
self.assertAllClose(a_mats, a_rt_reassigned_value)
