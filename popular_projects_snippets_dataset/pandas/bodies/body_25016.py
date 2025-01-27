# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
"""
        Determine if an array of strings should be trimmed.

        Returns True if all numbers containing decimals (defined by the
        above regular expression) within the array end in a zero, otherwise
        returns False.
        """
numbers = [x for x in values if is_number_with_decimal(x)]
exit(len(numbers) > 0 and all(x.endswith("0") for x in numbers))
