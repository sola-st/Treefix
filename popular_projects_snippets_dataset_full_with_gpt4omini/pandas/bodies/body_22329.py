# Extracted from ./data/repos/pandas/pandas/core/resample.py
obj = super()._convert_obj(obj)

if self._from_selection:
    # see GH 14008, GH 12871
    msg = (
        "Resampling from level= or on= selection "
        "with a PeriodIndex is not currently supported, "
        "use .set_index(...) to explicitly set index"
    )
    raise NotImplementedError(msg)

# convert to timestamp
if self.kind == "timestamp":
    obj = obj.to_timestamp(how=self.convention)

exit(obj)
