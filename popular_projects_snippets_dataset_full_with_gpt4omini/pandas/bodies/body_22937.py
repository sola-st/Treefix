# Extracted from ./data/repos/pandas/pandas/core/generic.py
r"""
        Copy object to the system clipboard.

        Write a text representation of object to the system clipboard.
        This can be pasted into Excel, for example.

        Parameters
        ----------
        excel : bool, default True
            Produce output in a csv format for easy pasting into excel.

            - True, use the provided separator for csv pasting.
            - False, write a string representation of the object to the clipboard.

        sep : str, default ``'\t'``
            Field delimiter.
        **kwargs
            These parameters will be passed to DataFrame.to_csv.

        See Also
        --------
        DataFrame.to_csv : Write a DataFrame to a comma-separated values
            (csv) file.
        read_clipboard : Read text from clipboard and pass to read_csv.

        Notes
        -----
        Requirements for your platform.

          - Linux : `xclip`, or `xsel` (with `PyQt4` modules)
          - Windows : none
          - macOS : none

        This method uses the processes developed for the package `pyperclip`. A
        solution to render any output string format is given in the examples.

        Examples
        --------
        Copy the contents of a DataFrame to the clipboard.

        >>> df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'C'])

        >>> df.to_clipboard(sep=',')  # doctest: +SKIP
        ... # Wrote the following to the system clipboard:
        ... # ,A,B,C
        ... # 0,1,2,3
        ... # 1,4,5,6

        We can omit the index by passing the keyword `index` and setting
        it to false.

        >>> df.to_clipboard(sep=',', index=False)  # doctest: +SKIP
        ... # Wrote the following to the system clipboard:
        ... # A,B,C
        ... # 1,2,3
        ... # 4,5,6

        Using the original `pyperclip` package for any string output format.

        .. code-block:: python

           import pyperclip
           html = df.style.to_html()
           pyperclip.copy(html)
        """
from pandas.io import clipboards

clipboards.to_clipboard(self, excel=excel, sep=sep, **kwargs)
