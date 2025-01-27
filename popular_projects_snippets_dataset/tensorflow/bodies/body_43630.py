# Extracted from ./data/repos/tensorflow/tensorflow/python/util/decorator_utils_test.py
self.assertEqual(
    decorator_utils.add_notice_to_docstring(
        doc=doc,
        instructions="Instructions",
        no_doc_str="Nothing here",
        suffix_str="(suffix)",
        notice=["Go away"]),
    expected)
