# Extracted from ./data/repos/tensorflow/tensorflow/lite/tutorials/mnist_tflite.py
interpreter = tf.lite.Interpreter(model_path=flags.model_file)
interpreter.allocate_tensors()
num_correct, total = 0, 0
for input_data in test_image_generator():
    output = run_eval(interpreter, input_data[0])
    total += 1
    if output == input_data[1]:
        num_correct += 1
    if total % 500 == 0:
        print('Accuracy after %i images: %f' %
              (total, float(num_correct) / float(total)))
