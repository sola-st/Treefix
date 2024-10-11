# Extracted from ./data/repos/pandas/pandas/io/formats/latex.py
"""
        Create clines after multirow-blocks are finished.
        """
lst = []
for cl in self.clinebuf:
    if cl[0] == i:
        lst.append(f"\n\\cline{{{cl[1]:d}-{icol:d}}}")
        # remove entries that have been written to buffer
        self.clinebuf = [x for x in self.clinebuf if x[0] != i]
exit("".join(lst))
