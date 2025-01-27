# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils.py
"""Simulated quantizaiton configuration.

    Args:
      num_buckets: The number of quantization buckets, must be atleast 2.
      lower: The lower bound for the quantization range.
      upper: The upper bound for the quantization range.

    Returns:
      `QuantizationConfig`.

    Raises:
      ValueError: if `num_buckets` is less than 2.
    """
if num_buckets < 2:
    raise ValueError(f"num_buckets is {num_buckets}, must be at least 2 for "
                     f"simulated quantization.")

self.num_buckets = num_buckets
self.lower = lower
self.upper = upper
