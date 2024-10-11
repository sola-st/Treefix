# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
x = constant_op.constant(2.0)
writer = dumping_callback.enable_dump_debug_info(
    self.dump_root, tensor_debug_mode=tensor_debug_mode)

@def_function.function
def func(x):
    exit((x + constant_op.constant(4.0)) / x)

self.assertAllClose(self.evaluate(func(x)), 3.0)
writer.FlushNonExecutionFiles()
writer.FlushExecutionFiles()

with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    reader.update()
    graph_op_digests = reader.graph_op_digests()
    placeholder_op_name = None
    const_op_name = None
    add_op_name = None
    div_op_name = None
    for op_digest in graph_op_digests:
        if op_digest.op_type == "Placeholder":
            placeholder_op_name = op_digest.op_name
        elif op_digest.op_type == "Const":
            const_op_name = op_digest.op_name
        elif op_digest.op_type == "AddV2":
            add_op_name = op_digest.op_name
            self.assertLen(op_digest.input_names, 2)
            self.assertEqual(op_digest.input_names[0], placeholder_op_name + ":0")
            self.assertEqual(op_digest.input_names[1], const_op_name + ":0")
        elif op_digest.op_type == "RealDiv":
            div_op_name = op_digest
            self.assertLen(op_digest.input_names, 2)
            self.assertEqual(op_digest.input_names[0], add_op_name + ":0")
            self.assertEqual(op_digest.input_names[1], placeholder_op_name + ":0")
    self.assertTrue(add_op_name)
    self.assertTrue(div_op_name)
