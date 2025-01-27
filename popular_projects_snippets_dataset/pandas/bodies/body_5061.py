# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_nat.py
if klass is Period and value == "":
    request.node.add_marker(
        pytest.mark.xfail(reason="Period cannot parse empty string")
    )

assert klass(value).value == iNaT
