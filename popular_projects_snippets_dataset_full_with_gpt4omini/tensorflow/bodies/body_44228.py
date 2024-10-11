# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/reference_test_base.py
exit(tf.autograph.to_graph(
    f, experimental_optional_features=self.autograph_opts))
