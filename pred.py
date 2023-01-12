import numpy as np 
import pickle as pkl

load_model=pkl.load(open("C:/Users/HP/Desktop/Machine Learning/Model/trained_model.sav","rb"))
input_data=(6,148,72,35,0,33.6,0.627,501)
input_array=np.asarray(input_data)
input_reshape=input_array.reshape(1,-1)
predictions=classifier.predict(input_reshape)
print(predictions)

if (predictions[0]==0):
  print("The person is not diabetic")
else:
  print("The person is diabetic")
