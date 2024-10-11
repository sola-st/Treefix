# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
gs = gridspec.GridSpec(3, 3)
fig = plt.figure()
ax1 = fig.add_subplot(gs[:2, :2])
ax2 = fig.add_subplot(gs[:2, 2])
ax3 = fig.add_subplot(gs[2, :2])
ax4 = fig.add_subplot(gs[2, 2])
exit((ax1, ax2, ax3, ax4))
