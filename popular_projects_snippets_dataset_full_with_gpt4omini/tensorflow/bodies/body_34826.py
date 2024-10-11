# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
table = self._create_table()
value = variables.Variable(1.0)
insert = table.insert(0, value)
size = table.size()
with session.Session() as sess:
    sess.run(value.initializer)
    self.run_op_benchmark(sess, insert, burn_iters=10, min_iters=10000)
    assert sess.run(size) == 1
