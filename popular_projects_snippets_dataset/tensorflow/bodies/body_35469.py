# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/multinomial_op_test.py
num_iters = 50
print("Composition of existing ops vs. Native Multinomial op [%d iters]" %
      num_iters)
print("BatchSize\tNumClasses\tNumSamples\tsec(composed)\tsec(native)\t"
      "speedup")

for batch_size in [32, 128]:
    for num_classes in [10000, 100000]:
        for num_samples in [1, 4, 32]:
            n_dt, c_dt = native_op_vs_composed_ops(batch_size, num_classes,
                                                   num_samples, num_iters)
            print("%d\t%d\t%d\t%.3f\t%.3f\t%.2f" % (batch_size, num_classes,
                                                    num_samples, c_dt, n_dt,
                                                    c_dt / n_dt))

            self.report_benchmark(
                name="native_batch%d_classes%d_s%d" %
                (batch_size, num_classes, num_samples),
                iters=num_iters,
                wall_time=n_dt)
            self.report_benchmark(
                name="composed_batch%d_classes%d_s%d" %
                (batch_size, num_classes, num_samples),
                iters=num_iters,
                wall_time=c_dt)
