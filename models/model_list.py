import torch
import torch.nn as nn

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(
                in_channels=1,
                out_channels=16,
                kernel_size=5,
                stride=1,
                padding=2,
            ),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(16, 32, 5, 1, 2),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )
        # fully connected layer, output 10 classes
        self.out = nn.Linear(32 * 7 * 7, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)        # flatten the output of conv2 to (batch_size, 32 * 7 * 7)
        x = x.view(x.size(0), -1)
        output = self.out(x)
        return output#, x    # return x for visualization

def get_model(model_name):
    if model_name == "SimpleCNN":
        return SimpleCNN()
    else:
        print("No model specified in experiment file. Using SimpleCNN.")
        return SimpleCNN()

def get_model_global(model_name):
    try:
        model = globals()[model_name]()
        print(f"Using {model_name} model")
    except:
        print("Invalid model specified in experiment file. Using SimpleCNN.")
        model = SimpleCNN()

    return model