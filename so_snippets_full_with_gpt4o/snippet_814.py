# Extracted from https://stackoverflow.com/questions/38714959/understanding-keras-lstms
        [     Step1      Step2      Step3      Step4      Step5
Tank A:    [[Pa1,Ta1], [Pa2,Ta2], [Pa3,Ta3], [Pa4,Ta4], [Pa5,Ta5]],
Tank B:    [[Pb1,Tb1], [Pb2,Tb2], [Pb3,Tb3], [Pb4,Tb4], [Pb5,Tb5]],
  ....
Tank N:    [[Pn1,Tn1], [Pn2,Tn2], [Pn3,Tn3], [Pn4,Tn4], [Pn5,Tn5]],
        ]

        [     Step1    Step2    Step3    Step4    Step5
Window  A:  [[P1,T1], [P2,T2], [P3,T3], [P4,T4], [P5,T5]],
Window  B:  [[P2,T2], [P3,T3], [P4,T4], [P5,T5], [P6,T6]],
Window  C:  [[P3,T3], [P4,T4], [P5,T5], [P6,T6], [P7,T7]],
  ....
        ]

outputs = LSTM(units, return_sequences=True)(inputs)

#output_shape -> (batch_size, steps, units)

outputs = LSTM(units)(inputs)

#output_shape -> (batch_size, units) --> steps were discarded, only the last was returned

outputs = RepeatVector(steps)(inputs) #where inputs is (batch,features)
outputs = LSTM(units,return_sequences=True)(outputs)

#output_shape -> (batch_size, steps, units)

                   BATCH 1                           BATCH 2
        [     Step1      Step2        |    [    Step3      Step4      Step5
Tank A:    [[Pa1,Ta1], [Pa2,Ta2],     |       [Pa3,Ta3], [Pa4,Ta4], [Pa5,Ta5]],
Tank B:    [[Pb1,Tb1], [Pb2,Tb2],     |       [Pb3,Tb3], [Pb4,Tb4], [Pb5,Tb5]],
  ....                                |
Tank N:    [[Pn1,Tn1], [Pn2,Tn2],     |       [Pn3,Tn3], [Pn4,Tn4], [Pn5,Tn5]],
        ]                                  ]

outputs = LSTM(units=features, 
               stateful=True, 
               return_sequences=True, #just to keep a nice output shape even with length 1
               input_shape=(None,features))(inputs) 
    #units = features because we want to use the outputs as inputs
    #None because we want variable length

#output_shape -> (batch_size, steps, units) 

input_data = someDataWithShape((batch, 1, features))

#important, we're starting new sequences, not continuing old ones:
model.reset_states()

output_sequence = []
last_step = input_data
for i in steps_to_predict:

    new_step = model.predict(last_step)
    output_sequence.append(new_step)
    last_step = new_step

 #end of the sequences
 model.reset_states()

outputs = LSTM(units=features, 
               stateful=True, 
               return_sequences=True, 
               input_shape=(None,features))(inputs) 
    #units = features because we want to use the outputs as inputs
    #None because we want variable length

#output_shape -> (batch_size, steps, units) 

totalSequences = someSequencesShaped((batch, steps, features))
    #batch size is usually 1 in these cases (often you have only one Tank in the example)

X = totalSequences[:,:-1] #the entire known sequence, except the last step
Y = totalSequences[:,1:] #one step ahead of X

#loop for resetting states at the start/end of the sequences:
for epoch in range(epochs):
    model.reset_states()
    model.train_on_batch(X,Y)

model.reset_states() #starting a new sequence
predicted = model.predict(totalSequences)
firstNewStep = predicted[:,-1:] #the last step of the predictions is the first future step

output_sequence = [firstNewStep]
last_step = firstNewStep
for i in steps_to_predict:

    new_step = model.predict(last_step)
    output_sequence.append(new_step)
    last_step = new_step

 #end of the sequences
 model.reset_states()

inputs = Input((steps,features))

#a few many to many layers:
outputs = LSTM(hidden1,return_sequences=True)(inputs)
outputs = LSTM(hidden2,return_sequences=True)(outputs)    

#many to one layer:
outputs = LSTM(hidden3)(outputs)

encoder = Model(inputs,outputs)

inputs = Input((hidden3,))

#repeat to make one to many:
outputs = RepeatVector(steps)(inputs)

#a few many to many layers:
outputs = LSTM(hidden4,return_sequences=True)(outputs)

#last layer
outputs = LSTM(features,return_sequences=True)(outputs)

decoder = Model(inputs,outputs)

inputs = Input((steps,features))
outputs = encoder(inputs)
outputs = decoder(outputs)

autoencoder = Model(inputs,outputs)

