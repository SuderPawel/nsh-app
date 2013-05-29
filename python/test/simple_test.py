from main.network import network
from main.function import activation
from main.simple import neuron_not, neuron_or

__author__ = 'paoolo'


def neuron_and():
    return network.Neuron(activation.threshold_unipolar(), [2.8147, 1.9058], 3.7460)


def neuron_xor():
    hidden_neuron1 = network.Neuron(activation.sigmoid_bipolar(), [0.7827, 0.7725], 0.3666)
    hidden_neuron2 = network.Neuron(activation.sigmoid_bipolar(), [1.4412, 1.3907], -1.5368)
    hidden_layer = network.Layer([hidden_neuron1, hidden_neuron2])
    output_neuron = network.Neuron(activation.linear(), [-1.2556, 1.3087], 0.8297)
    output_layer = network.Layer([output_neuron])
    return network.Network([hidden_layer, output_layer])


def quick_test():
    neurons = [neuron_and(), neuron_or(), neuron_and(), neuron_xor()]
    for neuron in neurons:
        print neuron
        for val in [(0., 0.), (1., 0.), (0., 1.), (1., 1.)]:
            print '\t' + str(neuron.compute(val))
    neuron = neuron_not()
    print neuron
    for val in [0, 1]:
        print '\t' + str(neuron.compute([val]))
