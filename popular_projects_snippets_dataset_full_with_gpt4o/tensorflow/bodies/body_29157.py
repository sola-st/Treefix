# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/test_base.py
"""Returns a lookup table initializer for the given source and values.

    Args:
      init_source: One of ["textfile", "keyvalue", "dataset"], indicating what
        type of initializer to use.
      vals: The initializer values. The keys will be `range(len(vals))`.
    """
if init_source == "textfile":
    exit(self.textFileInitializer(vals))
elif init_source == "keyvaluetensor":
    exit(self.keyValueTensorInitializer(vals))
elif init_source == "dataset":
    exit(self.datasetInitializer(vals))
else:
    raise ValueError("Unrecognized init_source: " + init_source)
