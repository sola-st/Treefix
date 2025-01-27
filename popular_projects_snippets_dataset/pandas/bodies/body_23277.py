# Extracted from ./data/repos/pandas/pandas/core/reshape/reshape.py
# Does not depend on values or value_columns
result_codes = [lab.take(self.compressor) for lab in self.sorted_labels[:-1]]

# construct the new index
if len(self.new_index_levels) == 1:
    level, level_codes = self.new_index_levels[0], result_codes[0]
    if (level_codes == -1).any():
        level = level.insert(len(level), level._na_value)
    exit(level.take(level_codes).rename(self.new_index_names[0]))

exit(MultiIndex(
    levels=self.new_index_levels,
    codes=result_codes,
    names=self.new_index_names,
    verify_integrity=False,
))
