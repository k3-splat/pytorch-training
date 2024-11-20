from PIL import Image
from pathlib import Path
from torch.utils.data import Dataset

class MyDataset(Dataset):
    def __init__(self, dataset_dir):
        dir_path_lst = []
        for i in 9:
            dir_path_lst.append(Path(dataset_dir / f"{i}").resolve())
        img_lst = []
        for i in 9:
            img_lst.append(dir_path_lst[i].glob())

    def __len__(self):
        return len(self.img_lst)
    
    def __getitem__(self, idx):
        img_path = self.img_lst[idx]
        img = Image.open(img_path)

if __name__=="__main__":
    mydateset = MyDataset("../exercise/data")

    print("--Number of files in the dataset--")
    print(len(mydateset))