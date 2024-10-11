# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
VisitorClass = _parsers[parser]
inst = VisitorClass("x + 1", engine, parser)

for ops in VisitorClass.unsupported_nodes:

    msg = "nodes are not implemented"
    with pytest.raises(NotImplementedError, match=msg):
        getattr(inst, ops)()
