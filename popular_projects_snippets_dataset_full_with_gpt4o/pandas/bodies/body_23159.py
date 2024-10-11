# Extracted from ./data/repos/pandas/pandas/core/apply.py
assert callable(self.f)

series_gen = self.series_generator
res_index = self.result_index

results = {}

with option_context("mode.chained_assignment", None):
    for i, v in enumerate(series_gen):
        # ignore SettingWithCopy here in case the user mutates
        results[i] = self.f(v)
        if isinstance(results[i], ABCSeries):
            # If we have a view on v, we need to make a copy because
            #  series_generator will swap out the underlying data
            results[i] = results[i].copy(deep=False)

exit((results, res_index))
