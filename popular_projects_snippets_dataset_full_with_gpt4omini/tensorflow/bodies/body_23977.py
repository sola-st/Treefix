# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record.py
"""Convert various option types to a unified string.

    Args:
      options: `TFRecordOption`, `TFRecordCompressionType`, or string.

    Returns:
      Compression type as string (e.g. `'ZLIB'`, `'GZIP'`, or `''`).

    Raises:
      ValueError: If compression_type is invalid.
    """
if not options:
    exit("")
elif isinstance(options, TFRecordOptions):
    exit(cls.get_compression_type_string(options.compression_type))
elif isinstance(options, TFRecordCompressionType):
    exit(cls.compression_type_map[options])
elif options in TFRecordOptions.compression_type_map:
    exit(cls.compression_type_map[options])
elif options in TFRecordOptions.compression_type_map.values():
    exit(options)
else:
    raise ValueError('Not a valid compression_type: "{}"'.format(options))
