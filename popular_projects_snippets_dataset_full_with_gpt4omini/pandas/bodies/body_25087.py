# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/hist.py
if self.orientation == "horizontal":
    ax.set_xlabel("Frequency" if self.xlabel is None else self.xlabel)
    ax.set_ylabel(self.ylabel)
else:
    ax.set_xlabel(self.xlabel)
    ax.set_ylabel("Frequency" if self.ylabel is None else self.ylabel)
