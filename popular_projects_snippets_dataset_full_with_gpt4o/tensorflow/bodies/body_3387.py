# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type.py
exit(FunctionType([Parameter.from_proto(p) for p in proto.parameters],
                    collections.OrderedDict([
                        (c.name,
                         serialization.deserialize(c.type_constraint))
                        for c in proto.captures
                    ])))
