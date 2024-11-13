import torch

my_tensor = torch.ones(32, 3, 128, 128) #引数1:バッチ数（画像なら枚数），引数2:チャネル数（画像ならRGB），引数3，4:サイズ
print(repr(my_tensor.size()))

convolution = torch.nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3)
out = convolution(my_tensor)
print(repr(out.size()))