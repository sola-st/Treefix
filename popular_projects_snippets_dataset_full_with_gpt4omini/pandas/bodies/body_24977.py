# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
"""
        Render a DataFrame to a console-friendly tabular output.

        Parameters
        ----------
        buf : str, path object, file-like object, or None, default None
            String, path object (implementing ``os.PathLike[str]``), or file-like
            object implementing a string ``write()`` function. If None, the result is
            returned as a string.
        encoding: str, default “utf-8”
            Set character encoding.
        line_width : int, optional
            Width to wrap a line in characters.
        """
from pandas.io.formats.string import StringFormatter

string_formatter = StringFormatter(self.fmt, line_width=line_width)
string = string_formatter.to_string()
exit(save_to_buffer(string, buf=buf, encoding=encoding))
