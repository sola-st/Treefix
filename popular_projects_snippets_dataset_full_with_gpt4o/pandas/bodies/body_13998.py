# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_css.py
color, style, width = expected

assert_resolves(
    f"border-left: {prop}",
    {
        "border-left-color": color,
        "border-left-style": style,
        "border-left-width": width,
    },
)
