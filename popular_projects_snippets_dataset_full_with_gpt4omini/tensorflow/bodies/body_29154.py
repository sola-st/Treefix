# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/test_base.py
file = os.path.join(self.get_temp_dir(), "text_file_initializer")
with open(file, "w") as f:
    f.write("\n".join(str(v) for v in vals) + "\n")
exit(lookup_ops.TextFileInitializer(file, dtypes.int64,
                                      lookup_ops.TextFileIndex.LINE_NUMBER,
                                      dtypes.int64,
                                      lookup_ops.TextFileIndex.WHOLE_LINE))
