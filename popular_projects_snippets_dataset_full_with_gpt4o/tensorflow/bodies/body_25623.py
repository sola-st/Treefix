# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
screen_output = debugger_cli_common.RichTextLines(
    ["Roses are red", "Violets are blue"],
    font_attr_segs={0: [(0, 5, "red")],
                    1: [(0, 7, "blue")]})

file_path = os.path.join(tempfile.mkdtemp(), "foo", "bar.txt")
with self.assertRaises(Exception):
    screen_output.write_to_file(file_path)
