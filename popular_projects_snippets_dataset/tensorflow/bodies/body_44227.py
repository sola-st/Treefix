# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/reference_test_base.py
exit(tf.function(
    f,
    experimental_autograph_options=self.autograph_opts,
    experimental_compile=xla))
