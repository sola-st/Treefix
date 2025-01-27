# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/record_input_test.py
options = tf_record.TFRecordOptions(compression_type)
for i in range(n):
    f = os.path.join(self.get_temp_dir(), prefix + "." + str(i))
    w = tf_record.TFRecordWriter(f, options=options)

    for j in range(m):
        w.write("{0:0{width}}".format(i * m + j, width=10).encode("utf-8"))

w.close()
