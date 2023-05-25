# model_building.py
# Author: Adam Messick
# Date: 5/24/2023

import torch
from torch import nn

class TwoLayerNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        """
        In the constructor we instantiate two nn.Linear modules and assign them as
        member variables.
        """
        super(TwoLayerNet, self).__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.linear2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        """
        In the forward function we accept a Tensor of input data and we must return
        a Tensor of output data. We can use Modules defined in the constructor as
        well as arbitrary operators on Tensors.
        """
        h_relu = self.linear1(x).clamp(min=0)
        y_pred = self.linear2(h_relu)
        return y_pred

def create_neural_network(input_size, hidden_size, output_size):
    """Create a two-layer neural network using PyTorch"""
    try:
        net = TwoLayerNet(input_size, hidden_size, output_size)
        return net
    except Exception as e:
        print(f"An error occurred while creating the neural network: {e}")

if __name__ == "__main__":
    # An example of using the network
    N, D_in, H, D_out = 64, 1000, 100, 10

    # Create random Tensors to hold inputs and outputs
    x = torch.randn(N, D_in)
    y = torch.randn(N, D_out)

    # Construct our model by instantiating the class defined above
    model = create_neural_network(D_in, H, D_out)

    # Forward pass: Compute predicted y by passing x to the model
    y_pred = model(x)
