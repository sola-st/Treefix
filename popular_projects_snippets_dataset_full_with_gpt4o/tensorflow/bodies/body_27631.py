# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/lookup_ops_test.py
vocabulary_file1 = self._createVocabFile("test1.txt",
                                         ("one", "two", "three"))
vocabulary_file2 = self._createVocabFile("test2.txt",
                                         ("four", "five", "six"))
ds = reader_ops.TextLineDataset([vocabulary_file1, vocabulary_file2])
ds = ds.enumerate(start=1)
init = lookup_ops.DatasetInitializer(ds)
table = self.getHashTable()(init, default_value="")
self.initialize_table(table)

output = table.lookup(constant_op.constant([2, 3, 4], dtypes.int64))
result = self.evaluate(output)
self.assertAllEqual(["two", "three", "four"], result)
