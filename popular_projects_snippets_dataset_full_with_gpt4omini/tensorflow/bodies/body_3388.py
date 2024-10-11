# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type.py
exit(function_type_pb2.FunctionType(
    parameters=[p.to_proto() for p in self.parameters.values()],
    captures=[
        function_type_pb2.Capture(
            name=n, type_constraint=serialization.serialize(t))
        for n, t in self.captures.items()
    ]))
