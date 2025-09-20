# Object Detector
## 1. Template Matching
Template matching is a fundamental technique in computer vision and image processing that involves finding regions within a target image that match a given reference image, referred to as the "template." The core idea is to slide the template over the target image and compute a similarity measure at each location to determine how well the template aligns with that region.

<img width="952" height="672" alt="image" src="https://github.com/user-attachments/assets/164bc955-b869-4b8d-9e2c-aeb02a0bf4e9" />

Several similarity metrics can be used in template matching, including sum of squared differences (SSD), normalized cross-correlation (NCC), and cosine similarity. Among these, normalized cross-correlation is widely used because it provides robustness against variations in illumination and contrast.
