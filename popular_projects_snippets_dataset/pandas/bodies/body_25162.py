# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
x, y = self.x, self.y
xlabel = self.xlabel if self.xlabel is not None else pprint_thing(x)
ylabel = self.ylabel if self.ylabel is not None else pprint_thing(y)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
