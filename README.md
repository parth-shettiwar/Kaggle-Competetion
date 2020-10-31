Platform - Kaggle
First take the train_dataset(which has 3 subfolders - aircrafts, ships, none) and run the code imagetonpy.py(present inside the train folder)
Train dataset should be in train folder.
Following paths should be there and should contain images.
train/aircrafts/*.png
train/none/*.png
train/ships/*.png
A npy file will be generated having the feature vectors in a np array.
Now upload the generated 'train_data.npy' file to kaggle notebook under title train_data.

Take the 'test' folder containing images and upload it directly to notebook under the title test_data.
Folder path - test/*.png

Now run all the cells.In the end a link will be created for "Download_csv" which will download a csv file having the image name and their corresponding labels.

I have done the testing and training in a single ipynb file which I have zipped.In addition I have added the imagetonpy.py file and readme.txt.
The basic architecture consists of 5 conv layers, pool layer, flatten, and  3 fully connected layer. Epochs 100 - takes about 3-4 min to train on kaggle GPU


