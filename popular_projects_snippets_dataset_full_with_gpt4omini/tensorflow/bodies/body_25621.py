# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
screen_output = debugger_cli_common.RichTextLines(
    ["Roses are red", "Violets are blue"],
    font_attr_segs={0: [(0, 5, "red")],
                    1: [(0, 7, "blue")]})

fd, file_path = tempfile.mkstemp()
os.close(fd)  # file opened exclusively, so we need to close this
# a better fix would be to make the API take a fd
screen_output.write_to_file(file_path)

with gfile.Open(file_path, "r") as f:
    self.assertEqual("Roses are red\nViolets are blue\n", f.read())

# Clean up.
gfile.Remove(file_path)
