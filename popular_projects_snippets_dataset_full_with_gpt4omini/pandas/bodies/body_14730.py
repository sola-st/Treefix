# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# GH 32073
dates = ["2008", "2009", None, "2011", "2012"]
df = DataFrame(
    {
        "A": [1, 2, 3, 4, 5],
        "B": [1, 2, 3, 4, 5],
        "C": np.array([7, 5, np.nan, 3, 2], dtype=object),
        "D": pd.to_datetime(dates, format="%Y").view("i8"),
        "E": pd.to_datetime(dates, format="%Y", utc=True).view("i8"),
    }
)

_check_plot_works(df.plot, x="A", y="B")
_check_plot_works(df[["A", "B"]].plot, x="A", y="B")
_check_plot_works(df[["C", "A"]].plot, x="C", y="A")  # nullable value on x-axis
_check_plot_works(df[["A", "C"]].plot, x="A", y="C")
_check_plot_works(df[["B", "C"]].plot, x="B", y="C")
_check_plot_works(df[["A", "D"]].plot, x="A", y="D")
_check_plot_works(df[["A", "E"]].plot, x="A", y="E")
