# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/conditional_accumulator_test.py
with self.cached_session():
    q = data_flow_ops.ConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=(3, 2))
    elems = [[[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]],
             [[10.0, 20.0], [30.0, 40.0], [50.0, 60.0]]]
    elems_ave = [[(a + b) / len(elems) for a, b in zip(x, y)]
                 for x, y in zip(elems[0], elems[1])]
    accum_ops = [q.apply_grad(x) for x in elems]
    takeg_t = q.take_grad(1)

    for accum_op in accum_ops:
        accum_op.run()

    is_all_equal = True
    val = self.evaluate(takeg_t)
    for i in range(len(val)):
        for j in range(len(val[i])):
            is_all_equal &= (val[i][j] == elems_ave[i][j])
    self.assertTrue(is_all_equal)
