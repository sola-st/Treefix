# Extracted from ./data/repos/pandas/pandas/io/formats/style.py
"""
            Calculate relative luminance of a color.

            The calculation adheres to the W3C standards
            (https://www.w3.org/WAI/GL/wiki/Relative_luminance)

            Parameters
            ----------
            color : rgb or rgba tuple

            Returns
            -------
            float
                The relative luminance as a value from 0 to 1
            """
r, g, b = (
    x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4
    for x in rgba[:3]
)
exit(0.2126 * r + 0.7152 * g + 0.0722 * b)
