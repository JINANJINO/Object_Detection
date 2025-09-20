# Object Detector
## 1. Template Matching

**Overview**

Template Matching is a classical technique in computer vision and image processing used to locate specific patterns or objects within a target image. The method works by sliding a smaller reference image, known as the template, across the target image and computing a similarity score at each position. The region with the highest score is considered the best match.

![Example GIF or Image](https://github.com/user-attachments/assets/9d25c8da-d3dd-4cf8-9865-3ebb5296d27f)

**Mathematical Formulation**

Given a template $$T(x,y)$$ and an image $$I(x,y)$$, the similarity score $$R(u,v)$$ at location $$(u,v)$$ can be defined using **Normalized Cross-Correlation (NCC)** as follows:

$$
R(u,v) = \frac{
    \sum_{x,y} \left( T(x,y) - \bar{T} \right) \left( I(x+u, y+v) - \bar{I}_{u,v} \right)
}{
    \sqrt{
        \sum_{x,y} \left( T(x,y) - \bar{T} \right)^2 \,
        \sum_{x,y} \left( I(x+u, y+v) - \bar{I}_{u,v} \right)^2
    }
}
$$

- $$\bar{T}$$: Mean intensity of the template
- $$\bar{I}_{u,v}$$: Mean intensity of the image region being compared

**Image Pyramid Technique**

<img width="213" height="237" alt="image" src="https://github.com/user-attachments/assets/2bf9d266-34ff-4903-a15d-db02acfb9e2c" />


Template Matching can be sensitive to scale variations between the template and target objects. To address this, the **Image Pyramid** technique is commonly used. An image pyramid is a multi-scale representation of an image, created by repeatedly downsampling the original image to generate progressively smaller versions. This allows the template to be matched against multiple scales of the target image efficiently.

The procedure is as follows:
1. Construct a pyramid of images by iteratively downsampling the original image.
2. At each pyramid level, perform template matching using the chosen similarity metric.
3. Record the best match location and similarity score at all levels.
4. Select the location with the highest score across all pyramid levels as the final match.

This approach enables **scale-invariant template matching**, improving robustness when the target object appears larger or smaller than the template.


---

## 1-1. Template Matched Example

The original image and template image are included in the repo.

<table>
  <tr>
    <td>
      <b>Original Image</b><br>
      <img src="https://github.com/user-attachments/assets/114394c9-d0bd-453d-b38f-fc82ee9fc077" width="300">
    </td>
    <td>
      <b>Template Matching result</b><br>
      <img src="https://github.com/user-attachments/assets/7f12c60f-0d5a-49e7-bc6b-cdf1372da67f" width="300">
    </td>
  </tr>
</table>

---

---

# 2. HOG (Histogram of Oriented Gradients)

**Overview**

**Histogram of Oriented Gradients (HOG)** is a feature descriptor widely used in computer vision for object detection, particularly for human detection. The main idea is to capture the local **gradient orientation patterns** of an image, which represent the shape and structure of objects while being relatively invariant to illumination changes and small deformations.

 <img width="254" height="497" alt="image" src="https://github.com/user-attachments/assets/b1ce4fd3-68a7-4e42-9b5d-88fbfd5e5876" />
 <img width="254" height="497" alt="image" src="https://github.com/user-attachments/assets/ab3bf1a4-b358-40ec-99c1-8f12065c200b" />



HOG works by dividing the image into small connected regions called **cells**. For each cell, a histogram of gradient directions is computed. These histograms are then **normalized** over larger regions called **blocks** to improve robustness to lighting variations. Finally, all normalized histograms are concatenated into a single feature vector representing the image.

---

**Mathematical Formulation**

1. **Gradient Computation**:  
   Compute the horizontal and vertical gradients at each pixel:
   
   $$G_x = I(x+1, y) - I(x-1, y), \quad   G_y = I(x, y+1) - I(x, y-1)$$
   
   Gradient magnitude and orientation are then:
   
   $$M(x,y) = \sqrt{G_x^2 + G_y^2}, \quad   \theta(x,y) = \arctan\left(\frac{G_y}{G_x}\right)$$

3. **Histogram Generation**:  
   For each cell, compute a histogram of gradient orientations. Each pixel votes into a bin proportional to its magnitude:
   
   $$H_c(b) = \sum_{(x,y) \in c} w(x,y) \cdot \delta\big(b - \text{bin}(\theta(x,y))\big)$$
   
   - $$\(w(x,y) = M(x,y)\)$$ (weight by magnitude)  
   - $$\(\delta\)$$ is the Kronecker delta function  
   - $$\(b\)$$ indexes the orientation bin  

5. **Block Normalization**:  
   Group cells into blocks and normalize histograms to reduce illumination variations:
   
   $$H_{\text{block}} = \frac{H_{\text{cells}}}{\sqrt{\|H_{\text{cells}}\|_2^2 + \epsilon^2}}$$

---

## 2.2 HOG (Histogram of Oriented Gradients) Example

I've attached an example of HOG to the ```hog.py``` code, and also attached an avi video so you can practice.
- **Original Image**

<img width="768" height="576" alt="Screenshot from 2025-09-20 17-26-05" src="https://github.com/user-attachments/assets/4e5ad770-5e3a-4c94-a723-7e19f78b06e1" />

---

- **Result**

<img width="768" height="576" alt="image" src="https://github.com/user-attachments/assets/c2af389d-d01f-4f98-aa1b-c5f30c754bbe" />
