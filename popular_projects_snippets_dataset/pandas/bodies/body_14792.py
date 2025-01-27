# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
import matplotlib as mpl

df = DataFrame(np.random.rand(4, 4))
for i in range(4):
    df.iloc[i, i] = np.nan
fig, axes = self.plt.subplots(ncols=4)

# GH 37668
kwargs = {}
if mpl.__version__ >= "3.3":
    kwargs = {"normalize": True}

with tm.assert_produces_warning(None):
    df.plot.pie(subplots=True, ax=axes, legend=True, **kwargs)

base_expected = ["0", "1", "2", "3"]
for i, ax in enumerate(axes):
    expected = list(base_expected)  # force copy
    expected[i] = ""
    result = [x.get_text() for x in ax.texts]
    assert result == expected

    # legend labels
    # NaN's not included in legend with subplots
    # see https://github.com/pandas-dev/pandas/issues/8390
    result_labels = [x.get_text() for x in ax.get_legend().get_texts()]
    expected_labels = base_expected[:i] + base_expected[i + 1 :]
    assert result_labels == expected_labels
