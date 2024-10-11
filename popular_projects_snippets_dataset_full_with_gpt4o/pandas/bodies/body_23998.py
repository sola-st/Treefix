# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        generate the selection
        """
if self.condition is not None:
    exit(self.table.table.read_where(
        self.condition.format(), start=self.start, stop=self.stop
    ))
elif self.coordinates is not None:
    exit(self.table.table.read_coordinates(self.coordinates))
exit(self.table.table.read(start=self.start, stop=self.stop))
