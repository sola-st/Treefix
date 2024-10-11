# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
table = self._create_table()
c = dataset_ops.make_one_shot_iterator(counter.Counter()).get_next()
value = variables.Variable([1.0] * 32)
insert = table.insert(32 * c + list(range(32)), value)
size = table.size()
with session.Session() as sess:
    sess.run(value.initializer)
    self.run_op_benchmark(sess, insert, burn_iters=10, min_iters=1000)
    assert sess.run(size) >= 1000 * 32
