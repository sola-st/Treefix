# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
np_ans = np.conj(cplx)
with test_util.device(use_gpu=use_gpu):
    inx = ops.convert_to_tensor(cplx)
    tf_conj = math_ops.conj(inx)
    tf_ans = self.evaluate(tf_conj)
self.assertAllEqual(np_ans, tf_ans)
self.assertShapeEqual(np_ans, tf_conj)
