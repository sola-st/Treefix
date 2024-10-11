# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
args, output_path = command_parser.extract_output_file_path(
    ["lp", "--execution_time=>100ms"])
self.assertEqual(["lp", "--execution_time=>100ms"], args)
self.assertIsNone(output_path)

args, output_path = command_parser.extract_output_file_path(
    ["lp", "--execution_time", ">1.2s"])
self.assertEqual(["lp", "--execution_time", ">1.2s"], args)
self.assertIsNone(output_path)

args, output_path = command_parser.extract_output_file_path(
    ["lp", "-e", ">1200"])
self.assertEqual(["lp", "-e", ">1200"], args)
self.assertIsNone(output_path)

args, output_path = command_parser.extract_output_file_path(
    ["lp", "--foo_value", ">-.2MB"])
self.assertEqual(["lp", "--foo_value", ">-.2MB"], args)
self.assertIsNone(output_path)

args, output_path = command_parser.extract_output_file_path(
    ["lp", "--bar_value", ">-42e3GB"])
self.assertEqual(["lp", "--bar_value", ">-42e3GB"], args)
self.assertIsNone(output_path)

args, output_path = command_parser.extract_output_file_path(
    ["lp", "--execution_time", ">=100ms"])
self.assertEqual(["lp", "--execution_time", ">=100ms"], args)
self.assertIsNone(output_path)

args, output_path = command_parser.extract_output_file_path(
    ["lp", "--execution_time=>=100ms"])
self.assertEqual(["lp", "--execution_time=>=100ms"], args)
self.assertIsNone(output_path)
