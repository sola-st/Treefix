# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
args, output_path = command_parser.extract_output_file_path(
    ["lp", ">1.2s"])
self.assertEqual(["lp"], args)
self.assertEqual("1.2s", output_path)

args, output_path = command_parser.extract_output_file_path(
    ["lp", "--execution_time", ">x.yms"])
self.assertEqual(["lp", "--execution_time"], args)
self.assertEqual("x.yms", output_path)

args, output_path = command_parser.extract_output_file_path(
    ["lp", "--memory", ">a.1kB"])
self.assertEqual(["lp", "--memory"], args)
self.assertEqual("a.1kB", output_path)

args, output_path = command_parser.extract_output_file_path(
    ["lp", "--memory", ">e002MB"])
self.assertEqual(["lp", "--memory"], args)
self.assertEqual("e002MB", output_path)
