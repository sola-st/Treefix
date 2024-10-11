# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
with session.Session() as sess:
    loop_body = lambda i: math_ops.add(i, 2)
    loop_cond = lambda i: math_ops.less(i, 16)

    i = constant_op.constant(10, name="i")
    loop = control_flow_ops.while_loop(loop_cond, loop_body, [i])

    loop_result, dump = self._debug_run_and_get_dump(sess, loop)
    self.assertEqual(16, loop_result)

    self.assertEqual(
        [[10]], dump.get_tensors("while/Enter", 0, "DebugIdentity"))
    self.assertEqual(
        [[12], [14], [16]],
        dump.get_tensors("while/NextIteration", 0, "DebugIdentity"))
