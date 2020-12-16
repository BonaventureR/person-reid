# Person Re-ID

This repo experiments with cross-data evaluation from pre-existing datasets such as Market1501 and CUKH-03 on our collected dataset. 

These experiments utilize the TorchReid Library created by Kaiyang Zhou <https://kaiyangzhou.github.io/deep-person-reid/> as a means to test Cross-Entropy and Triplet Loss Function's effects on mAP, and rank accuracies on collected datasets.

## Training Data
### Market 1501 <https://deepai.org/dataset/market-1501>

![alt text](https://pythonawesome.com/content/images/2018/07/beyond-part-models.jpg)

Market-1501 dataset annotates 27 attributes, containing 751 identities for training and 750 for testing, that are annotated in the identity level. Thus, the file contains 27 x 751 attributes for training and 27 x 750 for test. 

These images are used for cross-data evaluation on our dataset containing two disjoint cameras in various variable environment settings (lighting, view, background).

## Image of Rank@5 Outputs

## Softmax + CE Loss (Random Crop, Random Flip)
![alt text](https://github.com/BonaventureR/person-reid/blob/master/visrank_cvision_results/visrank_softmax_randomerase_dataset/visrank_cvision/0007_c2s2_0024.jpg)

## Softmax + CE Loss (Random Crop, Random Flip, Random Erase, Color Jitter)
![alt text](https://github.com/BonaventureR/person-reid/blob/master/visrank_cvision_results/visrank_softmax_randomerase_dataset_2/visrank_cvision/0003_c2s1_16.jpg)


## Triplet Loss

![alt text](https://github.com/BonaventureR/person-reid/blob/master/visrank_cvision_results/visrank_triplet_dataset/visrank_cvision/0005_c2s1_12.jpg)

But also, performed poorly in some examples, 


![alt text](https://github.com/BonaventureR/person-reid/blob/master/visrank_cvision_results/visrank_softmax_randomerase_dataset/visrank_cvision/0002_c1s2_0164.jpg)


![alt text](https://github.com/BonaventureR/person-reid/blob/master/visrank_cvision_results/visrank_softmax_randomerase_dataset/visrank_cvision/0001_c1s1_03.jpg)


## Evaluation

|             | Softmax+CLE (Crop, Flip)     | Softmax+CLE(Crop, Flip, CJitter, Patch)     | TripletLoss (Crop, Flip)     |
|:-------:    |:------------------------:    |:---------------------------------------:    |:------------------------:    |
|   mAP       |           45.6%              |                  42.9%                      |           45.8%              |
|  Rank@1     |           10.1%              |                  35.9%                      |           12.7%              |
|  Rank@5     |           25.3%              |                  66.7%                      |           30.4%              |
| Rank@10     |           53.2%              |                  79.5%                      |           51.9%              |
| Rank@20     |           63.3%              |                  84.6%                      |           67.1%              |

