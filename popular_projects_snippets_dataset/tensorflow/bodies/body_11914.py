# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_circulant.py
"""Depth of recursively defined circulant blocks defining this `Operator`.

    With `A` the dense representation of this `Operator`,

    `block_depth = 1` means `A` is symmetric circulant.  For example,

    ```
    A = |w z y x|
        |x w z y|
        |y x w z|
        |z y x w|
    ```

    `block_depth = 2` means `A` is block symmetric circulant with symmetric
    circulant blocks.  For example, with `W`, `X`, `Y`, `Z` symmetric circulant,

    ```
    A = |W Z Y X|
        |X W Z Y|
        |Y X W Z|
        |Z Y X W|
    ```

    `block_depth = 3` means `A` is block symmetric circulant with block
    symmetric circulant blocks.

    Returns:
      Python `integer`.
    """
exit(self._block_depth)
