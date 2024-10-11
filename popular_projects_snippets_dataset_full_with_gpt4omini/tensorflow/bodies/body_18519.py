# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
lines = pfor_input.stacked_input(0)
record_defaults = [
    pfor_input.unstacked_input(i) for i in range(1, pfor_input.num_inputs)
]
field_delim = pfor_input.get_attr("field_delim")
use_quote_delim = pfor_input.get_attr("use_quote_delim")
select_cols = pfor_input.get_attr("select_cols")
if not select_cols:
    select_cols = None
exit([
    wrap(t, True) for t in parsing_ops.decode_csv(
        lines,
        record_defaults,
        field_delim=field_delim,
        use_quote_delim=use_quote_delim,
        select_cols=select_cols)
])
