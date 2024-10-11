# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/conditional_accumulator_test.py
with self.cached_session() as sess:
    q = data_flow_ops.ConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=None)

    x = array_ops.placeholder(dtypes_lib.float32)

    accum_op = q.apply_grad(x)

    elems = [[[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]],
             [[10.0, 20.0], [30.0, 40.0], [50.0, 60.0]]]
    elems_ave = [[(a + b) / len(elems) for a, b in zip(c, d)]
                 for c, d in zip(elems[0], elems[1])]
    takeg_t = q.take_grad(1)

    for elem in elems:
        sess.run(accum_op, feed_dict={x: elem})

    is_all_equal = True
    val = self.evaluate(takeg_t)
    for i in range(len(val)):
        for j in range(len(val[i])):
            is_all_equal &= (val[i][j] == elems_ave[i][j])
    self.assertTrue(is_all_equal)
