<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">SegMetric</h3>

  <p align="center">
    A tool to establish ground truth in cell segmentation and create a quality metric that can be used to compare cell segmentation models
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

Currently, it is difficult to determine how well cell segmentation is performed without a qualitative examination. Furthermore, most cell segmentation methods employ a deep learning model that identify cells using nuclei DAPI markers and may use a variety of other markers to identify the membrane. However, these models are trained on datasets that may not encompass the cell morphological variance that tissues may have and thus may perform suboptimally. Additionally, noises in data can make these cell segmentation to be even less accurate. While, qualitative examination can provide brief insight into the performance of cell segmentation, it is difficult to scale with large amount of data, time-consuming, and does not provide a single metric that can be used to compare the models. 

Thus I developed SegMetric to automatically and quantatively generate a singe segmentation quality metric that can easily be used to compare segmentation models. Additionally, the visualization functions of this tool can further determine whether or not the model over- or under-segment cells. This information can then be used downstream to potentially filter cells. 

<!-- GETTING STARTED -->

### Prerequisites

Install the dependencies from the requirements.txt file.
  ```sh
  pip install requirements.txt
  ```

<!-- USAGE EXAMPLES -->
## Usage

The script takes five inputs: path to your DAPI image, path to your cell segmentation mask, number of iterations, sample size, and value to exclude from the mask.
  '''sh
  python SegMetric.py <PATH TO IMAGE> <PATH TO MASK> <# ITERATIONS> <# SAMPLE SIZE> <# VALUE TO EXCLUDE>
  '''
