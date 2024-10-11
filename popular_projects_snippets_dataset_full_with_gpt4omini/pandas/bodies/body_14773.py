# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
normal_df = DataFrame(
    {
        "A": np.repeat(np.array([1, 2, 3, 4, 5]), np.array([10, 9, 8, 7, 6])),
        "B": np.repeat(np.array([1, 2, 3, 4, 5]), np.array([8, 8, 8, 8, 8])),
        "C": np.repeat(np.array([1, 2, 3, 4, 5]), np.array([6, 7, 8, 9, 10])),
    },
    columns=["A", "B", "C"],
)

nan_df = DataFrame(
    {
        "A": np.repeat(
            np.array([np.nan, 1, 2, 3, 4, 5]), np.array([3, 10, 9, 8, 7, 6])
        ),
        "B": np.repeat(
            np.array([1, np.nan, 2, 3, 4, 5]), np.array([8, 3, 8, 8, 8, 8])
        ),
        "C": np.repeat(
            np.array([1, 2, 3, np.nan, 4, 5]), np.array([6, 7, 8, 3, 9, 10])
        ),
    },
    columns=["A", "B", "C"],
)

for df in [normal_df, nan_df]:
    ax = df.plot.hist(bins=5)
    self._check_box_coord(
        ax.patches[:5],
        expected_y=np.array([0, 0, 0, 0, 0]),
        expected_h=np.array([10, 9, 8, 7, 6]),
    )
    self._check_box_coord(
        ax.patches[5:10],
        expected_y=np.array([0, 0, 0, 0, 0]),
        expected_h=np.array([8, 8, 8, 8, 8]),
    )
    self._check_box_coord(
        ax.patches[10:],
        expected_y=np.array([0, 0, 0, 0, 0]),
        expected_h=np.array([6, 7, 8, 9, 10]),
    )

    ax = df.plot.hist(bins=5, stacked=True)
    self._check_box_coord(
        ax.patches[:5],
        expected_y=np.array([0, 0, 0, 0, 0]),
        expected_h=np.array([10, 9, 8, 7, 6]),
    )
    self._check_box_coord(
        ax.patches[5:10],
        expected_y=np.array([10, 9, 8, 7, 6]),
        expected_h=np.array([8, 8, 8, 8, 8]),
    )
    self._check_box_coord(
        ax.patches[10:],
        expected_y=np.array([18, 17, 16, 15, 14]),
        expected_h=np.array([6, 7, 8, 9, 10]),
    )

    axes = df.plot.hist(bins=5, stacked=True, subplots=True)
    self._check_box_coord(
        axes[0].patches,
        expected_y=np.array([0, 0, 0, 0, 0]),
        expected_h=np.array([10, 9, 8, 7, 6]),
    )
    self._check_box_coord(
        axes[1].patches,
        expected_y=np.array([0, 0, 0, 0, 0]),
        expected_h=np.array([8, 8, 8, 8, 8]),
    )
    self._check_box_coord(
        axes[2].patches,
        expected_y=np.array([0, 0, 0, 0, 0]),
        expected_h=np.array([6, 7, 8, 9, 10]),
    )

    # horizontal
    ax = df.plot.hist(bins=5, orientation="horizontal")
    self._check_box_coord(
        ax.patches[:5],
        expected_x=np.array([0, 0, 0, 0, 0]),
        expected_w=np.array([10, 9, 8, 7, 6]),
    )
    self._check_box_coord(
        ax.patches[5:10],
        expected_x=np.array([0, 0, 0, 0, 0]),
        expected_w=np.array([8, 8, 8, 8, 8]),
    )
    self._check_box_coord(
        ax.patches[10:],
        expected_x=np.array([0, 0, 0, 0, 0]),
        expected_w=np.array([6, 7, 8, 9, 10]),
    )

    ax = df.plot.hist(bins=5, stacked=True, orientation="horizontal")
    self._check_box_coord(
        ax.patches[:5],
        expected_x=np.array([0, 0, 0, 0, 0]),
        expected_w=np.array([10, 9, 8, 7, 6]),
    )
    self._check_box_coord(
        ax.patches[5:10],
        expected_x=np.array([10, 9, 8, 7, 6]),
        expected_w=np.array([8, 8, 8, 8, 8]),
    )
    self._check_box_coord(
        ax.patches[10:],
        expected_x=np.array([18, 17, 16, 15, 14]),
        expected_w=np.array([6, 7, 8, 9, 10]),
    )

    axes = df.plot.hist(
        bins=5, stacked=True, subplots=True, orientation="horizontal"
    )
    self._check_box_coord(
        axes[0].patches,
        expected_x=np.array([0, 0, 0, 0, 0]),
        expected_w=np.array([10, 9, 8, 7, 6]),
    )
    self._check_box_coord(
        axes[1].patches,
        expected_x=np.array([0, 0, 0, 0, 0]),
        expected_w=np.array([8, 8, 8, 8, 8]),
    )
    self._check_box_coord(
        axes[2].patches,
        expected_x=np.array([0, 0, 0, 0, 0]),
        expected_w=np.array([6, 7, 8, 9, 10]),
    )
