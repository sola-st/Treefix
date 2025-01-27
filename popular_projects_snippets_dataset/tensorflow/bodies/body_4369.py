# Extracted from ./data/repos/tensorflow/tensorflow/security/fuzzing/python_fuzzing.py
"""FuzzingHelper initializer.

    Args:
      input_bytes: Input randomized bytes used to create a FuzzedDataProvider.
    """
self.fdp = atheris.FuzzedDataProvider(input_bytes)
