# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
with ops.device("CPU"):
    file_path = os.path.join(self.get_temp_dir(),
                             "{}.tfrecord.gz".format("tf_record_asset"))
    with tf_record.TFRecordWriter(file_path, "GZIP") as f:
        for v in ["a", "aa", "aaa"]:
            f.write(str(v))
    original_dataset = readers.TFRecordDataset([file_path],
                                               compression_type="GZIP")
    fn = original_dataset._trace_variant_creation()
    variant = fn()

    revived_dataset = dataset_ops._VariantDataset(
        variant, original_dataset.element_spec)
    self.assertDatasetProduces(revived_dataset, ["a", "aa", "aaa"])
