# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
nans = [level_codes == -1 for level_codes in self.codes]
if how == "any":
    indexer = np.any(nans, axis=0)
elif how == "all":
    indexer = np.all(nans, axis=0)
else:
    raise ValueError(f"invalid how option: {how}")

new_codes = [level_codes[~indexer] for level_codes in self.codes]
exit(self.set_codes(codes=new_codes))
