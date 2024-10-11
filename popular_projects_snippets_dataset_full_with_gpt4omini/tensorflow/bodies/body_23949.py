# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
"""Create record with mix of random and repeated data to test compression on."""
rnd = random.Random(123)
random_record = compat.as_bytes(
    "".join(rnd.choice(string.digits) for _ in range(10000)))
repeated_record = compat.as_bytes(_TEXT)
for _ in range(10000):
    start_i = rnd.randint(0, len(_TEXT))
    length = rnd.randint(10, 200)
    repeated_record += _TEXT[start_i:start_i + length]
records = [random_record, repeated_record, random_record]

tests = [
    ("compression_level", 2, "LE"),  # Lower compression is worse or equal.
    ("compression_level", 6, 0),  # Default compression_level is equal.
    ("flush_mode", zlib.Z_FULL_FLUSH, 1),  # A few less bytes.
    ("flush_mode", zlib.Z_NO_FLUSH, 0),  # NO_FLUSH is the default.
    ("input_buffer_size", 4096, 0),  # Increases time not size.
    ("output_buffer_size", 4096, 0),  # Increases time not size.
    ("window_bits", 8, -1),  # Smaller than default window increases size.
    ("compression_strategy", zlib.Z_HUFFMAN_ONLY, -1),  # Worse.
    ("compression_strategy", zlib.Z_FILTERED, "LE"),  # Worse or equal.
]

compression_type = tf_record.TFRecordCompressionType.ZLIB
options_a = tf_record.TFRecordOptions(compression_type)
for prop, value, delta_sign in tests:
    options_b = tf_record.TFRecordOptions(
        compression_type=compression_type, **{prop: value})
    delta = self._CompressionSizeDelta(records, options_a, options_b)
    if delta_sign == "LE":
        self.assertLessEqual(
            delta, 0,
            "Setting {} = {}, file was {} smaller didn't match sign of {}"
            .format(prop, value, delta, delta_sign))
    else:
        self.assertTrue(
            delta == 0 if delta_sign == 0 else delta // delta_sign > 0,
            "Setting {} = {}, file was {} smaller didn't match sign of {}"
            .format(prop, value, delta, delta_sign))
