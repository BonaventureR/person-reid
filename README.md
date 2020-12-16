# Person Re-ID

This repo experiments with cross-data evaluation from pre-existing datasets such as Market1501 and CUKH-03 on our collected dataset. 

These experiments utilize the TorchReid Library created by Kaiyang Zhou <https://kaiyangzhou.github.io/deep-person-reid/> as a means to test Cross-Entropy and Triplet Loss Function's effects on mAP, and rank accuracies on collected datasets.

## Training Data
###### Market 1501 <https://deepai.org/dataset/market-1501>

![alt text](https://pythonawesome.com/content/images/2018/07/beyond-part-models.jpg)

Market-1501 dataset annotates 27 attributes, containing 751 identities for training and 750 for testing, that are annotated in the identity level. Thus, the file contains 27 x 751 attributes for training and 27 x 750 for test. 

These images are used for cross-data evaluation on our dataset containing two disjoint cameras in various variable environment settings (lighting, view, background).

## Ranking@10 Image Preview

## Softmax + CE Loss (Random Crop, Random Flip)
![alt text](https://github.com/BonaventureR/person-reid/blob/master/visrank_cvision_results/visrank_softmax_randomerase_dataset/visrank_cvision/0007_c2s2_0024.jpg)

### Softmax + CE Loss (Random Crop, Random Flip, Random Erase, Color Jitter)
![alt text](https://github.com/BonaventureR/person-reid/blob/master/visrank_cvision_results/visrank_softmax_randomerase_dataset_2/visrank_cvision/0003_c2s1_16.jpg)


### Triplet Loss

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

## References

[1] Hermans, A., Beyer, L., &amp; Leibe, B. (2017). In Defense of Triplet Loss for Person Re-Identification. Retrieved December 15, 2020, from https://arxiv.org/pdf/1703.07737.pdf

[2] Li, W., Zhao, R., Xiao, T., &amp; Wang, X. (2014). DeepReID: Deep Filter Pairing Neural Network for Person Re-identification. 2014 IEEE Conference on Computer Vision and Pattern Recognition. doi:10.1109/cvpr.2014.27

[3] Wang, G., Lai, J., Huang, P., &amp; Xie, X. (2018). Spatial-Temporal Person Re-identification. Retrieved December 15, 2020, from https://arxiv.org/pdf/1812.03282v1.pdf

[4] Zheng, L., Shen, L., Tian, L., Wang, S., Wang, J., &amp; Tian, Q. (2015). Scalable Person Re-Identification: A Benchmark. Retrieved December 16, 2020, from https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Zheng_Scalable_Person_Re-Identification_ICCV_2015_paper.pdf

[5] Zhong, Z., Zheng, L., Zheng, Z., Li, S., &amp; Yang, Y. (2018). Camera Style Adaptation for Person Re-identification. Retrieved December 15, 2020, from https://arxiv.org/pdf/1711.10295.pdf

[6] Li, W., Zhao, R., Xiao, T., &amp; Wang, X. (2014). DeepReID: Deep Filter Pairing Neural Network for Person Re-identification. 2014 IEEE Conference on Computer Vision and Pattern Recognition. doi:10.1109/cvpr.2014.27

[7] Hirzer, M., Beleznai, C., Roth, P., & Bischof, H. (2011). Person Re-identification by Descriptive and Discriminative Classification. SCIA.
