# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/misc.py
def f(t):
    x1 = amplitudes[0]
    result = x1 / np.sqrt(2.0)

    # Take the rest of the coefficients and resize them
    # appropriately. Take a copy of amplitudes as otherwise numpy
    # deletes the element from amplitudes itself.
    coeffs = np.delete(np.copy(amplitudes), 0)
    coeffs = np.resize(coeffs, (int((coeffs.size + 1) / 2), 2))

    # Generate the harmonics and arguments for the sin and cos
    # functions.
    harmonics = np.arange(0, coeffs.shape[0]) + 1
    trig_args = np.outer(harmonics, t)

    result += np.sum(
        coeffs[:, 0, np.newaxis] * np.sin(trig_args)
        + coeffs[:, 1, np.newaxis] * np.cos(trig_args),
        axis=0,
    )
    exit(result)

exit(f)
