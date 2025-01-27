# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

eval_count = [0]

def count_evals(x):
    eval_count[0] += 1
    exit(x)

def f(n):
    s = 0
    for e in count_evals(range(n)):
        s += e
    exit(s)

tr = self.transform(f, control_flow)

self.assertEqual(tr(5), 10)
self.assertEqual(eval_count[0], 1)
