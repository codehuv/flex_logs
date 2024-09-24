import os
import shutil
import pandas as pd

output_df = pd.read_csv('./imagenet_sorted.csv')
imagenet_folder = '/local_datasets/ILS/'


seq40_folder = os.path.join(imagenet_folder, 'seq_40')
if not os.path.exists(seq40_folder):
    os.makedirs(seq40_folder)

seq40_df = output_df[output_df['Best'].str.contains('seq = 40')]

for image_name in seq40_df['image_name']:
    source_path = os.path.join(imagenet_folder, image_name)
    destination_path = os.path.join(seq40_folder, image_name)

    if os.path.exists(source_path):
        shutil.move(source_path, destination_path)
        print(f"Moved {image_name} to seq=40 folder.")
    else:
        print(f"Image {image_name} not found.")


seq40_folder = os.path.join(imagenet_folder, 'seq_30')
if not os.path.exists(seq40_folder):
    os.makedirs(seq40_folder)

seq40_df = output_df[output_df['Best'].str.contains('seq = 30')]

for image_name in seq40_df['image_name']:
    source_path = os.path.join(imagenet_folder, image_name)
    destination_path = os.path.join(seq40_folder, image_name)

    if os.path.exists(source_path):
        shutil.move(source_path, destination_path)
        print(f"Moved {image_name} to seq=40 folder.")
    else:
        print(f"Image {image_name} not found.")


seq40_folder = os.path.join(imagenet_folder, 'seq_24')
if not os.path.exists(seq40_folder):
    os.makedirs(seq40_folder)

seq40_df = output_df[output_df['Best'].str.contains('seq = 24')]

for image_name in seq40_df['image_name']:
    source_path = os.path.join(imagenet_folder, image_name)
    destination_path = os.path.join(seq40_folder, image_name)

    if os.path.exists(source_path):
        shutil.move(source_path, destination_path)
        print(f"Moved {image_name} to seq=40 folder.")
    else:
        print(f"Image {image_name} not found.")


seq40_folder = os.path.join(imagenet_folder, 'seq_20')
if not os.path.exists(seq40_folder):
    os.makedirs(seq40_folder)

seq40_df = output_df[output_df['Best'].str.contains('seq = 20')]

for image_name in seq40_df['image_name']:
    source_path = os.path.join(imagenet_folder, image_name)
    destination_path = os.path.join(seq40_folder, image_name)

    if os.path.exists(source_path):
        shutil.move(source_path, destination_path)
        print(f"Moved {image_name} to seq=40 folder.")
    else:
        print(f"Image {image_name} not found.")


seq40_folder = os.path.join(imagenet_folder, 'seq_16')
if not os.path.exists(seq40_folder):
    os.makedirs(seq40_folder)

seq40_df = output_df[output_df['Best'].str.contains('seq = 16')]

for image_name in seq40_df['image_name']:
    source_path = os.path.join(imagenet_folder, image_name)
    destination_path = os.path.join(seq40_folder, image_name)

    if os.path.exists(source_path):
        shutil.move(source_path, destination_path)
        print(f"Moved {image_name} to seq=40 folder.")
    else:
        print(f"Image {image_name} not found.")


seq40_folder = os.path.join(imagenet_folder, 'seq_12')
if not os.path.exists(seq40_folder):
    os.makedirs(seq40_folder)

seq40_df = output_df[output_df['Best'].str.contains('seq = 12')]

for image_name in seq40_df['image_name']:
    source_path = os.path.join(imagenet_folder, image_name)
    destination_path = os.path.join(seq40_folder, image_name)

    if os.path.exists(source_path):
        shutil.move(source_path, destination_path)
        print(f"Moved {image_name} to seq=40 folder.")
    else:
        print(f"Image {image_name} not found.")


seq40_folder = os.path.join(imagenet_folder, 'seq_10')
if not os.path.exists(seq40_folder):
    os.makedirs(seq40_folder)

seq40_df = output_df[output_df['Best'].str.contains('seq = 10')]

for image_name in seq40_df['image_name']:
    source_path = os.path.join(imagenet_folder, image_name)
    destination_path = os.path.join(seq40_folder, image_name)

    if os.path.exists(source_path):
        shutil.move(source_path, destination_path)
        print(f"Moved {image_name} to seq=40 folder.")
    else:
        print(f"Image {image_name} not found.")

seq40_folder = os.path.join(imagenet_folder, 'seq_8')
if not os.path.exists(seq40_folder):
    os.makedirs(seq40_folder)

seq40_df = output_df[output_df['Best'].str.contains('seq = 8')]

for image_name in seq40_df['image_name']:
    source_path = os.path.join(imagenet_folder, image_name)
    destination_path = os.path.join(seq40_folder, image_name)

    if os.path.exists(source_path):
        shutil.move(source_path, destination_path)
        print(f"Moved {image_name} to seq=40 folder.")
    else:
        print(f"Image {image_name} not found.")

print("Image rearrangement completed.")
