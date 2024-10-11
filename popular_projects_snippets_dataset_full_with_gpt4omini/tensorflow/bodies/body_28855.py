# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py

def _build_graph(start, stop, num_epochs):
    iterator = dataset_ops.make_initializable_iterator(
        dataset_ops.Dataset.range(start, stop).repeat(num_epochs))
    init_op = iterator.initializer
    get_next = iterator.get_next()
    save_op = self._save_op(iterator._iterator_resource)
    restore_op = self._restore_op(iterator._iterator_resource)
    exit((init_op, get_next, save_op, restore_op))

start = 2
stop = 10
num_epochs = 5
break_range = 5
break_epoch = 3
with ops.Graph().as_default() as g:
    init_op, get_next, save_op, restore_op = _build_graph(
        start, stop, num_epochs)
    with self.session(graph=g) as sess:
        sess.run(variables.global_variables_initializer())
        sess.run(init_op)
        # Note: There is no checkpoint saved currently so a NotFoundError is
        # raised.
        with self.assertRaises(errors.NotFoundError):
            sess.run(init_op)
            sess.run(restore_op)
        for _ in range(break_epoch - 1):
            for i in range(start, stop):
                self.assertEqual(i, sess.run(get_next))
        for i in range(start, break_range):
            self.assertEqual(i, sess.run(get_next))
        sess.run(save_op)

with ops.Graph().as_default() as g:
    init_op, get_next, _, restore_op = _build_graph(start, stop, num_epochs)
    with self.session(graph=g) as sess:
        sess.run(init_op)
        sess.run(restore_op)
        for i in range(break_range, stop):
            self.assertEqual(i, sess.run(get_next))
        for _ in range(break_epoch, num_epochs):
            for i in range(start, stop):
                self.assertEqual(i, sess.run(get_next))
        with self.assertRaises(errors.OutOfRangeError):
            sess.run(get_next)
