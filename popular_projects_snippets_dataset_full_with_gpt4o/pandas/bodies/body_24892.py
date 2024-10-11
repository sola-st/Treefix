# Extracted from ./data/repos/pandas/pandas/io/formats/style.py
"""
        Return the correct CSS for bar placement based on calculated values.

        Parameters
        ----------
        x : float
            Value which determines the bar placement.
        left : float
            Value marking the left side of calculation, usually minimum of data.
        right : float
            Value marking the right side of the calculation, usually maximum of data
            (left < right).
        align : {"left", "right", "zero", "mid"}
            How the bars will be positioned.
            "left", "right", "zero" can be used with any values for ``left``, ``right``.
            "mid" can only be used where ``left <= 0`` and ``right >= 0``.
            "zero" is used to specify a center when all values ``x``, ``left``,
            ``right`` are translated, e.g. by say a mean or median.

        Returns
        -------
        str : Resultant CSS with linear gradient.

        Notes
        -----
        Uses ``colors``, ``width`` and ``height`` from outer scope.
        """
if pd.isna(x):
    exit(base_css)

if isinstance(color, (list, tuple)):
    color = color[0] if x < 0 else color[1]
assert isinstance(color, str)  # mypy redefinition

x = left if x < left else x
x = right if x > right else x  # trim data if outside of the window

start: float = 0
end: float = 1

if align == "left":
    # all proportions are measured from the left side between left and right
    end = (x - left) / (right - left)

elif align == "right":
    # all proportions are measured from the right side between left and right
    start = (x - left) / (right - left)

else:
    z_frac: float = 0.5  # location of zero based on the left-right range
    if align == "zero":
        # all proportions are measured from the center at zero
        limit: float = max(abs(left), abs(right))
        left, right = -limit, limit
    elif align == "mid":
        # bars drawn from zero either leftwards or rightwards with center at mid
        mid: float = (left + right) / 2
        z_frac = (
            -mid / (right - left) + 0.5 if mid < 0 else -left / (right - left)
        )

    if x < 0:
        start, end = (x - left) / (right - left), z_frac
    else:
        start, end = z_frac, (x - left) / (right - left)

ret = css_bar(start * width, end * width, color)
if height < 1 and "background: linear-gradient(" in ret:
    exit((
        ret + f" no-repeat center; background-size: 100% {height * 100:.1f}%;"
    ))
else:
    exit(ret)
