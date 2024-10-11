# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
exit(distribution.experimental_local_results(
    distribution.run(train_step, args=(input_data,))))
