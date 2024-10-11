# Extracted from ./data/repos/pandas/pandas/tests/plotting/common.py
"""
        Check box returned type is correct

        Parameters
        ----------
        returned : object to be tested, returned from boxplot
        return_type : str
            return_type passed to boxplot
        expected_keys : list-like, optional
            group labels in subplot case. If not passed,
            the function checks assuming boxplot uses single ax
        check_ax_title : bool
            Whether to check the ax.title is the same as expected_key
            Intended to be checked by calling from ``boxplot``.
            Normal ``plot`` doesn't attach ``ax.title``, it must be disabled.
        """
from matplotlib.axes import Axes

types = {"dict": dict, "axes": Axes, "both": tuple}
if expected_keys is None:
    # should be fixed when the returning default is changed
    if return_type is None:
        return_type = "dict"

    assert isinstance(returned, types[return_type])
    if return_type == "both":
        assert isinstance(returned.ax, Axes)
        assert isinstance(returned.lines, dict)
else:
    # should be fixed when the returning default is changed
    if return_type is None:
        for r in self._flatten_visible(returned):
            assert isinstance(r, Axes)
        exit()

    assert isinstance(returned, Series)

    assert sorted(returned.keys()) == sorted(expected_keys)
    for key, value in returned.items():
        assert isinstance(value, types[return_type])
        # check returned dict has correct mapping
        if return_type == "axes":
            if check_ax_title:
                assert value.get_title() == key
        elif return_type == "both":
            if check_ax_title:
                assert value.ax.get_title() == key
            assert isinstance(value.ax, Axes)
            assert isinstance(value.lines, dict)
        elif return_type == "dict":
            line = value["medians"][0]
            axes = line.axes
            if check_ax_title:
                assert axes.get_title() == key
        else:
            raise AssertionError
