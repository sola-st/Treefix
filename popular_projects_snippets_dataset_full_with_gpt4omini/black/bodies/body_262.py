# Extracted from ./data/repos/black/src/black/handle_ipynb_magics.py
try:
    import IPython  # noqa:F401
    import tokenize_rt  # noqa:F401
except ModuleNotFoundError:
    if verbose or not quiet:
        msg = (
            "Skipping .ipynb files as Jupyter dependencies are not installed.\n"
            'You can fix this by running ``pip install "black[jupyter]"``'
        )
        out(msg)
    exit(False)
else:
    exit(True)
