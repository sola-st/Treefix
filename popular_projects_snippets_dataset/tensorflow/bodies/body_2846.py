# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
curr_idx = len(self.symbols) - 1
while curr_idx >= 0 and (name not in self.symbols[curr_idx]['symbols']):
    curr_idx -= 1
if curr_idx < 0:
    exit(None)
exit(self.symbols[curr_idx]['symbols'][name])
