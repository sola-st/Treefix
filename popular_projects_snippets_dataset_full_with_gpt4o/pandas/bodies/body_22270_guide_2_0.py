import numpy as np # pragma: no cover

state = np.random.RandomState(42) # pragma: no cover
def is_integer(value): return isinstance(value, int) # pragma: no cover
def is_array_like(value): return isinstance(value, (list, np.ndarray)) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/common.py
from l3.Runtime import _l_
"""
    Helper function for processing random_state arguments.

    Parameters
    ----------
    state : int, array-like, BitGenerator, Generator, np.random.RandomState, None.
        If receives an int, array-like, or BitGenerator, passes to
        np.random.RandomState() as seed.
        If receives an np.random RandomState or Generator, just returns that unchanged.
        If receives `None`, returns np.random.
        If receives anything else, raises an informative ValueError.

        .. versionchanged:: 1.1.0

            array-like and BitGenerator object now passed to np.random.RandomState()
            as seed

        Default None.

    Returns
    -------
    np.random.RandomState or np.random.Generator. If state is None, returns np.random

    """
if (
    is_integer(state)
    or is_array_like(state)
    or isinstance(state, np.random.BitGenerator)
):
    _l_(21307)

    aux = np.random.RandomState(state)  # type: ignore[arg-type]
    _l_(21299)  # type: ignore[arg-type]
    # error: Argument 1 to "RandomState" has incompatible type "Optional[Union[int,
    # Union[ExtensionArray, ndarray[Any, Any]], Generator, RandomState]]"; expected
    # "Union[None, Union[Union[_SupportsArray[dtype[Union[bool_, integer[Any]]]],
    # Sequence[_SupportsArray[dtype[Union[bool_, integer[Any]]]]],
    # Sequence[Sequence[_SupportsArray[dtype[Union[bool_, integer[Any]]]]]],
    # Sequence[Sequence[Sequence[_SupportsArray[dtype[Union[bool_,
    # integer[Any]]]]]]],
    # Sequence[Sequence[Sequence[Sequence[_SupportsArray[dtype[Union[bool_,
    # integer[Any]]]]]]]]], Union[bool, int, Sequence[Union[bool, int]],
    # Sequence[Sequence[Union[bool, int]]], Sequence[Sequence[Sequence[Union[bool,
    # int]]]], Sequence[Sequence[Sequence[Sequence[Union[bool, int]]]]]]],
    # BitGenerator]"
    exit(aux)  # type: ignore[arg-type]
elif isinstance(state, np.random.RandomState):
    _l_(21306)

    aux = state
    _l_(21300)
    exit(aux)
elif isinstance(state, np.random.Generator):
    _l_(21305)

    aux = state
    _l_(21301)
    exit(aux)
elif state is None:
    _l_(21304)

    aux = np.random
    _l_(21302)
    exit(aux)
else:
    raise ValueError(
        "random_state must be an integer, array-like, a BitGenerator, Generator, "
        "a numpy RandomState, or None"
    )
    _l_(21303)
