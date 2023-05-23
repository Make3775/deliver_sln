# Instructions on how to execute the code

- Ensure that Python3, pytorch, torchvision, torchaudio is installed and a virtual environment has been setup

- OpenCv has to be installed, PLI(available in conda and pip). (Use pip or conda)

- Ensure that the HMDB51 datasets have been downloaded and also the train_test_splits file available on the SerreLabs domain

- Extract the HMDB51 contents from rar to folder to fetch the action videos

- Extract the splits file too to its own folder

- store the folders in the same directory as the python files given

- To extract frames from a given action, just change the path in the main execution function in the `extract.py` file and run the code below

    `python extract.py`

- To train, test, validate an action and splits, execute

    `python all_functions_c_tst_train_val.py`

- necessary files are created. To load a file:

    `np.loadtxt('action.txt')` eg. np.loadtxt('test_data.txt')