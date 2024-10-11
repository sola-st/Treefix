# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/boxplot.py
if self.subplots:
    # Disable label ax sharing. Otherwise, all subplots shows last
    # column label
    if self.orientation == "vertical":
        self.sharex = False
    else:
        self.sharey = False
