import os
import random

def randomly_delete_files(folder_path, num_files_to_delete):
    # Get a list of all files in the folder
    all_files = os.listdir(folder_path)

    # Randomly choose files to delete
    files_to_delete = random.sample(all_files, num_files_to_delete)

    # Delete the selected files
    for file_to_delete in files_to_delete:
        file_path = os.path.join(folder_path, file_to_delete)
        os.remove(file_path)
        print(f"Deleted: {file_path}")
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    your_dataset_folder = "/Users/rajveersodhi/Desktop/archive/asl_alphabet_train/asl_alphabet_train/" + letter
    num_files_to_delete = 300
    randomly_delete_files(your_dataset_folder, num_files_to_delete)

your_dataset_folder = "/Users/rajveersodhi/Desktop/archive/asl_alphabet_train/asl_alphabet_train/space"
num_files_to_delete = 300
randomly_delete_files(your_dataset_folder, num_files_to_delete)