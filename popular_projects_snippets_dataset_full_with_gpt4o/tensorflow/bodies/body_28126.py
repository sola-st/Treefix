# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_test_base.py
if label_key_provided:
    # outputs would be a tuple of (feature dict, label)
    features, label = self.evaluate(outputs())
else:
    features = self.evaluate(outputs())
    label = features["label"]
file_out = features["file"]
keywords_indices = features["keywords"].indices
keywords_values = features["keywords"].values
keywords_dense_shape = features["keywords"].dense_shape
record = features["record"]
exit(([
    file_out, keywords_indices, keywords_values, keywords_dense_shape,
    record, label
]))
