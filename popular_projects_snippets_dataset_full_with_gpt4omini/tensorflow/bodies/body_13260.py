# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
counts = np.ones([1]).astype(np.float32)
mean_ss = np.random.random_sample(shape).astype(np.float32)
variance_ss = np.random.random_sample(shape).astype(np.float32)
variance_ss *= variance_ss
if shift:
    shift_v = np.random.random_sample(shape).astype(np.float32)
else:
    shift_v = None
npm, npv = self._npNormalizeMoments(counts, mean_ss, variance_ss, shift_v)
for use_gpu in [True, False]:
    with self.cached_session(use_gpu=use_gpu) as sess:
        tf_counts = constant_op.constant(counts, name="counts")
        tf_mean_ss = constant_op.constant(mean_ss, name="mean_ss")
        tf_variance_ss = constant_op.constant(variance_ss, name="variance_ss")
        if shift:
            tf_shift_v = constant_op.constant(shift_v, name="shift")
        else:
            tf_shift_v = None
        opm, opv = self._opNormalizeMoments(tf_counts, tf_mean_ss,
                                            tf_variance_ss, tf_shift_v)
        tfm, tfv = self.evaluate([opm, opv])
        self.assertAllClose(npm, tfm, atol=0.000001)
        self.assertAllClose(npv, tfv, atol=0.000001)
