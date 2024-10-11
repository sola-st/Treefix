# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/op_selector_test.py
seed_ops = [self.h.op]
# Include all ops except for self.g.op
within_ops = [
    x.op for x in [self.a, self.b, self.c, self.d, self.e, self.f, self.h]
]
# For the fn, exclude self.c.op.
within_ops_fn = lambda op: op not in (self.c.op,)
stop_at_ts = (self.f,)

with self.graph.as_default():
    # Backward walk only includes h since we stop at f and g is not within.
    ops = op_selector.get_backward_walk_ops(
        seed_ops,
        inclusive=True,
        within_ops=within_ops,
        within_ops_fn=within_ops_fn,
        stop_at_ts=stop_at_ts)
    self.assertEqual(set(ops), set([self.h.op]))

    # If we do inclusive=False, the result is empty.
    ops = op_selector.get_backward_walk_ops(
        seed_ops,
        inclusive=False,
        within_ops=within_ops,
        within_ops_fn=within_ops_fn,
        stop_at_ts=stop_at_ts)
    self.assertEqual(set(ops), set())

    # Removing stop_at_fs adds f.op, d.op.
    ops = op_selector.get_backward_walk_ops(
        seed_ops,
        inclusive=True,
        within_ops=within_ops,
        within_ops_fn=within_ops_fn)
    self.assertEqual(set(ops), set([self.d.op, self.f.op, self.h.op]))

    # Not using within_ops_fn adds back ops for a, b, c.
    ops = op_selector.get_backward_walk_ops(
        seed_ops, inclusive=True, within_ops=within_ops)
    self.assertEqual(
        set(ops),
        set([
            self.a.op, self.b.op, self.c.op, self.d.op, self.f.op, self.h.op
        ]))

    # Vanially backward search via self.h.op includes everything except e.op.
    ops = op_selector.get_backward_walk_ops(seed_ops, inclusive=True)
    self.assertEqual(
        set(ops),
        set([
            self.a.op, self.b.op, self.c.op, self.d.op, self.f.op, self.g.op,
            self.h.op
        ]))
