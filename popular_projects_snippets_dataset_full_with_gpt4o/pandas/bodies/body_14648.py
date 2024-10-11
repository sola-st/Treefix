# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
import matplotlib.pyplot as plt

fig = plt.gcf()

try:
    plt.clf()
    ax = fig.add_subplot(211)
    orig_ax = kwargs.pop("ax", plt.gca())
    orig_axfreq = getattr(orig_ax, "freq", None)

    ret = f(*args, **kwargs)
    assert ret is not None  # do something more intelligent

    ax = kwargs.pop("ax", plt.gca())
    if series is not None:
        dfreq = series.index.freq
        if isinstance(dfreq, BaseOffset):
            dfreq = dfreq.rule_code
        if orig_axfreq is None:
            assert ax.freq == dfreq

    if freq is not None and orig_axfreq is None:
        assert ax.freq == freq

    ax = fig.add_subplot(212)
    kwargs["ax"] = ax
    ret = f(*args, **kwargs)
    assert ret is not None  # TODO: do something more intelligent

    with tm.ensure_clean(return_filelike=True) as path:
        plt.savefig(path)

    # GH18439, GH#24088, statsmodels#4772
    with tm.ensure_clean(return_filelike=True) as path:
        pickle.dump(fig, path)
finally:
    plt.close(fig)
