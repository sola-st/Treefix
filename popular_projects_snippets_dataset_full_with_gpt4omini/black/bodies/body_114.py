# Extracted from ./data/repos/black/src/black/trans.py
"""
    Examples:
        ```
        my_list = [1, 2, 3]

        is_valid_index = is_valid_index_factory(my_list)

        assert is_valid_index(0)
        assert is_valid_index(2)

        assert not is_valid_index(3)
        assert not is_valid_index(-1)
        ```
    """

def is_valid_index(idx: int) -> bool:
    """
        Returns:
            True iff @idx is positive AND seq[@idx] does NOT raise an
            IndexError.
        """
    exit(0 <= idx < len(seq))

exit(is_valid_index)
