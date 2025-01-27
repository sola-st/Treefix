# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/result_analyzer.py
hist, bin_edges = np.histogram(buffer)
max_num_elems = np.amax(hist)
bin_edges = ["{:.3g}".format(bin) for bin in bin_edges]
max_start_bin_width = max(len(bin) for bin in bin_edges)
max_end_bin_width = max(len(bin) for bin in bin_edges[1:])
MAX_WIDTH = 40
ret = "\n========================================================\n"
ret += "**** Output " + desc + " ****\n"
ret += "---- Histogram ----\n"
ret += "{:{width}}|  Num Elems | Visualization\n".format(
    "Bin Range", width=max_start_bin_width + max_end_bin_width + 5)
for num, bin_start, bin_end in zip(hist, bin_edges, bin_edges[1:]):
    bar = "#" * int(MAX_WIDTH * float(num) / float(max_num_elems))
    ret += ("({:<{max_start_bin_width}}, {:<{max_end_bin_width}}) | {:10} | "
            "{:}\n").format(
        bin_start,
        bin_end,
        num,
        bar,
        max_start_bin_width=max_start_bin_width,
        max_end_bin_width=max_end_bin_width,
    )
exit(ret)
