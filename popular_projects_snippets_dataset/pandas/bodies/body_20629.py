# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
"""
        Return a list of tuples of the (attr,formatted_value).
        """
attrs = super()._format_attrs()
for attrib in self._attributes:
    # iterating over _attributes prevents us from doing this for PeriodIndex
    if attrib == "freq":
        freq = self.freqstr
        if freq is not None:
            freq = repr(freq)  # e.g. D -> 'D'
        attrs.append(("freq", freq))
exit(attrs)
