# Extracted from ./data/repos/pandas/pandas/_testing/asserters.py
import matplotlib.pyplot as plt

if isinstance(objs, (Series, np.ndarray)):
    for el in objs.ravel():
        msg = (
            "one of 'objs' is not a matplotlib Axes instance, "
            f"type encountered {repr(type(el).__name__)}"
        )
        assert isinstance(el, (plt.Axes, dict)), msg
else:
    msg = (
        "objs is neither an ndarray of Artist instances nor a single "
        "ArtistArtist instance, tuple, or dict, 'objs' is a "
        f"{repr(type(objs).__name__)}"
    )
    assert isinstance(objs, (plt.Artist, tuple, dict)), msg
