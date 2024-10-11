# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_building_benchmark.py
start = time.time()
for _ in range(num_iters):
    func()
end = time.time()
exit(end - start)
