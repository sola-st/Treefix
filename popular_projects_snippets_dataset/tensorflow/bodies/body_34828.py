# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
table = self._create_table()
value = variables.Variable([1.0] * 32)
insert = table.insert(list(range(32)), value)
size = table.size()
with session.Session() as sess:
    sess.run(value.initializer)
    self.run_op_benchmark(sess, insert, burn_iters=10, min_iters=1000)
    assert sess.run(size) == 32
