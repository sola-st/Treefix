# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
super(PeepholeLSTMCell, self).build(input_shape)
# The following are the weight matrices for the peephole connections. These
# are multiplied with the previous internal state during the computation of
# carry and output.
self.input_gate_peephole_weights = self.add_weight(
    shape=(self.units,),
    name='input_gate_peephole_weights',
    initializer=self.kernel_initializer)
self.forget_gate_peephole_weights = self.add_weight(
    shape=(self.units,),
    name='forget_gate_peephole_weights',
    initializer=self.kernel_initializer)
self.output_gate_peephole_weights = self.add_weight(
    shape=(self.units,),
    name='output_gate_peephole_weights',
    initializer=self.kernel_initializer)
