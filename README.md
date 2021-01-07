# Image super resolution using RRDN
## Main parameters
RRDN Network architecture
The main parameters of the architecture structure are:

T - number of Residual in Residual Dense Blocks (RRDB)  
D - number of Residual Dense Blocks (RDB) insider each RRDB  
C - number of convolutional layers stacked inside a RDB  
G - number of feature maps of each convolutional layers inside the RDBs  
G0 - number of feature maps for convolutions outside of RDBs and of each RBD output  

## links
Data was downloaded from:  
https://drive.google.com/drive/u/0/folders/1H-sIY7zj42Fex1ZjxxSC3PV1pK4Mij6x

Model original:  
https://github.com/idealo/image-super-resolution#installation  

## Reproducing steps
Use `git clone https://github.com/veax-void/img_super_res` to load the code.  
Then download data and put it in to the folder 'data' near 'img_super_res' folder.  

Open 'ISR_runner.ipynb' and follow next steps:  
1) Run 'Data generation' step in this notebook, change folder paths to yours.  
2) For training run: `python train_new_models.py`   
3) For inference use 'Inference step' in this notebook  
    
All weights located at './weights', you can change parameters of the model inside 'train_new_models.py' file if needed. 