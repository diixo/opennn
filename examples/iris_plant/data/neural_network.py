''' 
Artificial Intelligence Techniques SL	
artelnics@artelnics.com	

Your model has been exported to this python file.
You can manage it with the main method where you 	
can change the values of your inputs. For example:

if we want to add these 3 values (0.3, 2.5 and 1.8)
to our 3 inputs (Input_1, Input_2 and Input_1), the
main program has to look like this:

def main ():
	#default_val = 3.1416
	inputs = [None]*3
	
	Id_1 = 0.3
	Id_1 = 2.5
	Id_1 = 1.8
	
	inputs[0] = Input_1
	inputs[1] = Input_2
	inputs[2] = Input_3
	. . .


Inputs Names: 	
	0) sepal_lenght
	1) sepal_width
	2) petal_lenght
	3) petal_width


''' 


import math
import numpy as np


class NeuralNetwork:
	def __init__(self):
		self.inputs_number = 4


	def calculate_outputs(self, inputs):
		sepal_lenght = inputs[0]
		sepal_width = inputs[1]
		petal_lenght = inputs[2]
		petal_width = inputs[3]

		scaled_sepal_lenght = (sepal_lenght-5.843333244)/0.8280661106;
		scaled_sepal_width = (sepal_width-3.057333231)/0.4358662963;
		scaled_petal_lenght = (petal_lenght-3.757999897)/1.765298247;
		scaled_petal_width = (petal_width-1.19933331)/0.762237668;
		
		perceptron_layer_1_output_0 = np.tanh( 0.398424 + (scaled_sepal_lenght*0.509155) + (scaled_sepal_width*-0.755941) + (scaled_petal_lenght*1.04209) + (scaled_petal_width*1.13809) );
		perceptron_layer_1_output_1 = np.tanh( -3.23168 + (scaled_sepal_lenght*-0.176614) + (scaled_sepal_width*-0.910796) + (scaled_petal_lenght*2.20948) + (scaled_petal_width*2.42128) );
		perceptron_layer_1_output_2 = np.tanh( 0.300156 + (scaled_sepal_lenght*0.382983) + (scaled_sepal_width*0.632999) + (scaled_petal_lenght*-0.888551) + (scaled_petal_width*-1.23076) );
		
		probabilistic_layer_combinations_0 = -0.45919 -1.31559*perceptron_layer_1_output_0 -1.20404*perceptron_layer_1_output_1 +3.04406*perceptron_layer_1_output_2 ;
		probabilistic_layer_combinations_1 = 1.2198 +0.674133*perceptron_layer_1_output_0 -1.58597*perceptron_layer_1_output_1 -0.618454*perceptron_layer_1_output_2 ;
		probabilistic_layer_combinations_2 = -0.850095 +1.07785*perceptron_layer_1_output_0 +2.88505*perceptron_layer_1_output_1 -2.82181*perceptron_layer_1_output_2 ;
			
		sum = np.exp(probabilistic_layer_combinations_0) + np.exp(probabilistic_layer_combinations_1) + np.exp(probabilistic_layer_combinations_2);
		
		iris_setosa = np.exp(probabilistic_layer_combinations_0)/sum;
		iris_versicolor = np.exp(probabilistic_layer_combinations_1)/sum;
		iris_virginica = np.exp(probabilistic_layer_combinations_2)/sum;
		
		out = [None]*3
		out[0] = iris_setosa
		out[1] = iris_versicolor
		out[2] = iris_virginica

		return out;


	def main (self):
		default_val = 3.1416
		inputs = [None]*4

		sepal_lenght = default_val	#Change this value
		inputs[0] = sepal_lenght

		sepal_width = default_val	#Change this value
		inputs[1] = sepal_width

		petal_lenght = default_val	#Change this value
		inputs[2] = petal_lenght

		petal_width = default_val	#Change this value
		inputs[3] = petal_width


		outputs = NeuralNetwork.calculate_outputs(self, inputs)

		print("\nThese are your outputs:\n")
		print( "\t iris_setosa:" + str(outputs[0]) + "\n" )
		print( "\t iris_versicolor:" + str(outputs[1]) + "\n" )
		print( "\t iris_virginica:" + str(outputs[2]) + "\n" )

nn = NeuralNetwork()
nn.main()
