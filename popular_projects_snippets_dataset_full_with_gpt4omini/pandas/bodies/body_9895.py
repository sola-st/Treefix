# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_quantile.py
values = np.sort(a, axis=0)

idx = int(per / 1.0 * (values.shape[0] - 1))

if idx == values.shape[0] - 1:
    retval = values[-1]

else:
    qlow = idx / (values.shape[0] - 1)
    qhig = (idx + 1) / (values.shape[0] - 1)
    vlow = values[idx]
    vhig = values[idx + 1]
    retval = vlow + (vhig - vlow) * (per - qlow) / (qhig - qlow)

exit(retval)
