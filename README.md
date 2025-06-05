##  Image-To-Video Generation from Sparse Image Inputs

A code base for a project submitted as part of the **UvA Computer Vision 2 Course 2025**.

This work builds upon the paper:  
 _[CamI2V: Camera-Controlled Image-to-Video Diffusion Model](https://arxiv.org/abs/2410.15957)_  
Original codebase: [CamI2V GitHub](https://github.com/935963004/LaBraM](https://github.com/ZGCTroy/CamI2V/tree/main)

---

##  Abstract

Generating high-quality, temporally coherent videos from sparse image inputs, particularly single images, remains a significant challenge, with outputs often exhibiting visual artifacts such as noise and limited resolution. This study investigates the enhancement of single-image diffusion-based video generation, specifically focusing on outputs from the CamI2V model, through the systematic application and combination of post-processing techniques. We explore video denoising using FastDVDnet and video super-resolution using Upscale-A-Video, evaluating their individual and sequential impacts on video quality.
- Denoising only (FastDVDnet)
- Upscaling only (Upscale-A-Video)
- Denoising followed by upscaling
- Upscaling followed by denoising
  
Experiments were conducted on diverse indoor scenes, assessing performance using Peak Signal-to-Noise Ratio (PSNR) for pixel-level temporal consistency and Structural Similarity Index Measure (SSIM) for temporal perceptual coherence. Our quantitative results show modest differences between methods, with high PSNR standard deviations making definitive conclusions challenging. While denoising alone yielded the highest mean PSNR, and upscaling followed by denoising achieved the highest mean SSIM, these improvements were not always substantial across all metrics and were impacted by resolution inconsistencies. Qualitatively, all post-processing methods visibly reduced noise (see [demos](https://voytech-0.github.io/CV2-project-page/)). However, the study also highlights that inherent artifacts from the base generative model may limit the overall efficacy of post-processing. This work underscores the complexities in evaluating and enhancing single-image video generation and suggests that optimal strategies may involve improvements to the foundational models alongside post-processing.

---

##  CamI2V 



##  PostProcessing Methods


