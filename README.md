# HFGL-Net:Laplacian-Based Explicit High-Frequency Component Guidance for a Multi-Scale Non-local Channel Attention Network in Remote Sensing Object Detection
In this paper, we propose a Laplacian-Based Explicit High-Frequency Component Guidance for a Multi-Scale Non-local Channel Attention Network(HFGL-Net).Specifically, a high-frequency decomposition of the image using the Laplacian pyramid and the introduction of a high-frequency component enhancement model (HCEM) explicitly capture the high-frequency information of the image, providing explicit high-frequency guidance to the network and thus enhancing the network’s detection performance. Furthermore, we propose a Multi-Scale Non-local Channel Attention Mechanism (MS-GLCA), which combines multi-scale and non-local perception mechanisms, adaptively fuses features at different scales, enhances the network’s ability to integrate local features with global dependencies, and more effectively assigns feature weights to the detection network.
![The overall architecture of HFGL-Net. HFGL-Net consists of detection structures such as HCEM and MS-GLCA. The figure illustrates the HFGL-Net architecture, which integrates the High-Frequency Component Enhancement Module (HCEM) and the Multi-scale Non-local Channel Attention Mechanism (MS-GLCA)](https://github.com/15272874521/HFGL-Net/blob/main/Overall.png)
![The Multi-scale Non-local Channel Attention Mechanism (MS-GLCA). By leveraging multi-scale features and non-local perception strategies, this mechanism enhances the model’s ability to detect multi-scale objects in remote sensing images. It adaptively captures the interdependencies between local details and global context, effectively allocating feature weights for the detection network, thereby improving detection accuracy.](https://github.com/15272874521/HFGL-Net/blob/main/attention.png)
# Installation
Please refer to [install.md](./docs/install.md) for installation and dataset preparation.

# Getting Started 
This repo is based on [yolov5](https://github.com/ultralytics/yolov5). 

#  Acknowledgements
I have used utility functions from other wonderful open-source projects. Espeicially thank the authors of:

* [ultralytics/yolov5](https://github.com/ultralytics/yolov5).
