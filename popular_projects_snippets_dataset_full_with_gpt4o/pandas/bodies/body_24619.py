# Extracted from ./data/repos/pandas/pandas/io/formats/css.py
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
