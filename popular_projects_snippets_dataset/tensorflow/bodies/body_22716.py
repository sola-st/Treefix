# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/jit_test.py
with self.session(graph=ops.Graph()):
    with jit.experimental_jit_scope(True):
        # XlaScope 0
        a1 = constant_op.constant(1)
    with jit.experimental_jit_scope(True):
        # XlaScope 1
        a2 = constant_op.constant(1)
        with jit.experimental_jit_scope(True):
            # XlaScope still 1, depth 1
            a3 = constant_op.constant(1)
            with jit.experimental_jit_scope(True):
                # XlaScope still 1, depth 2
                a4 = constant_op.constant(1)
            # XlaScope still 1, depth 1
            a5 = constant_op.constant(1)
    with jit.experimental_jit_scope(True):
        # XlaScope now 2, depth 0
        a6 = constant_op.constant(1)

self.assertEqual(b"jit_scope_0", a1.op.get_attr("_XlaScope"))
self.assertEqual(b"jit_scope_1", a2.op.get_attr("_XlaScope"))
self.assertEqual(b"jit_scope_1", a3.op.get_attr("_XlaScope"))
self.assertEqual(b"jit_scope_1", a4.op.get_attr("_XlaScope"))
self.assertEqual(b"jit_scope_1", a5.op.get_attr("_XlaScope"))
self.assertEqual(b"jit_scope_2", a6.op.get_attr("_XlaScope"))
