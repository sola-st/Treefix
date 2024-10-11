# Extracted from ./data/repos/tensorflow/tensorflow/python/types/trace.py
"""Returns the tracing type of this object.

    The tracing type is used to build the signature of a tf.function
    when traced, and to match arguments with existing signatures.
    When a Function object is called, tf.function looks at the tracing type
    of the call arguments. If an existing signature of matching type exists,
    it will be used. Otherwise, a new function is traced, and its signature
    will use the tracing type of the call arguments.

    Args:
      context: a context object created for each function call for tracking
        information about the call arguments as a whole
    Returns:
      The tracing type of this object.
    """
