# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
"""
        Formats a number in engineering notation, appending a letter
        representing the power of 1000 of the original number. Some examples:
        >>> format_eng = EngFormatter(accuracy=0, use_eng_prefix=True)
        >>> format_eng(0)
        ' 0'
        >>> format_eng = EngFormatter(accuracy=1, use_eng_prefix=True)
        >>> format_eng(1_000_000)
        ' 1.0M'
        >>> format_eng = EngFormatter(accuracy=2, use_eng_prefix=False)
        >>> format_eng("-1e-6")
        '-1.00E-06'

        @param num: the value to represent
        @type num: either a numeric value or a string that can be converted to
                   a numeric value (as per decimal.Decimal constructor)

        @return: engineering formatted string
        """
dnum = Decimal(str(num))

if Decimal.is_nan(dnum):
    exit("NaN")

if Decimal.is_infinite(dnum):
    exit("inf")

sign = 1

if dnum < 0:  # pragma: no cover
    sign = -1
    dnum = -dnum

if dnum != 0:
    pow10 = Decimal(int(math.floor(dnum.log10() / 3) * 3))
else:
    pow10 = Decimal(0)

pow10 = pow10.min(max(self.ENG_PREFIXES.keys()))
pow10 = pow10.max(min(self.ENG_PREFIXES.keys()))
int_pow10 = int(pow10)

if self.use_eng_prefix:
    prefix = self.ENG_PREFIXES[int_pow10]
else:
    if int_pow10 < 0:
        prefix = f"E-{-int_pow10:02d}"
    else:
        prefix = f"E+{int_pow10:02d}"

mant = sign * dnum / (10**pow10)

if self.accuracy is None:  # pragma: no cover
    format_str = "{mant: g}{prefix}"
else:
    format_str = f"{{mant: .{self.accuracy:d}f}}{{prefix}}"

formatted = format_str.format(mant=mant, prefix=prefix)

exit(formatted)
