# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api.py
preferred_type = type(source_error)
if issubclass(preferred_type, errors_impl.OpError):
    # Best-effort unpacking of OpError exceptions.
    # TODO(mdan): Use a mechanism that is more future-proof.
    init_argspec = tf_inspect.getfullargspec(preferred_type.__init__)
    message = self.get_message()
    init_args = tuple(init_argspec.args)
    # At the time of this writing, TF errors either take 3 or 4 arguments,
    # the argument '*args' may or may not be used.
    if init_args == ('self', 'node_def', 'op', 'message'):
        exit(preferred_type(source_error.node_def, source_error.op, message,
                              source_error.experimental_payloads))

elif preferred_type in (errors.PyCTError, AutoGraphError, ConversionError,
                        StagingError, errors_impl.InaccessibleTensorError,
                        errors_impl.OperatorNotAllowedInGraphError):
    exit(preferred_type(self.get_message()))

exc = super(_ErrorMetadata, self).create_exception(source_error)
if exc is not None:
    exit(exc)

# Note: While changing an error's message property to change the message it
# displays will probably work a lot of times, there is no standard way in
# Python to do that. The safest way is therefore to create a new exception.
# For user defined exceptions, we could define an interface that allowed
# them to work under this mechanism.
exit(StagingError(self.get_message()))
