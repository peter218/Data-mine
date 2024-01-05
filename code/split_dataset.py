import os
import random
import shutil


def split_dataset(image_dir, mask_dir, train_ratio=0.8):
    # 列出所有图片和对应的掩码文件
    images = sorted([f for f in os.listdir(image_dir) if f.endswith('.png')])
    masks = sorted([f for f in os.listdir(mask_dir) if f.endswith('.png')])

    # 随机打乱文件顺序
    combined = list(zip(images, masks))
    random.shuffle(combined)

    # 分割成训练集和测试集
    split_idx = int(len(combined) * train_ratio)
    train_set = combined[:split_idx]
    test_set = combined[split_idx:]

    # 可以选择创建新的文件夹来存储分割后的数据集
    os.makedirs('train_images', exist_ok=True)
    os.makedirs('train_masks', exist_ok=True)
    os.makedirs('test_images', exist_ok=True)
    os.makedirs('test_masks', exist_ok=True)

    # 将文件复制到新的文件夹
    for img, mask in train_set:
        shutil.copy(os.path.join(image_dir, img), 'train_images')
        shutil.copy(os.path.join(mask_dir, mask), 'train_masks')

    for img, mask in test_set:
        shutil.copy(os.path.join(image_dir, img), 'test_images')
        shutil.copy(os.path.join(mask_dir, mask), 'test_masks')


# 调用函数
image_dir = 'D:\\Download\\MICCAI-2023-Challenges-STS-2D-main\\MICCAI-2023-Challenges-STS-2D-main\\code\\train\\image'
mask_dir = 'D:\\Download\\MICCAI-2023-Challenges-STS-2D-main\\MICCAI-2023-Challenges-STS-2D-main\\code\\train\\mask'
split_dataset(image_dir, mask_dir)
