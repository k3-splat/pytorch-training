import torch
from torch.nn import Module

class MyModel(Module):
    def __init__(self, arg1 :torch.Tensor, arg2 :int, arg3 :int):
        super().__init__()
        self.mytensor = arg1
        self.elem_add = arg2
        self.elem_multiply = arg3

    def forward(self, x):
        tmp1 = x + self.mytensor
        tmp2 = tmp1 + self.elem_add
        tmp3 = tmp2 * self.elem_multiply

        return tmp1, tmp2, tmp3
    
if __name__=="__main__":
    mymodel = MyModel(torch.ones(3, 3))