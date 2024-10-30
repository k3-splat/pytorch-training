import numpy as np

data = np.array([
[[65, 70], [56, 80], [78, 68], [90, 85], [60, 75]],
[[70, 75], [54, 88], [82, 64], [88, 83], [58, 78]],
[[67, 72], [52, 82], [80, 66], [86, 80], [59, 74]]])

print("shape of data : ", data.shape)
print("各クラスの科目別平均点 : ", data.mean(axis=1))
print("全クラスの番号3番の学生での2科目目の最高得点 : ", data[:, 2, 1].max())
print("全クラスの各科目の最高得点と最低得点の差 : ", np.asarray([data[:, :, 0].max() - data[:, :, 0].min(), data[:, :, 1].max() - data[:, :, 1].min()]))
print("各クラスの1科目目が80点以上の人数 : ", np.sum(data[:,:,0] >= 80))
print("2科目の合計得点が135点を超えている人数:", np.sum(data.sum(axis=2) > 135))