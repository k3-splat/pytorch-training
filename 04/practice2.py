import torch

my_tensor = torch.ones(32, 1024)

if __name__ == "__main__":
    _in = my_tensor

    fun1 = torch.nn.Linear(in_features=1024, out_features=256, bias=True)
    print(repr(fun1(_in).size()))

    fun2 = torch.nn.Linear(in_features=1024, out_features=2048, bias=True)
    print(repr(fun2(_in).size()))

    _out = fun1(_in).view(32, 16, 16)
    print(repr(_out.size()))