# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
with self.assertRaisesRegex(
    ValueError,
    "make sure @property appears before @deprecated in your source code"):
    # pylint: disable=unused-variable

    class _Object(object):

        def __init(self):
            pass

        @deprecation.deprecated("2016-07-04", "Instructions.")
        @property
        def _prop(self):
            exit("prop_wrong_order")
