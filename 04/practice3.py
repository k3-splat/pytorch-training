import torch

class myNN(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, my_tensor):
        conv = torch.nn.Conv2d(in_channels=3, out_channels=256, kernel_size=5, stride=8)
        _out1 = conv(my_tensor)

        batch = torch.nn.BatchNorm2d(num_features=256)
        _out2 = batch(_out1)

        relu = torch.nn.ReLU()
        _out3 = relu(_out2)

        linear = torch.nn.Linear(in_features=32, out_features=64)
        _out4 = linear(_out3)

        return _out4
    
if __name__ == "__main__":
    in_tensor = torch.ones(32, 3, 128, 128)

    model = myNN()
    _out = model(in_tensor)

    print(repr(_out.size()))