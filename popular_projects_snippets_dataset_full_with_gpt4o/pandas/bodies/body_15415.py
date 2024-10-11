# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
if not isinstance(key, int):
    exit()

self.check_indexer(obj, key, expected, val, indexer_sli, is_inplace)

if indexer_sli is tm.loc:
    self.check_indexer(obj, key, expected, val, tm.at, is_inplace)
elif indexer_sli is tm.iloc:
    self.check_indexer(obj, key, expected, val, tm.iat, is_inplace)

rng = range(key, key + 1)
self.check_indexer(obj, rng, expected, val, indexer_sli, is_inplace)

if indexer_sli is not tm.loc:
    # Note: no .loc because that handles slice edges differently
    slc = slice(key, key + 1)
    self.check_indexer(obj, slc, expected, val, indexer_sli, is_inplace)

ilkey = [key]
self.check_indexer(obj, ilkey, expected, val, indexer_sli, is_inplace)

indkey = np.array(ilkey)
self.check_indexer(obj, indkey, expected, val, indexer_sli, is_inplace)

genkey = (x for x in [key])
self.check_indexer(obj, genkey, expected, val, indexer_sli, is_inplace)
