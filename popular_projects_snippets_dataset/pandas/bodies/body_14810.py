# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
gs = gridspec.GridSpec(1, 3)
fig = plt.figure()
ax1 = fig.add_subplot(gs[:, :2])
ax2 = fig.add_subplot(gs[:, 2])
exit((ax1, ax2))
