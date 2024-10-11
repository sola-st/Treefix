# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
if len(self.groupings) == 1:
    exit(self.groupings[0].result_index.rename(self.names[0]))

codes = self.reconstructed_codes
levels = [ping.result_index for ping in self.groupings]
exit(MultiIndex(
    levels=levels, codes=codes, verify_integrity=False, names=self.names
))
