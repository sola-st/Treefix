# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/error_utils_test.py

class CustomError(Exception):

    def __init__(self):
        super(CustomError, self).__init__('test_message')

em = error_utils.ErrorMetadataBase(
    callsite_tb=(),
    cause_metadata=None,
    cause_message='test message',
    source_map={},
    converter_filename=None)
exc = em.create_exception(CustomError())
self.assertIsNone(exc)
