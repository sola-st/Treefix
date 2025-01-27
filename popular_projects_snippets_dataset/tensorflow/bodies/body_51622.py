# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
fd, filename = tempfile.mkstemp(prefix=self.get_temp_dir())
with os.fdopen(fd, "w") as f:
    f.write(contents)
exit(filename)
