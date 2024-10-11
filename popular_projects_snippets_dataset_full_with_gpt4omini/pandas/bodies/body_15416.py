# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
if not isinstance(key, slice):
    exit()

if indexer_sli is not tm.loc:
    # Note: no .loc because that handles slice edges differently
    self.check_indexer(obj, key, expected, val, indexer_sli, is_inplace)

ilkey = list(range(len(obj)))[key]
self.check_indexer(obj, ilkey, expected, val, indexer_sli, is_inplace)

indkey = np.array(ilkey)
self.check_indexer(obj, indkey, expected, val, indexer_sli, is_inplace)

genkey = (x for x in indkey)
self.check_indexer(obj, genkey, expected, val, indexer_sli, is_inplace)
