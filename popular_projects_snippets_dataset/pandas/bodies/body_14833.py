# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
import matplotlib as mpl
import matplotlib.gridspec
import matplotlib.pyplot as plt

gs = mpl.gridspec.GridSpec(2, 2)
ax_tl = plt.subplot(gs[0, 0])
ax_ll = plt.subplot(gs[1, 0])
ax_tr = plt.subplot(gs[0, 1])
ax_lr = plt.subplot(gs[1, 1])

exit((gs, [ax_tl, ax_ll, ax_tr, ax_lr]))
