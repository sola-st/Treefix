# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Asserts that message is same as parsed expected_message_ascii.

    Creates another prototype of message, reads the ascii message into it and
    then compares them using self._AssertProtoEqual().

    Args:
      expected_message_maybe_ascii: proto message in original or ascii form.
      message: the message to validate.
      msg: Optional message to report on failure.
    """
if isinstance(expected_message_maybe_ascii, type(message)):
    expected_message = expected_message_maybe_ascii
    self._AssertProtoEquals(expected_message, message, msg=msg)
elif isinstance(expected_message_maybe_ascii, (str, bytes)):
    expected_message = type(message)()
    text_format.Merge(
        expected_message_maybe_ascii,
        expected_message,
        descriptor_pool=descriptor_pool.Default())
    self._AssertProtoEquals(expected_message, message, msg=msg)
else:
    assert False, ("Can't compare protos of type %s and %s." %
                   (type(expected_message_maybe_ascii), type(message)))
