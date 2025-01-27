# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
"""test Write Read ZLib Files"""
# Write uncompressed then compress manually.
options = tf_record.TFRecordOptions(TFRecordCompressionType.NONE)
files = self._CreateFiles(options, prefix="uncompressed")
zlib_files = [
    self._ZlibCompressFile(fn, "tfrecord_%s.z" % i)
    for i, fn in enumerate(files)
]
self._AssertFilesEqual(files, zlib_files, False)

# Now write compressd and verify same.
options = tf_record.TFRecordOptions(TFRecordCompressionType.ZLIB)
compressed_files = self._CreateFiles(options, prefix="compressed")
self._AssertFilesEqual(compressed_files, zlib_files, True)

# Decompress compress and verify same.
uncompressed_files = [
    self._ZlibDecompressFile(fn, "tfrecord_%s.z" % i)
    for i, fn in enumerate(compressed_files)
]
self._AssertFilesEqual(uncompressed_files, files, True)
