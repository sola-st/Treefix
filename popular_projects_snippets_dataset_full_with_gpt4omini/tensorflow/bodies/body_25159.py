# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
"""Check RichTextLines output for node_info commands.

  Args:
    tst: A test_util.TensorFlowTestCase instance.
    out: The RichTextLines object to be checked.
    node_name: Name of the node.
    op_type: Op type of the node, as a str.
    device: Name of the device on which the node resides.
    input_op_type_node_name_pairs: A list of 2-tuples of op type and node name,
      for the (non-control) inputs to the node.
    ctrl_input_op_type_node_name_pairs: A list of 2-tuples of op type and node
      name, for the control inputs to the node.
    recipient_op_type_node_name_pairs: A list of 2-tuples of op type and node
      name, for the (non-control) output recipients to the node.
    ctrl_recipient_op_type_node_name_pairs: A list of 2-tuples of op type and
      node name, for the control output recipients to the node.
    attr_key_val_pairs: Optional: attribute key-value pairs of the node, as a
      list of 2-tuples.
    num_dumped_tensors: Optional: number of tensor dumps from the node.
    show_stack_trace: (bool) whether the stack trace of the node's
      construction is asserted to be present.
    stack_trace_available: (bool) whether Python stack trace is available.
  """

line_iter = iter(out.lines)

tst.assertEqual("Node %s" % node_name, next(line_iter))
tst.assertEqual("", next(line_iter))
tst.assertEqual("  Op: %s" % op_type, next(line_iter))
tst.assertEqual("  Device: %s" % device, next(line_iter))
tst.assertEqual("", next(line_iter))
tst.assertEqual("  %d input(s) + %d control input(s):" %
                (len(input_op_type_node_name_pairs),
                 len(ctrl_input_op_type_node_name_pairs)), next(line_iter))

# Check inputs.
tst.assertEqual("    %d input(s):" % len(input_op_type_node_name_pairs),
                next(line_iter))
for op_type, node_name in input_op_type_node_name_pairs:
    tst.assertEqual("      [%s] %s" % (op_type, node_name), next(line_iter))

tst.assertEqual("", next(line_iter))

# Check control inputs.
if ctrl_input_op_type_node_name_pairs:
    tst.assertEqual("    %d control input(s):" %
                    len(ctrl_input_op_type_node_name_pairs), next(line_iter))
    for op_type, node_name in ctrl_input_op_type_node_name_pairs:
        tst.assertEqual("      [%s] %s" % (op_type, node_name), next(line_iter))

    tst.assertEqual("", next(line_iter))

tst.assertEqual("  %d recipient(s) + %d control recipient(s):" %
                (len(recipient_op_type_node_name_pairs),
                 len(ctrl_recipient_op_type_node_name_pairs)),
                next(line_iter))

# Check recipients, the order of which is not deterministic.
tst.assertEqual("    %d recipient(s):" %
                len(recipient_op_type_node_name_pairs), next(line_iter))

t_recs = []
for _ in recipient_op_type_node_name_pairs:
    line = next(line_iter)

    op_type, node_name = parse_op_and_node(line)
    t_recs.append((op_type, node_name))

tst.assertItemsEqual(recipient_op_type_node_name_pairs, t_recs)

# Check control recipients, the order of which is not deterministic.
if ctrl_recipient_op_type_node_name_pairs:
    tst.assertEqual("", next(line_iter))

    tst.assertEqual("    %d control recipient(s):" %
                    len(ctrl_recipient_op_type_node_name_pairs),
                    next(line_iter))

    t_ctrl_recs = []
    for _ in ctrl_recipient_op_type_node_name_pairs:
        line = next(line_iter)

        op_type, node_name = parse_op_and_node(line)
        t_ctrl_recs.append((op_type, node_name))

    tst.assertItemsEqual(ctrl_recipient_op_type_node_name_pairs, t_ctrl_recs)

# The order of multiple attributes can be non-deterministic.
if attr_key_val_pairs:
    tst.assertEqual("", next(line_iter))

    tst.assertEqual("Node attributes:", next(line_iter))

    kv_pairs = []
    for key, val in attr_key_val_pairs:
        key = next(line_iter).strip().replace(":", "")

        val = next(line_iter).strip()

        kv_pairs.append((key, val))

        tst.assertEqual("", next(line_iter))

if num_dumped_tensors is not None:
    tst.assertEqual("%d dumped tensor(s):" % num_dumped_tensors,
                    next(line_iter))
    tst.assertEqual("", next(line_iter))

    dump_timestamps_ms = []
    for _ in range(num_dumped_tensors):
        line = next(line_iter)

        tst.assertStartsWith(line.strip(), "Slot 0 @ DebugIdentity @")
        tst.assertTrue(line.strip().endswith(" ms"))

        dump_timestamp_ms = float(line.strip().split(" @ ")[-1].replace("ms", ""))
        tst.assertGreaterEqual(dump_timestamp_ms, 0.0)

        dump_timestamps_ms.append(dump_timestamp_ms)

    tst.assertEqual(sorted(dump_timestamps_ms), dump_timestamps_ms)

if show_stack_trace:
    tst.assertEqual("", next(line_iter))
    tst.assertEqual("", next(line_iter))
    tst.assertEqual("Traceback of node construction:", next(line_iter))
    if stack_trace_available:
        try:
            depth_counter = 0
            while True:
                for i in range(5):
                    line = next(line_iter)
                    if i == 0:
                        tst.assertEqual(depth_counter, int(line.split(":")[0]))
                    elif i == 1:
                        tst.assertStartsWith(line, "  Line:")
                    elif i == 2:
                        tst.assertStartsWith(line, "  Function:")
                    elif i == 3:
                        tst.assertStartsWith(line, "  Text:")
                    elif i == 4:
                        tst.assertEqual("", line)

                depth_counter += 1
        except StopIteration:
            tst.assertEqual(0, i)
    else:
        tst.assertEqual("(Unavailable because no Python graph has been loaded)",
                        next(line_iter))
