
# C-NERF: Representing Scene Changes as Directional Consistency Difference-based NeRF
 
## Installation
```
git clone https://github.com/C-NeRF/C-NeRF.git
cd C-NeRF
conda create -n cnerf python=3.7
conda activate cnerf
pip install -r requirements.txt
```

## Download NeRF models 
 You can download the pre-trained models from [drive](https://drive.google.com/file/d/1rtmWgOIrOKVGO6ls3WGmQeaGCEEaifap/view?usp=sharing). Unzip the logs to the project root dir to save training time. 


## Download Demo Dataset
 You can download the demo datasets from [drive](https://drive.google.com/file/d/11iEnLMk43oTx0CmMBofdkLmZNdnDDHJP/view). Unzip the downloaded data to the project root dir in order to train. 


## Obtain CD Results
First download trained NeRF Models and dataset. Then, 
```
bash C-NeRF.sh
```
This command will obtain the render images with change markers, the results are saved to `./logs/chess1/results_path_199999`


## Train NeRF models before and after scene change
First download the dataset. Then,
```
python run_nerf.py --config configs/chess1.txt
python run_nerf.py --config configs/chess2.txt
```


