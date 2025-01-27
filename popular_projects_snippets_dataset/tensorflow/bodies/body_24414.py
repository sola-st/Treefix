# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
"""Watch an output slot not emitting any edges.

    (Not even control edges from the node.)
    """

with session.Session() as sess:
    x_init = constant_op.constant([2, 2, 3, 5, 5])
    x = variables.VariableV1(x_init, name="unconnected/x")

    # The UniqueOp (tf.unique) has two output slots. Use only slot 0 in the
    # graph. Let the debugger watch the unused slot 1.
    unique_x, _ = array_ops.unique(x, name="unconnected/unique_x")
    y = math_ops.add(unique_x, [0, 1, 2], name="unconnected/y")

    x.initializer.run()

    # Verify that only slot 0 of unique_x has recipients, while slot 1 of the
    # same node does not have recipients.
    unique_x_slot_0_recipients = []
    unique_x_slot_1_recipients = []
    for op in sess.graph.get_operations():
        for inp in op.inputs:
            if inp.name == "unconnected/unique_x:0":
                unique_x_slot_0_recipients.append(op.name)
            elif inp.name == "unconnected/unique_x:1":
                unique_x_slot_1_recipients.append(op.name)

    self.assertEqual(["unconnected/y"], unique_x_slot_0_recipients)
    self.assertEqual([], unique_x_slot_1_recipients)

    y_result, dump = self._debug_run_and_get_dump(sess, y)
    self.assertAllClose([2, 4, 7], y_result)

    # Assert that the connected slot (slot 0) is dumped properly.
    unique_x_slot_0_dumps = dump.watch_key_to_data(
        "unconnected/unique_x:0:DebugIdentity")
    self.assertEqual(1, len(unique_x_slot_0_dumps))
    self.assertEqual("unconnected/unique_x",
                     unique_x_slot_0_dumps[0].node_name)
    self.assertEqual(0, unique_x_slot_0_dumps[0].output_slot)
    self.assertAllClose([2, 3, 5], unique_x_slot_0_dumps[0].get_tensor())

    # Assert that the unconnected slot (slot 1) is dumped properly.
    unique_x_slot_1_dumps = dump.watch_key_to_data(
        "unconnected/unique_x:1:DebugIdentity")
    self.assertEqual(1, len(unique_x_slot_1_dumps))
    self.assertEqual("unconnected/unique_x",
                     unique_x_slot_1_dumps[0].node_name)
    self.assertEqual(1, unique_x_slot_1_dumps[0].output_slot)
    self.assertAllClose([0, 0, 1, 2, 2],
                        unique_x_slot_1_dumps[0].get_tensor())
