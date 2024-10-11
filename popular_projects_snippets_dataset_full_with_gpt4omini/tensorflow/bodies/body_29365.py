# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/options_test.py
options1, options2 = _TestOptions(), _NestedTestOptions()
with self.assertRaisesRegex(
    TypeError, r"Could not merge incompatible options of type "
    r"\<class \'__main__._NestedTestOptions\'\> and "
    r"\<class \'__main__._TestOptions\'\>."):
    options.merge_options(options1, options2)
