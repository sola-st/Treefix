# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
for child in children:
    _, attr = tf_decorator.unwrap(child[1])
    api_names = tf_export.get_v1_names(attr)
    for name in api_names:
        _, _, _, text = self._upgrade("tf." + name)
        if (text and
            not text.startswith("tf.compat.v1") and
            not text.startswith("tf.compat.v2") and
            text not in self.v2_symbols and
            # Ignore any symbol that contains __internal__
            "__internal__" not in text and
            # Builds currently install old version of estimator that doesn't
            # have some 2.0 symbols.
            not text.startswith("tf.estimator")):
            self.assertFalse(
                True, "Symbol %s generated from %s not in v2 API" % (
                    text, name))
