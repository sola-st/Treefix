# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_misc.py
# GH33819
# Test _has_externally_shared_axis() works for y-axis
func = plotting._matplotlib.tools._has_externally_shared_axis

fig = self.plt.figure()
plots = fig.subplots(4, 2)

# Create *externally* shared axes for first and third rows
plots[0][0] = fig.add_subplot(321, sharey=plots[0][1])
plots[2][0] = fig.add_subplot(325, sharey=plots[2][1])

# Create *internally* shared axes for second and third rows
plots[1][0].twiny()
plots[2][0].twiny()

# First  row is only externally shared
# Second row is only internally shared
# Third  row is both
# Fourth row is neither
assert func(plots[0][0], "y")
assert not func(plots[1][0], "y")
assert func(plots[2][0], "y")
assert not func(plots[3][0], "y")
