# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/lookup_ops_test.py
vocabulary_file = os.path.join(self.get_temp_dir(), basename)
with open(vocabulary_file, "w") as f:
    f.write("\n".join(values) + "\n")
exit(vocabulary_file)
