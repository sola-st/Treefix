# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
with self.assertRaisesRegex(SyntaxError, "Redirect file path is empty"):
    command_parser.extract_output_file_path(
        ["pt", "a:0", ">"])
