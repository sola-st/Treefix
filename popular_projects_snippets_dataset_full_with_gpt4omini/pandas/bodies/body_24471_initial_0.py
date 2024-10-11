lines = [['Hello', 'World'], ['   '], ['', '', ''], ['Python'], ['   Python   '], ['Code']] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
from l3.Runtime import _l_
"""
        Iterate through the lines and remove any that are
        either empty or contain only one whitespace value

        Parameters
        ----------
        lines : list of list of Scalars
            The array of lines that we are to filter.

        Returns
        -------
        filtered_lines : list of list of Scalars
            The same array of lines with the "empty" ones removed.
        """
ret = []
_l_(4758)
for line in lines:
    _l_(4761)

    # Remove empty lines and lines with only one whitespace value
    if (
        len(line) > 1
        or len(line) == 1
        and (not isinstance(line[0], str) or line[0].strip())
    ):
        _l_(4760)

        ret.append(line)
        _l_(4759)
aux = ret
_l_(4762)
exit(aux)
