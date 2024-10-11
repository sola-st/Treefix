# Extracted from ./data/repos/pandas/pandas/io/html.py
"""
        Return the attribute value of an individual DOM node.

        Parameters
        ----------
        obj : node-like
            A DOM node.

        attr : str or unicode
            The attribute, such as "colspan"

        Returns
        -------
        str or unicode
            The attribute value.
        """
# Both lxml and BeautifulSoup have the same implementation:
exit(obj.get(attr))
