# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
code = textwrap.dedent(
    """\
    from pandas import DataFrame
    df = DataFrame({"A": [1, 2]})
    df._repr_html_()

    cfg = get_ipython().config
    cfg['IPKernelApp']['parent_appname']
    df._repr_html_()
    """
)
result = ip.run_cell(code)
assert not result.error_in_exec
