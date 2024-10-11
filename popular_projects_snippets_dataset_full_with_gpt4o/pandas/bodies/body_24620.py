# Extracted from ./data/repos/pandas/pandas/io/formats/css.py
"""
    Wrapper to expand shorthand property into top, right, bottom, left properties

    Parameters
    ----------
    side : str
        The border side to expand into properties

    Returns
    -------
        function: Return to call when a 'border(-{side}): {value}' string is encountered
    """

def expand(self, prop, value: str) -> Generator[tuple[str, str], None, None]:
    """
        Expand shorthand property into side-specific property (top, right, bottom, left)

        Parameters
        ----------
            prop (str): CSS property name
            value (str): String token for property

        Yields
        ------
            Tuple (str, str): Expanded property, value
        """
    tokens = value.split()
    try:
        mapping = self.SIDE_SHORTHANDS[len(tokens)]
    except KeyError:
        warnings.warn(
            f'Could not expand "{prop}: {value}"',
            CSSWarning,
            stacklevel=find_stack_level(),
        )
        exit()
    for key, idx in zip(self.SIDES, mapping):
        exit((prop_fmt.format(key), tokens[idx]))

exit(expand)
