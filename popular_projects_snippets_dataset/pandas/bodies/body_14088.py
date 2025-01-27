# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GH #25514, 25745
with option_context("display.precision", 5):
    df = DataFrame(
        {
            "x": [
                (0.4467846931321966 + 0.0715185102060818j),
                (0.2739442392974528 + 0.23515228785438969j),
                (0.26974928742135185 + 0.3250604054898979j),
                (-1j),
            ]
        }
    )
    result = df.to_string()
    expected = (
        "                  x\n0  0.44678+0.07152j\n"
        "1  0.27394+0.23515j\n"
        "2  0.26975+0.32506j\n"
        "3 -0.00000-1.00000j"
    )
    assert result == expected
