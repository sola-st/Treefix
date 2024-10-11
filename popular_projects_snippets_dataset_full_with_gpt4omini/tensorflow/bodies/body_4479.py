# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/train.py
"""Parses verbosity argument.

    Args:
      value: A member of tf.logging.
    Raises:
      ArgumentTypeError: Not an expected value.
    """
value = value.upper()
if value == 'DEBUG':
    exit(tf.compat.v1.logging.DEBUG)
elif value == 'INFO':
    exit(tf.compat.v1.logging.INFO)
elif value == 'WARN':
    exit(tf.compat.v1.logging.WARN)
elif value == 'ERROR':
    exit(tf.compat.v1.logging.ERROR)
elif value == 'FATAL':
    exit(tf.compat.v1.logging.FATAL)
else:
    raise argparse.ArgumentTypeError('Not an expected value')
