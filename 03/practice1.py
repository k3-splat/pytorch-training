import numpy as np
import torch

data = np.array([
[[65, 70], [56, 80], [78, 68], [90, 85], [60, 75]],
[[70, 75], [54, 88], [82, 64], [88, 83], [58, 78]],
[[67, 72], [52, 82], [80, 66], [86, 80], [59, 74]]])

data_tensor = torch.tensor(data)
print(torch.Tensor.size(data_tensor))

permute_data = torch.permute(data_tensor, (2, 0, 1))
print(permute_data)

