# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils_test.py
super(UtilsTest, self).setUp()
self._old_np_doc_form = np_utils.get_np_doc_form()
self._old_is_sig_mismatch_an_error = np_utils.is_sig_mismatch_an_error()
