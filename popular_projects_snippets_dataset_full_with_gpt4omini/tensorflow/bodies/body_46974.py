# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/error_utils_test.py

callsite_tb = [
    ('/path/one.py', 11, 'test_fn_1', 'test code 1'),
    ('/path/two.py', 0, 'test_fn_2', 'test code 2'),
    ('/path/three.py', 171, 'test_fn_3', 'test code 3'),
]
cause_message = 'Test message'
em = error_utils.ErrorMetadataBase(
    callsite_tb=callsite_tb,
    cause_metadata=None,
    cause_message=cause_message,
    source_map={},
    converter_filename='/path/two.py')
self.assertRegex(
    em.get_message(),
    re.compile((r'"/path/one.py", line 11, in test_fn_1.*'
                r'"/path/three.py", line 171, in test_fn_3  \*\*.*'
                r'Test message'), re.DOTALL))
