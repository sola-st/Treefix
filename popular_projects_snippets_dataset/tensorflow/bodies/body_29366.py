# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/options_test.py
with self.assertRaisesRegex(
    TypeError, "All options to be merged should inherit from "
    r"\`OptionsBase\` but found option of type \<class \'int\'\> which "
    "does not."):
    options.merge_options(1, 2, 3)
