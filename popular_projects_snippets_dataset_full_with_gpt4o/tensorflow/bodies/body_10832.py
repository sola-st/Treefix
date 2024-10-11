# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
others_msg = ("Implementation error: "
              "selected default action #%d was called, but some of other "
              "predicates are True: " % k)
default_msg = ("Input error: "
               "None of conditions evaluated as True:",
               array_ops.stack(predicates, name="preds_c"))
with ops.control_dependencies([
    _assert_at_most_n_true(other_predicates, n=0, msg=others_msg),
    Assert(predicate, data=default_msg)
]):
    exit(action())
