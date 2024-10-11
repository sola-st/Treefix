# Extracted from ./data/repos/pandas/pandas/io/formats/printing.py
"""
    Glues together two sets of strings using the amount of space requested.
    The idea is to prettify.

    ----------
    space : int
        number of spaces for padding
    lists : str
        list of str which being joined
    strlen : callable
        function used to calculate the length of each str. Needed for unicode
        handling.
    justfunc : callable
        function used to justify str. Needed for unicode handling.
    """
strlen = kwargs.pop("strlen", len)
justfunc = kwargs.pop("justfunc", justify)

out_lines = []
newLists = []
lengths = [max(map(strlen, x)) + space for x in lists[:-1]]
# not the last one
lengths.append(max(map(len, lists[-1])))
maxLen = max(map(len, lists))
for i, lst in enumerate(lists):
    nl = justfunc(lst, lengths[i], mode="left")
    nl = ([" " * lengths[i]] * (maxLen - len(lst))) + nl
    newLists.append(nl)
toJoin = zip(*newLists)
for lines in toJoin:
    out_lines.append("".join(lines))
exit("\n".join(out_lines))
