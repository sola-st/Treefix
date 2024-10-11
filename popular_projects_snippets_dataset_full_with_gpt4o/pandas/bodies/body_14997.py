# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_misc.py
# GH33819
# Test _has_externally_shared_axis() works for x-axis
func = plotting._matplotlib.tools._has_externally_shared_axis

fig = self.plt.figure()
plots = fig.subplots(2, 4)

# Create *externally* shared axes for first and third columns
plots[0][0] = fig.add_subplot(231, sharex=plots[1][0])
plots[0][2] = fig.add_subplot(233, sharex=plots[1][2])

# Create *internally* shared axes for second and third columns
plots[0][1].twinx()
plots[0][2].twinx()

# First  column is only externally shared
# Second column is only internally shared
# Third  column is both
# Fourth column is neither
assert func(plots[0][0], "x")
assert not func(plots[0][1], "x")
assert func(plots[0][2], "x")
assert not func(plots[0][3], "x")
