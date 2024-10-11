# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record.py
# pylint: disable=line-too-long
"""Creates a `TFRecordOptions` instance.

    Options only effect TFRecordWriter when compression_type is not `None`.
    Documentation, details, and defaults can be found in
    [`zlib_compression_options.h`](https://www.tensorflow.org/code/tensorflow/core/lib/io/zlib_compression_options.h)
    and in the [zlib manual](http://www.zlib.net/manual.html).
    Leaving an option as `None` allows C++ to set a reasonable default.

    Args:
      compression_type: `"GZIP"`, `"ZLIB"`, or `""` (no compression).
      flush_mode: flush mode or `None`, Default: Z_NO_FLUSH.
      input_buffer_size: int or `None`.
      output_buffer_size: int or `None`.
      window_bits: int or `None`.
      compression_level: 0 to 9, or `None`.
      compression_method: compression method or `None`.
      mem_level: 1 to 9, or `None`.
      compression_strategy: strategy or `None`. Default: Z_DEFAULT_STRATEGY.

    Returns:
      A `TFRecordOptions` object.

    Raises:
      ValueError: If compression_type is invalid.
    """
# pylint: enable=line-too-long
# Check compression_type is valid, but for backwards compatibility don't
# immediately convert to a string.
self.get_compression_type_string(compression_type)
self.compression_type = compression_type
self.flush_mode = flush_mode
self.input_buffer_size = input_buffer_size
self.output_buffer_size = output_buffer_size
self.window_bits = window_bits
self.compression_level = compression_level
self.compression_method = compression_method
self.mem_level = mem_level
self.compression_strategy = compression_strategy
