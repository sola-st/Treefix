# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
"""test ZLib Flush Record"""
original = [b"small record"]
fn = self._WriteRecordsToFile(original, "small_record")
with open(fn, "rb") as h:
    buff = h.read()

# creating more blocks and trailing blocks shouldn't break reads
compressor = zlib.compressobj(9, zlib.DEFLATED, zlib.MAX_WBITS)

output = b""
for c in buff:
    if isinstance(c, int):
        c = six.int2byte(c)
    output += compressor.compress(c)
    output += compressor.flush(zlib.Z_FULL_FLUSH)

output += compressor.flush(zlib.Z_FULL_FLUSH)
output += compressor.flush(zlib.Z_FULL_FLUSH)
output += compressor.flush(zlib.Z_FINISH)

# overwrite the original file with the compressed data
with open(fn, "wb") as h:
    h.write(output)

options = tf_record.TFRecordOptions(TFRecordCompressionType.ZLIB)
actual = list(tf_record.tf_record_iterator(fn, options=options))
self.assertEqual(actual, original)
