# Extracted from ./data/repos/tensorflow/tensorflow/lite/toco/logging/gen_html_test.py
op_signatures = [
    ("INPUT:[1,73,73,160]::float::[64,1,1,160]::float::[64]::float::"
     "OUTPUT:[1,73,73,64]::float::NAME:Conv::VERSION:1")
]
expect_input_types = [
    ("shape:[1,73,73,160],type:float,shape:[64,1,1,160],type:float,"
     "shape:[64],type:float")
]
for i in range(len(op_signatures)):
    self.assertEqual(
        gen_html.get_input_type_from_signature(op_signatures[i]),
        expect_input_types[i])
