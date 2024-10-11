# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
"""Check RichTextLines output for list_tensors commands.

  Args:
    tst: A test_util.TensorFlowTestCase instance.
    out: The RichTextLines object to be checked.
    expected_tensor_names: (list of str) Expected tensor names in the list.
    expected_op_types: (list of str) Expected op types of the tensors, in the
      same order as the expected_tensor_names.
    node_name_regex: Optional: node name regex filter.
    op_type_regex: Optional: op type regex filter.
    tensor_filter_name: Optional: name of the tensor filter.
    sort_by: (str) (timestamp | op_type | tensor_name) the field by which the
      tensors in the list are sorted.
    reverse: (bool) whether the sorting is in reverse (i.e., descending) order.
  """

line_iter = iter(out.lines)
attr_segs = out.font_attr_segs
line_counter = 0

num_dumped_tensors = int(next(line_iter).split(" ")[0])
line_counter += 1
tst.assertGreaterEqual(num_dumped_tensors, len(expected_tensor_names))

if op_type_regex is not None:
    tst.assertEqual("Op type regex filter: \"%s\"" % op_type_regex,
                    next(line_iter))
    line_counter += 1

if node_name_regex is not None:
    tst.assertEqual("Node name regex filter: \"%s\"" % node_name_regex,
                    next(line_iter))
    line_counter += 1

tst.assertEqual("", next(line_iter))
line_counter += 1

# Verify the column heads "t (ms)", "Op type" and "Tensor name" are present.
line = next(line_iter)
tst.assertIn("t (ms)", line)
tst.assertIn("Op type", line)
tst.assertIn("Tensor name", line)

# Verify the command shortcuts in the top row.
attr_segs = out.font_attr_segs[line_counter]
attr_seg = attr_segs[0]
tst.assertEqual(0, attr_seg[0])
tst.assertEqual(len("t (ms)"), attr_seg[1])
command = attr_seg[2][0].content
tst.assertIn("-s timestamp", command)
assert_column_header_command_shortcut(
    tst, command, reverse, node_name_regex, op_type_regex,
    tensor_filter_name)
tst.assertEqual("bold", attr_seg[2][1])

idx0 = line.index("Size")
attr_seg = attr_segs[1]
tst.assertEqual(idx0, attr_seg[0])
tst.assertEqual(idx0 + len("Size (B)"), attr_seg[1])
command = attr_seg[2][0].content
tst.assertIn("-s dump_size", command)
assert_column_header_command_shortcut(tst, command, reverse, node_name_regex,
                                      op_type_regex, tensor_filter_name)
tst.assertEqual("bold", attr_seg[2][1])

idx0 = line.index("Op type")
attr_seg = attr_segs[2]
tst.assertEqual(idx0, attr_seg[0])
tst.assertEqual(idx0 + len("Op type"), attr_seg[1])
command = attr_seg[2][0].content
tst.assertIn("-s op_type", command)
assert_column_header_command_shortcut(
    tst, command, reverse, node_name_regex, op_type_regex,
    tensor_filter_name)
tst.assertEqual("bold", attr_seg[2][1])

idx0 = line.index("Tensor name")
attr_seg = attr_segs[3]
tst.assertEqual(idx0, attr_seg[0])
tst.assertEqual(idx0 + len("Tensor name"), attr_seg[1])
command = attr_seg[2][0].content
tst.assertIn("-s tensor_name", command)
assert_column_header_command_shortcut(
    tst, command, reverse, node_name_regex, op_type_regex,
    tensor_filter_name)
tst.assertEqual("bold", attr_seg[2][1])

# Verify the listed tensors and their timestamps.
tensor_timestamps = []
dump_sizes_bytes = []
op_types = []
tensor_names = []
for line in line_iter:
    items = line.split(" ")
    items = [item for item in items if item]

    rel_time = float(items[0][1:-1])
    tst.assertGreaterEqual(rel_time, 0.0)

    tensor_timestamps.append(rel_time)
    dump_sizes_bytes.append(command_parser.parse_readable_size_str(items[1]))
    op_types.append(items[2])
    tensor_names.append(items[3])

# Verify that the tensors should be listed in ascending order of their
# timestamps.
if sort_by == "timestamp":
    sorted_timestamps = sorted(tensor_timestamps)
    if reverse:
        sorted_timestamps.reverse()
    tst.assertEqual(sorted_timestamps, tensor_timestamps)
elif sort_by == "dump_size":
    sorted_dump_sizes_bytes = sorted(dump_sizes_bytes)
    if reverse:
        sorted_dump_sizes_bytes.reverse()
    tst.assertEqual(sorted_dump_sizes_bytes, dump_sizes_bytes)
elif sort_by == "op_type":
    sorted_op_types = sorted(op_types)
    if reverse:
        sorted_op_types.reverse()
    tst.assertEqual(sorted_op_types, op_types)
elif sort_by == "tensor_name":
    sorted_tensor_names = sorted(tensor_names)
    if reverse:
        sorted_tensor_names.reverse()
    tst.assertEqual(sorted_tensor_names, tensor_names)
else:
    tst.fail("Invalid value in sort_by: %s" % sort_by)

# Verify that the tensors are all listed.
for tensor_name, op_type in zip(expected_tensor_names, expected_op_types):
    tst.assertIn(tensor_name, tensor_names)
    index = tensor_names.index(tensor_name)
    tst.assertEqual(op_type, op_types[index])
