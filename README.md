## Environment

* python=3.10.4
* torch=1.11.0
* numpy=1.22.3
* scipy=1.7.3

## Usage
Before running the code, you need to check if the “Models/” and “History/” directories exist; if not, you need to create it. Then, enter the following command in the terminal to start training the model. The training and testing logs are included in the “History/” directory.

```
python Main.py --data programmableweb --ssl1 3 --ssl2 3 --temp 0.5 --reg 3e-8 --edgeSampRate 0.1
```

* `reg`: This is the weight for weight-decay regularization.
* `ssl`: This is the weight for the solidity prediction loss of self-supervised learning task.
* `edgeSampRate`: This is the ratio of sampling edges.

## Baseline

These are the repository links for the baseline method.

https://github.com/rdz98/bprmf-pytorch

https://github.com/gusye1234/LightGCN-PyTorch

https://github.com/ruizhang-ai/GMCF_Neural_Graph_Matching_based_Collaborative_Filtering

https://github.com/PeiJieSun/diffnet

https://github.com/senllh/DHCF

https://github.com/wujcan/SGL-Torch

https://github.com/JiaHongZ/MHCNN

https://github.com/donalee/BUIR

## Achnowledgements
This work is supported by Educational Commission of Hunan Province of China under Grant No: 23A0359, and Project of Hunan Province Ordinary Higher Education Reform under Grant No. HNJG-2021-0650. The corresponding authors are Yong Xiao, and Guosheng Kang.

