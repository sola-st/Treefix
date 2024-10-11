# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
with self.assertRaisesRegex(
    # Due to exception chaining in PY3, we can't be more specific here and
    # check that the phrase 'Fail argument sent' is present.
    ValueError, 'Failed to load delegate from'):
    interpreter_wrapper.load_delegate(
        self._delegate_file, options={'fail': 'fail'})
