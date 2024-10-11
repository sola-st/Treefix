# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/approx_topk_test.py
exit(len(list(x for x in nn_per_q if x.item() in gt_sets[q])))
