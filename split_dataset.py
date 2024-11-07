# split_dataset.py

import os
import shutil
import random

def split_dataset(source_dir, train_dir, val_dir, split=0.8):
    for class_name in os.listdir(source_dir):
        class_dir = os.path.join(source_dir, class_name)
        if not os.path.isdir(class_dir):
            continue

        # Create directories for this class in train and val
        train_class_dir = os.path.join(train_dir, class_name)
        val_class_dir = os.path.join(val_dir, class_name)
        os.makedirs(train_class_dir, exist_ok=True)
        os.makedirs(val_class_dir, exist_ok=True)

        # Get all image files
        images = [f for f in os.listdir(class_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
        
        # Shuffle the images
        random.shuffle(images)

        # Split point
        split_point = int(len(images) * split)

        # Copy images to train and val directories
        for img in images[:split_point]:
            shutil.copy(os.path.join(class_dir, img), train_class_dir)
        for img in images[split_point:]:
            shutil.copy(os.path.join(class_dir, img), val_class_dir)

    print("Dataset splitting completed!")