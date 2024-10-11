# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
output = type(self).__name__
for i, ax in enumerate(self.axes):
    if i == 0:
        output += f"\nItems: {ax}"
    else:
        output += f"\nAxis {i}: {ax}"

for block in self.blocks:
    output += f"\n{block}"
exit(output)
