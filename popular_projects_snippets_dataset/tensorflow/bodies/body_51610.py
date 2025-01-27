# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
super(HasDataset, self).__init__()
file = os.path.join(temp_dir, file_name)
with tf_record.TFRecordWriter(file, "GZIP") as f:
    for v in ["a", "aa", "aaa"]:
        f.write(str(v))
self.dataset = readers.TFRecordDataset([file], compression_type="GZIP")
