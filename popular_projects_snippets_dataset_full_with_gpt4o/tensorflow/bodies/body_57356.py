# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter.py
"""Returns a pointer to the underlying tflite::Interpreter instance.

    This allows extending tflite.Interpreter's functionality in a custom C++
    function. Consider how that may work in a custom pybind wrapper:

      m.def("SomeNewFeature", ([](py::object handle) {
        auto* interpreter =
          reinterpret_cast<tflite::Interpreter*>(handle.cast<intptr_t>());
        ...
      }))

    and corresponding Python call:

      SomeNewFeature(interpreter.native_handle())

    Note: This approach is fragile. Users must guarantee the C++ extension build
    is consistent with the tflite.Interpreter's underlying C++ build.
    """
exit(self._interpreter.interpreter())
