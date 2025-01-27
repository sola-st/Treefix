# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
results = self._generate_dump_from_simple_addition_graph()

self.assertEqual(results.u.op.type,
                 results.dump.node_op_type(results.u_name))
self.assertIn(results.v.op.type, results.dump.node_op_type(results.v_name))
self.assertIn(results.w.op.type, results.dump.node_op_type(results.w_name))

with self.assertRaisesRegexp(
    ValueError, r"None of the .* device\(s\) has a node named "):
    results.dump.node_op_type("foo_bar")
