

# In[2]:


import os
import cv2
import numpy as np
import time


# In[19]:


def total_files():
    total = 0
    for i in MAIN_DIR:
        train_test_base = os.path.join(BASE, DATASET_FOLDER_NAME, i) 
        train_test_dir = os.listdir(train_test_base)
        for j in train_test_dir:
            labeled_dir_path = os.path.join(train_test_base, j) 
            all_img = os.listdir(labeled_dir_path)
            total += len(all_img)
    print(f'Total files are {total}')


# In[20]:


target = []
data = []
data_map = {
    'with_mask':1,
    'without_mask':0
}
skipped = 0

BASE = ""
DATASET_FOLDER_NAME = 'Dataset'
IGNORE_FILES = ['README.md']
img_shape = 50


# In[22]:



MAIN_DIR = os.listdir(os.path.join(BASE, DATASET_FOLDER_NAME))
for ignore_file in IGNORE_FILES:
    MAIN_DIR.remove(ignore_file)
    
total_files()
for i in MAIN_DIR:
    train_test_base = os.path.join(BASE, DATASET_FOLDER_NAME, i) 
    train_test_dir = os.listdir(train_test_base) 
    for j in train_test_dir:
        labeled_dir_path = os.path.join(train_test_base, j) 
        all_img = os.listdir(labeled_dir_path) 
        print(f'\nExecuting - {i}/{j}')
        for k in all_img:
            image_path = os.path.join(labeled_dir_path, k)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            try:
                
                image = cv2.resize(image,(img_shape,img_shape))
            except Exception as E:
                skipped += 1
                print(E)
                continue
            data.append(image)
            target.append(data_map[j])
print(f'\n{skipped} files skipped.')

with open(r'Training/data.npy','wb') as file:
    np.save(file,np.array(data))
    print('\nData file saved.')
    
with open(r'Training/target.npy','wb') as file:
    np.save(file,np.array(target))
    print('Target file saved.')

print('\nFinished')
time.sleep(6000)




