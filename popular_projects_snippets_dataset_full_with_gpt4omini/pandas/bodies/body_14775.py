# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
import matplotlib.pyplot as plt

fig = plt.gcf()

df = DataFrame(np.random.randn(100, 3))
for markers in [
    {0: "^", 1: "+", 2: "o"},
    {0: "^", 1: "+"},
    ["^", "+", "o"],
    ["^", "+"],
]:
    fig.clf()
    fig.add_subplot(111)
    ax = df.plot(style=markers)
    for idx, line in enumerate(ax.get_lines()[: len(markers)]):
        assert line.get_marker() == markers[idx]
