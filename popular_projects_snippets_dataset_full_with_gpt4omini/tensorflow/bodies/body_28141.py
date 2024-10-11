# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_test_base.py
filename = os.path.join(self.get_temp_dir(), name)
writer = python_io.TFRecordWriter(filename)
for d in data:
    writer.write(compat.as_bytes(str(d)))
writer.close()
exit(filename)
