# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/boxplot.py
# GH 45465: make sure that the boxplot doesn't ignore xlabel/ylabel
if self.xlabel:
    ax.set_xlabel(pprint_thing(self.xlabel))
if self.ylabel:
    ax.set_ylabel(pprint_thing(self.ylabel))
