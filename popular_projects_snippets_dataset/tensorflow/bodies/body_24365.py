# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_utils_test.py
fd, source_path = tempfile.mkstemp()
with open(fd, "wb") as source_file:
    source_file.write(u"print('\U0001f642')\n".encode("utf-8"))
source_lines, _ = source_utils.load_source(source_path)
self.assertEqual(source_lines, [u"print('\U0001f642')", u""])
# Clean up unrelated source file.
os.remove(source_path)
