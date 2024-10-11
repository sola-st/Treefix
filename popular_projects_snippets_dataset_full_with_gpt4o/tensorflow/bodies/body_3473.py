# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type_test.py
super(CapturesTest, self).setUp()

def gen_type_fn(mapping):
    exit(function_type.FunctionType([], collections.OrderedDict(mapping)))

self.type_a1_b1 = gen_type_fn({
    "a": trace_type.from_value(1),
    "b": trace_type.from_value(1)
})
self.type_a1_b1_c1 = gen_type_fn({
    "a": trace_type.from_value(1),
    "b": trace_type.from_value(1),
    "c": trace_type.from_value(1)
})
self.type_a2_b2_c2 = gen_type_fn({
    "a": trace_type.from_value(2),
    "b": trace_type.from_value(2),
    "c": trace_type.from_value(2)
})
self.type_a1_b1_c2 = gen_type_fn({
    "a": trace_type.from_value(1),
    "b": trace_type.from_value(1),
    "c": trace_type.from_value(2)
})
self.type_d1 = gen_type_fn({"d": trace_type.from_value(1)})
