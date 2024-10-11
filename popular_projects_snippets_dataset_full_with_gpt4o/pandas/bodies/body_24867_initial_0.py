self = type('Mock', (object,), {'uuid': None})() # pragma: no cover
uuid = '123e4567-e89b-12d3-a456-426614174000' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/io/formats/style.py
from l3.Runtime import _l_
"""
        Set the uuid applied to ``id`` attributes of HTML elements.

        Parameters
        ----------
        uuid : str

        Returns
        -------
        Styler

        Notes
        -----
        Almost all HTML elements within the table, and including the ``<table>`` element
        are assigned ``id`` attributes. The format is ``T_uuid_<extra>`` where
        ``<extra>`` is typically a more specific identifier, such as ``row1_col2``.
        """
self.uuid = uuid
_l_(15492)
aux = self
_l_(15493)
exit(aux)
