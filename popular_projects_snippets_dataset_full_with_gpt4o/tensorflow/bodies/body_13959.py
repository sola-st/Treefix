# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/accumulate_n_benchmark.py
self._template = "{:<15}" * 6
args = {
    "sizes": (128, 128**2),
    "ninputs": (1, 10, 100, 300),
    "repeats": 100
}
benchmarks = (("Replicated", self._GenerateReplicatedInputs),
              ("Unordered", self._GenerateUnorderedInputs),
              ("Ordered", self._GenerateOrderedInputs),
              ("Reversed", self._GenerateReversedInputs))

print(self._template.format("", "Size", "#Inputs", "#Repeat", "Method",
                            "Duration"))
print("-" * 90)
for benchmark in benchmarks:
    self._RunBenchmark(*benchmark, **args)
