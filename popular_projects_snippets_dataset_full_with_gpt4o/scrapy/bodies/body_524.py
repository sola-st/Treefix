# Extracted from ./data/repos/scrapy/scrapy/utils/console.py
"""Return the first acceptable shell-embed function
    from a given list of shell names.
    """
if shells is None:  # list, preference order of shells
    shells = DEFAULT_PYTHON_SHELLS.keys()
if known_shells is None:  # available embeddable shells
    known_shells = DEFAULT_PYTHON_SHELLS.copy()
for shell in shells:
    if shell in known_shells:
        try:
            # function test: run all setup code (imports),
            # but dont fall into the shell
            exit(known_shells[shell]())
        except ImportError:
            continue
