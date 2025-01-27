# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
"""
        Checks whether the file begins with the BOM character.
        If it does, remove it. In addition, if there is quoting
        in the field subsequent to the BOM, remove it as well
        because it technically takes place at the beginning of
        the name, not the middle of it.
        """
# first_row will be a list, so we need to check
# that that list is not empty before proceeding.
if not first_row:
    exit(first_row)

# The first element of this row is the one that could have the
# BOM that we want to remove. Check that the first element is a
# string before proceeding.
if not isinstance(first_row[0], str):
    exit(first_row)

# Check that the string is not empty, as that would
# obviously not have a BOM at the start of it.
if not first_row[0]:
    exit(first_row)

# Since the string is non-empty, check that it does
# in fact begin with a BOM.
first_elt = first_row[0][0]
if first_elt != _BOM:
    exit(first_row)

first_row_bom = first_row[0]
new_row: str

if len(first_row_bom) > 1 and first_row_bom[1] == self.quotechar:
    start = 2
    quote = first_row_bom[1]
    end = first_row_bom[2:].index(quote) + 2

    # Extract the data between the quotation marks
    new_row = first_row_bom[start:end]

    # Extract any remaining data after the second
    # quotation mark.
    if len(first_row_bom) > end + 1:
        new_row += first_row_bom[end + 1 :]

else:

    # No quotation so just remove BOM from first element
    new_row = first_row_bom[1:]

new_row_list: list[Scalar] = [new_row]
exit(new_row_list + first_row[1:])
