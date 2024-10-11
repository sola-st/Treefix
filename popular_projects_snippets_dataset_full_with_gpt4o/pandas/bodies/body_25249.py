# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/boxplot.py
if isinstance(self.color, dict):
    boxes = self.color.get("boxes", self._boxes_c)
    whiskers = self.color.get("whiskers", self._whiskers_c)
    medians = self.color.get("medians", self._medians_c)
    caps = self.color.get("caps", self._caps_c)
else:
    # Other types are forwarded to matplotlib
    # If None, use default colors
    boxes = self.color or self._boxes_c
    whiskers = self.color or self._whiskers_c
    medians = self.color or self._medians_c
    caps = self.color or self._caps_c

# GH 30346, when users specifying those arguments explicitly, our defaults
# for these four kwargs should be overridden; if not, use Pandas settings
if not self.kwds.get("boxprops"):
    setp(bp["boxes"], color=boxes, alpha=1)
if not self.kwds.get("whiskerprops"):
    setp(bp["whiskers"], color=whiskers, alpha=1)
if not self.kwds.get("medianprops"):
    setp(bp["medians"], color=medians, alpha=1)
if not self.kwds.get("capprops"):
    setp(bp["caps"], color=caps, alpha=1)
