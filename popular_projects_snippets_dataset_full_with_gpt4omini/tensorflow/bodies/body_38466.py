# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/confusion_matrix_test.py
with self.cached_session() as sess:
    m_neg = array_ops.placeholder(dtype=dtypes.float32)
    m_pos = array_ops.placeholder(dtype=dtypes.float32)
    s = array_ops.placeholder(dtype=dtypes.float32)

    neg = random_ops.random_normal(
        [20], mean=m_neg, stddev=s, dtype=dtypes.float32)
    pos = random_ops.random_normal(
        [20], mean=m_pos, stddev=s, dtype=dtypes.float32)

    data = array_ops.concat([neg, pos], 0)
    data = math_ops.cast(math_ops.round(data), tf_dtype)
    data = math_ops.minimum(math_ops.maximum(data, 0), 1)
    lab = array_ops.concat(
        [
            array_ops.zeros(
                [20], dtype=tf_dtype), array_ops.ones(
                    [20], dtype=tf_dtype)
        ],
        0)

    cm = confusion_matrix.confusion_matrix(
        lab, data, dtype=tf_dtype, num_classes=2)

    d, l, cm_out = sess.run([data, lab, cm], {m_neg: 0.0, m_pos: 1.0, s: 1.0})

    truth = np.zeros([2, 2], dtype=np_dtype)
    for i in range(len(d)):
        truth[l[i], d[i]] += 1

    self.assertEqual(cm_out.dtype, np_dtype)
    self.assertAllClose(cm_out, truth, atol=1e-10)
