# Extracted from ./data/repos/tensorflow/tensorflow/cc/saved_model/testdata/generate_saved_models.py
self.asset = asset.Asset(
    test.test_src_dir_path(
        "cc/saved_model/testdata/static_hashtable_asset.txt"))
self.table = lookup_ops.StaticHashTable(
    lookup_ops.TextFileInitializer(self.asset, dtypes.string,
                                   lookup_ops.TextFileIndex.WHOLE_LINE,
                                   dtypes.int64,
                                   lookup_ops.TextFileIndex.LINE_NUMBER),
    -1)
