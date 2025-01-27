# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/error_utils_test.py
callsite_tb = [
    ('/path/one.py', 11, 'test_fn_1', 'test code 1'),
    ('/path/two.py', 171, 'test_fn_2', 'test code 2'),
    ('/path/three.py', 171, 'test_fn_3', 'test code 3'),
]
cause_message = 'Test message'
em = error_utils.ErrorMetadataBase(
    callsite_tb=callsite_tb,
    cause_metadata=None,
    cause_message=cause_message,
    source_map={
        origin_info.LineLocation(filename='/path/two.py', lineno=171):
            origin_info.OriginInfo(
                loc=origin_info.LineLocation(
                    filename='/path/other_two.py', lineno=13),
                function_name='converted_fn',
                source_code_line='converted test code',
                comment=None)
    },
    converter_filename=None)
result = em.get_message()
self.assertRegex(
    result,
    re.compile((r'converted_fn  \*.*'
                r'"/path/three.py", line 171, in test_fn_3.*'
                r'Test message'), re.DOTALL))
self.assertNotRegex(result, re.compile('test_fn_1'))
