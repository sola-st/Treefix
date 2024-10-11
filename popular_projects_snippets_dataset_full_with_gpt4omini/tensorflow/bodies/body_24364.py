# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_utils_test.py
# Create an unrelated source file.
fd, unrelated_source_path = tempfile.mkstemp()
with open(fd, "wt") as source_file:
    source_file.write("print('hello, world')\n")

self.assertEqual({},
                 source_utils.annotate_source(self.dump,
                                              unrelated_source_path))

# Clean up unrelated source file.
os.remove(unrelated_source_path)
