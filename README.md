##  Image-To-Video Generation from Sparse Image Inputs

A code base for a project submitted as part of the **UvA Computer Vision 2 Course 2025**.

This work builds upon the paper: _[CamI2V: Camera-Controlled Image-to-Video Diffusion Model](https://arxiv.org/abs/2410.15957)_  
Original codebase: [CamI2V GitHub](https://github.com/ZGCTroy/CamI2V/tree/main)

---

##  Abstract

Generating high-quality, temporally coherent videos from sparse image inputs, particularly single images, remains a significant challenge, with outputs often exhibiting visual artifacts such as noise and limited resolution. This study investigates the enhancement of single-image diffusion-based video generation, specifically focusing on outputs from the CamI2V model, through the systematic application and combination of post-processing techniques. We explore video denoising using FastDVDnet and video super-resolution using Upscale-A-Video, evaluating their individual and sequential impacts on video quality.
- Denoising only (FastDVDnet)
- Upscaling only (Upscale-A-Video)
- Denoising followed by upscaling
- Upscaling followed by denoising
  
Experiments were conducted on diverse indoor scenes, assessing performance using Peak Signal-to-Noise Ratio (PSNR) for pixel-level temporal consistency and Structural Similarity Index Measure (SSIM) for temporal perceptual coherence. Our quantitative results show modest differences between methods, with high PSNR standard deviations making definitive conclusions challenging. While denoising alone yielded the highest mean PSNR, and upscaling followed by denoising achieved the highest mean SSIM, these improvements were not always substantial across all metrics and were impacted by resolution inconsistencies. Qualitatively, all post-processing methods visibly reduced noise (see [demos](https://voytech-0.github.io/CV2-project-page/)). 

However, the study also highlights that inherent artifacts from the base generative model may limit the overall efficacy of post-processing. This work underscores the complexities in evaluating and enhancing single-image video generation and suggests that optimal strategies may involve improvements to the foundational models alongside post-processing.

---

##  CamI2V 

In the CamI2V folder, you can find the ReadMe and corresponding code of the original [CamI2V GitHub](https://github.com/ZGCTroy/CamI2V/tree/main). This ReadMe contains all steps necessary to run inference. We downloaded the [CamI2V_512x320@100k](https://huggingface.co/MuteApo/CamI2V/blob/main/512_cami2v_100k.pt) for higher resolution and advanced camera control. We also downloaded [Qwen2-VL Captioner](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct-AWQ) to add a caption to your custom imaged when generating videos.  [CamI2V_512x320@100k](https://huggingface.co/MuteApo/CamI2V/blob/main/512_cami2v_100k.pt) model should be put in the `ckpts` folder and [Qwen2-VL Captioner](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct-AWQ) in the `pretrained_models` folder.

To run this dashboard on Snellius, we have `env_cami2v.job` that installs the environment and `install_cami2v` that installs some extra dependcies in the environment on snellius. `cami2v.job` runs the dashboard for how long you want. In order to connect the dashboard to your localhost, you should take some extra steps. Assuming you have already installed your environment, the following steps should be taken to run CamI2V on Snellius connected to your localhost:
1. Login: <ssh -X scurXXXX@snellius.surf.nl>,
2. <sbatch cami2v.job>,
3. <squeue>,
4. Find node under nodelist (i.e. gcn25),
5. Open new powershell,
6. <ssh -L 7860:localhost:7860 -J scurXXXX@snellius.surf.nl scurXXXX@gcnXX> (adjust node if different),
7. Open http://localhost:7860/ in browse


The `Images` folder contains the images we generated videos from...settings...

##  PostProcessing Methods


