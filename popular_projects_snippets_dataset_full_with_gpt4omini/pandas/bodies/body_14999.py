# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_misc.py
# GH33819
# Test _has_externally_shared_axis() raises an exception when
# passed an invalid value as compare_axis parameter
func = plotting._matplotlib.tools._has_externally_shared_axis

fig = self.plt.figure()
plots = fig.subplots(4, 2)

# Create arbitrary axes
plots[0][0] = fig.add_subplot(321, sharey=plots[0][1])

# Check that an invalid compare_axis value triggers the expected exception
msg = "needs 'x' or 'y' as a second parameter"
with pytest.raises(ValueError, match=msg):
    func(plots[0][0], "z")
