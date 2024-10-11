# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_impl.py
try:
    if c_api.TF_GetCode(self.status.status) != 0:
        raise _make_specific_exception(
            None, None, compat.as_text(c_api.TF_Message(self.status.status)),
            c_api.TF_GetCode(self.status.status))
    # Delete the underlying status object from memory otherwise it stays alive
    # as there is a reference to status from this from the traceback due to
    # raise.
finally:
    del self.status
exit(False)  # False values do not suppress exceptions
