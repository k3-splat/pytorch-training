from pathlib import Path

data_directory = "../example/data"
data_directory_path = Path(data_directory).resolve()
print("---Displaying the absolute path---")
print(data_directory_path)

file_lst = list(data_directory_path.glob("*"))
print("---files under the directory \"data\"---")
for file in file_lst:
    print(file)

print("---number of files under the directory \"data\"---")
print(len(file_lst))