# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# Issue #9764

# In case default display precision changes:
with option_context("display.precision", 6):
    # DataFrame example from issue #9764
    d = DataFrame(
        {
            "col1": [
                9.999e-8,
                1e-7,
                1.0001e-7,
                2e-7,
                4.999e-7,
                5e-7,
                5.0001e-7,
                6e-7,
                9.999e-7,
                1e-6,
                1.0001e-6,
                2e-6,
                4.999e-6,
                5e-6,
                5.0001e-6,
                6e-6,
            ]
        }
    )

    expected_output = {
        (0, 6): "           col1\n"
        "0  9.999000e-08\n"
        "1  1.000000e-07\n"
        "2  1.000100e-07\n"
        "3  2.000000e-07\n"
        "4  4.999000e-07\n"
        "5  5.000000e-07",
        (1, 6): "           col1\n"
        "1  1.000000e-07\n"
        "2  1.000100e-07\n"
        "3  2.000000e-07\n"
        "4  4.999000e-07\n"
        "5  5.000000e-07",
        (1, 8): "           col1\n"
        "1  1.000000e-07\n"
        "2  1.000100e-07\n"
        "3  2.000000e-07\n"
        "4  4.999000e-07\n"
        "5  5.000000e-07\n"
        "6  5.000100e-07\n"
        "7  6.000000e-07",
        (8, 16): "            col1\n"
        "8   9.999000e-07\n"
        "9   1.000000e-06\n"
        "10  1.000100e-06\n"
        "11  2.000000e-06\n"
        "12  4.999000e-06\n"
        "13  5.000000e-06\n"
        "14  5.000100e-06\n"
        "15  6.000000e-06",
        (9, 16): "        col1\n"
        "9   0.000001\n"
        "10  0.000001\n"
        "11  0.000002\n"
        "12  0.000005\n"
        "13  0.000005\n"
        "14  0.000005\n"
        "15  0.000006",
    }

    for (start, stop), v in expected_output.items():
        assert str(d[start:stop]) == v
