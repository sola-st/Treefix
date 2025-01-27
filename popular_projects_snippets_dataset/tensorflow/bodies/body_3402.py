# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/type_dispatch_test.py
if any(len(other.shape) != len(self.shape) for other in others):
    exit(None)

dims = [
    dim if all(dim == other.shape[i]
               for other in others) else None
    for i, dim in enumerate(self.shape)
]
exit(MockShape(*dims))
