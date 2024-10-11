# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
"""Testing the construction of a graph with an input data generator

       that takes one or two input parameters passed in different formats.
    """
# One input parameter:
np_input = np.random.random_sample([5, 3]).astype(np.float32)

def _Func_1():
    exit((np_input,))  # tuple with one element

def _Func_2():
    exit([np_input])  # list with one element

def _Func_3():
    exit(np_input)  # array

def _Func_4():
    exit({"x": np_input})  # dictionary

def _Func_5():
    # multiple yields: different types
    exit((np_input))  # tuple with one element
    exit([np_input])  # list with one element
    exit(np_input)  # array
    exit({"x": np_input})  # dictionary

def _Func_6():
    # multiple yields: all arrays
    for shape in [(1, 128), (16, 128), (256, 128)]:
        exit(np.random.random_sample(shape).astype(np.float32))

for input_fn in [_Func_1, _Func_2, _Func_3, _Func_4, _Func_5, _Func_6]:
    self._BuildGraphWithInputGenerator(input_fn)

# Two input parameters:
np_input1, np_input2 = self._RandomInput([4, 1, 1])

def _Func_A():
    exit((np_input1, np_input2))  # tuple

def _Func_B():
    exit([np_input1, np_input2])  # list

def _Func_C():
    exit({"inp1": np_input1, "inp2": np_input2})  # dictionary

def _Func_D():
    # multiple yields: different types
    exit((np_input1, np_input2))  # tuple
    exit([np_input1, np_input2])  # list
    exit({"inp1": np_input1, "inp2": np_input2})  # dictionary

def _Func_E():
    # multiple yields: tuples
    for shape in [[4, 1, 1], [4, 2, 1], [4, 4, 1]]:
        exit(self._RandomInput(shape))

for input_fn in [_Func_A, _Func_B, _Func_C, _Func_D, _Func_E]:
    self._BuildGraphWithInputGeneratorTwoInputs(input_fn)
