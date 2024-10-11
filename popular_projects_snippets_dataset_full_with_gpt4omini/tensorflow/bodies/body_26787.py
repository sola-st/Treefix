# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/make_deterministic_test.py
path = os.path.join(self.get_temp_dir(), filename)
with open(path, "w") as f:
    f.write("\n".join(str(n) for n in numbers))
exit(path)
