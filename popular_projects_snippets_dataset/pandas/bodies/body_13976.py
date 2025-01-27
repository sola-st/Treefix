# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_eng_formatting.py
"""
        Parameters:
        -----------
        formatter: EngFormatter under test
        in_out: list of tuples. Each tuple = (number, expected_formatting)

        It is tested if 'formatter(number) == expected_formatting'.
        *number* should be >= 0 because formatter(-number) == fmt is also
        tested. *fmt* is derived from *expected_formatting*
        """
for input, output in in_out:
    self.compare(formatter, input, output)
    self.compare(formatter, -input, "-" + output[1:])
