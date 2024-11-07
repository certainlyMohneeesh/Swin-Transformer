# run_split.py

from split_dataset import split_dataset

# Source directory containing your classes
source_dir = '/home/chemicalmyth/swin test/Swin-Transformer/Cotton Dataset/cotton'

# Destination directories for train and validation sets
train_dir = 'Cotton_Dataset/train'
val_dir = 'Cotton_Dataset/val'

# Split the dataset (80% train, 20% validation)
split_dataset(source_dir, train_dir, val_dir, split=0.8)