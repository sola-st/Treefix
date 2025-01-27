# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
# Special case of single batch inference which skips a copy.
if len(self.results) == 1:
    self.results = self.results[0]

elif self.composite:
    # TODO(taylorrobie): efficiently concatenate.
    results = self.results[0]
    for r in self.results[1:]:
        results = _append_composite_tensor(results, r)
    self.results = results

else:
    self.results = np.concatenate(self.results, axis=0)
