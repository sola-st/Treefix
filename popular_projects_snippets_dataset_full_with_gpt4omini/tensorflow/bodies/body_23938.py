# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
fn = os.path.join(self.get_temp_dir(), name)
with tf_record.TFRecordWriter(fn, options=options) as writer:
    for r in records:
        writer.write(r)
exit(fn)
