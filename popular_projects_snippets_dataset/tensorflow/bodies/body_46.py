# Extracted from ./data/repos/tensorflow/tensorflow/tools/benchmark/parse_onednn_benchmarks.py
filename = sys.argv[1]
with open(filename, "r") as f:
    lines = f.readlines()
parse_results(lines)
print("Showing runtimes in microseconds. `?` means not available.")
print("%20s, %6s, %14s, %14s, %10s" %
      ("Model", "Batch", "Vanilla", "oneDNN", "Speedup"))
for model in sorted(models):
    for batch in sorted(batch_sizes):
        key = (model, batch, 0)
        eigen = db[key] if key in db else "?"
        key = (model, batch, 1)
        onednn = db[key] if key in db else "?"
        speedup = "%10.2f" % (eigen / onednn) if "?" not in (eigen,
                                                             onednn) else "?"
        print("%20s, %6d, %14s, %14s, %10s" %
              (model, batch, str(eigen), str(onednn), speedup))
