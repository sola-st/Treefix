# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
ax, leg = self._get_ax_legend(self.axes[0])

handles = []
labels = []
title = ""

if not self.subplots:
    if leg is not None:
        title = leg.get_title().get_text()
        # Replace leg.LegendHandles because it misses marker info
        handles = leg.legendHandles
        labels = [x.get_text() for x in leg.get_texts()]

    if self.legend:
        if self.legend == "reverse":
            handles += reversed(self.legend_handles)
            labels += reversed(self.legend_labels)
        else:
            handles += self.legend_handles
            labels += self.legend_labels

        if self.legend_title is not None:
            title = self.legend_title

    if len(handles) > 0:
        ax.legend(handles, labels, loc="best", title=title)

elif self.subplots and self.legend:
    for ax in self.axes:
        if ax.get_visible():
            ax.legend(loc="best")
