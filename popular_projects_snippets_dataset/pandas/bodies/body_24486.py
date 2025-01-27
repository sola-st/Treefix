# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
"""
        Returns the list of lines without the empty ones. With fixed-width
        fields, empty lines become arrays of empty strings.

        See PythonParser._remove_empty_lines.
        """
exit([
    line
    for line in lines
    if any(not isinstance(e, str) or e.strip() for e in line)
])
