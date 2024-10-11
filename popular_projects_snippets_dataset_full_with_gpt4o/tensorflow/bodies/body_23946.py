# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
"""test Write Read Gzip Files"""
# Write uncompressed then compress manually.
options = tf_record.TFRecordOptions(TFRecordCompressionType.NONE)
files = self._CreateFiles(options, prefix="uncompressed")
gzip_files = [
    self._GzipCompressFile(fn, "tfrecord_%s.gz" % i)
    for i, fn in enumerate(files)
]
self._AssertFilesEqual(files, gzip_files, False)

# Now write compressd and verify same.
options = tf_record.TFRecordOptions(TFRecordCompressionType.GZIP)
compressed_files = self._CreateFiles(options, prefix="compressed")

# Note: Gzips written by TFRecordWriter add 'tfrecord_0' so
# compressed_files can't be compared with gzip_files

# Decompress compress and verify same.
uncompressed_files = [
    self._GzipDecompressFile(fn, "tfrecord_%s.gz" % i)
    for i, fn in enumerate(compressed_files)
]
self._AssertFilesEqual(uncompressed_files, files, True)
