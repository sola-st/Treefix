# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/error_utils_test.py
callsite_tb = [
    ('/path/one.py', 11, 'test_fn_1', None),
    ('/path/two.py', 171, 'test_fn_2', 'test code'),
]
cause_message = 'Test message'
em = error_utils.ErrorMetadataBase(
    callsite_tb=callsite_tb,
    cause_metadata=None,
    cause_message=cause_message,
    source_map={},
    converter_filename=None)
self.assertRegex(
    em.get_message(),
    re.compile(('"/path/one.py", line 11, in test_fn_1.*'
                '"/path/two.py", line 171, in test_fn_2.*'
                'Test message'), re.DOTALL))
