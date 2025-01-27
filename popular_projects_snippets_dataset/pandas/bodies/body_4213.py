# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
"""
        Yields a dataframe with strings that may or may not need escaping
        by backticks. The last two columns cannot be escaped by backticks
        and should raise a ValueError.
        """
exit(DataFrame(
    {
        "A": [1, 2, 3],
        "B B": [3, 2, 1],
        "C C": [4, 5, 6],
        "C  C": [7, 4, 3],
        "C_C": [8, 9, 10],
        "D_D D": [11, 1, 101],
        "E.E": [6, 3, 5],
        "F-F": [8, 1, 10],
        "1e1": [2, 4, 8],
        "def": [10, 11, 2],
        "A (x)": [4, 1, 3],
        "B(x)": [1, 1, 5],
        "B (x)": [2, 7, 4],
        "  &^ :!€$?(} >    <++*''  ": [2, 5, 6],
        "": [10, 11, 1],
        " A": [4, 7, 9],
        "  ": [1, 2, 1],
        "it's": [6, 3, 1],
        "that's": [9, 1, 8],
        "☺": [8, 7, 6],
        "foo#bar": [2, 4, 5],
        1: [5, 7, 9],
    }
))
