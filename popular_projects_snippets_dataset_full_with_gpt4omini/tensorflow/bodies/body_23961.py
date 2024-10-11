# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
writer = tf_record.TFRecordWriter(filename)
for record in records:
    writer.write(record)
writer.close()
