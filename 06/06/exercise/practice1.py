import matplotlib.pyplot as plt
from PIL import Image
from torchvision import transforms

if __name__=="__main__":
    preprocess_1 = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])
    preprocess_2 = transforms.Compose([
        transforms.RandomHorizontalFlip(),
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.2),
        transforms.ToTensor()
    ])
    preprocess_3 = transforms.Compose([
        transforms.RandomHorizontalFlip(),
        transforms.RandomResizedCrop(224),
        transforms.ToTensor() 
    ])

    imagePath = "./exercise_data/dog_img.png"
    image = Image.open(imagePath)

    processed1Image = preprocess_1(image)
    plt.imshow(processed1Image.permute(1, 2, 0))
    plt.show()

    processed2Image = preprocess_2(image)
    plt.imshow(processed2Image.permute(1, 2, 0))
    plt.show()

    processed3Image = preprocess_3(image)
    plt.imshow(processed3Image.permute(1, 2, 0))
    plt.show()