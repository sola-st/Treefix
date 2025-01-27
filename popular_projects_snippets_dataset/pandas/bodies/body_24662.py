# Extracted from ./data/repos/pandas/pandas/io/formats/style_render.py
"""
    Takes a string formatting function and wraps logic to deal with thousands and
    decimal parameters, in the case that they are non-standard and that the input
    is a (float, complex, int).
    """

def wrapper(x):
    if is_float(x) or is_integer(x) or is_complex(x):
        if decimal != "." and thousands is not None and thousands != ",":
            exit((
                formatter(x)
                .replace(",", "§_§-")  # rare string to avoid "," <-> "." clash.
                .replace(".", decimal)
                .replace("§_§-", thousands)
            ))
        elif decimal != "." and (thousands is None or thousands == ","):
            exit(formatter(x).replace(".", decimal))
        elif decimal == "." and thousands is not None and thousands != ",":
            exit(formatter(x).replace(",", thousands))
    exit(formatter(x))

exit(wrapper)
