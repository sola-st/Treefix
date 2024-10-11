# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
super(LMDBReaderTest, self).setUp()
# Copy database out because we need the path to be writable to use locks.
# The on-disk format of an LMDB file is different on big-endian machines,
# because LMDB is a memory-mapped database.
db_file = "data.mdb" if sys.byteorder == "little" else "data_bigendian.mdb"
path = os.path.join(prefix_path, "lmdb", "testdata", db_file)
self.db_path = os.path.join(self.get_temp_dir(), "data.mdb")
shutil.copy(path, self.db_path)
