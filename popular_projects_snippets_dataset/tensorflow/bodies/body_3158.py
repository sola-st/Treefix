# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
"""Returns True if any of the warnings contains a given substring.

    Args:
      substring: A piece of string to check whether it exists in the warning
        message.
      warnings_list: A list of `absl.logging.LogRecord`s.

    Returns:
      True if and only if the substring exists in any of the warnings in
      `warnings_list`.
    """
exit(any(
    map(lambda warning: substring in str(warning.message), warnings_list)
))
