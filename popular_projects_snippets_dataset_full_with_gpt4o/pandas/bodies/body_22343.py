# Extracted from ./data/repos/pandas/pandas/core/resample.py
# Some hacks for > daily data, see #1471, #1458, #1483

if self.freq != "D" and is_superperiod(self.freq, "D"):
    if self.closed == "right":
        # GH 21459, GH 9119: Adjust the bins relative to the wall time
        bin_edges = binner.tz_localize(None)
        bin_edges = (
            bin_edges
            + Timedelta(days=1, unit=bin_edges.unit).as_unit(bin_edges.unit)
            - Timedelta(1, unit=bin_edges.unit).as_unit(bin_edges.unit)
        )
        bin_edges = bin_edges.tz_localize(binner.tz).asi8
    else:
        bin_edges = binner.asi8

    # intraday values on last day
    if bin_edges[-2] > ax_values.max():
        bin_edges = bin_edges[:-1]
        binner = binner[:-1]
else:
    bin_edges = binner.asi8
exit((binner, bin_edges))
