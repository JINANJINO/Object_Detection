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

## 1-1. Template Matched Practice

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





