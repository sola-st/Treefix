# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
"""
        Alert a user about a malformed row, depending on value of
        `self.on_bad_lines` enum.

        If `self.on_bad_lines` is ERROR, the alert will be `ParserError`.
        If `self.on_bad_lines` is WARN, the alert will be printed out.

        Parameters
        ----------
        msg: str
            The error message to display.
        row_num: int
            The row number where the parsing error occurred.
            Because this row number is displayed, we 1-index,
            even though we 0-index internally.
        """
if self.on_bad_lines == self.BadLineHandleMethod.ERROR:
    raise ParserError(msg)
if self.on_bad_lines == self.BadLineHandleMethod.WARN:
    base = f"Skipping line {row_num}: "
    sys.stderr.write(base + msg + "\n")
