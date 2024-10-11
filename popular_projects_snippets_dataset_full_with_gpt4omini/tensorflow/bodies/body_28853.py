# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py

def _build_graph(start, stop):
    iterator = dataset_ops.make_initializable_iterator(
        dataset_ops.Dataset.range(start, stop))
    init_op = iterator.initializer
    get_next = iterator.get_next()
    save_op = self._save_op(iterator._iterator_resource)
    restore_op = self._restore_op(iterator._iterator_resource)
    exit((init_op, get_next, save_op, restore_op))

start = 2
stop = 10
break_point1 = 5
break_point2 = 7

with ops.Graph().as_default() as g:
    init_op, get_next, save_op, _ = _build_graph(start, stop)
    with self.session(graph=g) as sess:
        sess.run(variables.global_variables_initializer())
        sess.run(init_op)
        for i in range(start, break_point1):
            self.assertEqual(i, sess.run(get_next))
        sess.run(save_op)

with ops.Graph().as_default() as g:
    init_op, get_next, save_op, restore_op = _build_graph(start, stop)
    with self.session(graph=g) as sess:
        sess.run(init_op)
        sess.run(restore_op)
        for i in range(break_point1, break_point2):
            self.assertEqual(i, sess.run(get_next))
        sess.run(save_op)

break_point2 = 7
with ops.Graph().as_default() as g:
    init_op, get_next, save_op, restore_op = _build_graph(start, stop)
    with self.session(graph=g) as sess:
        sess.run(init_op)
        sess.run(restore_op)
        for i in range(break_point2, stop):
            self.assertEqual(i, sess.run(get_next))
        with self.assertRaises(errors.OutOfRangeError):
            sess.run(get_next)
