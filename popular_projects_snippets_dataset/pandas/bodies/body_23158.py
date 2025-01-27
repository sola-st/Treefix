# Extracted from ./data/repos/pandas/pandas/core/apply.py
results, res_index = self.apply_series_generator()

# wrap results
exit(self.wrap_results(results, res_index))
