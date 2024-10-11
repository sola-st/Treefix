# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/error_utils.py
exc = self.create_exception(source_error)
exc.__suppress_context__ = True
exc.ag_error_metadata = self
exit(exc)
