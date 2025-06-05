##  Image-To-Video Generation from Sparse Image Inputs

A code base developed for a project submitted as part of the **UvA Computer Vision 2 Course 2025**.

This work builds upon the paper _[CamI2V: Camera-Controlled Image-to-Video Diffusion Model](https://arxiv.org/abs/2410.15957)_  
Original codebase: [CamI2V GitHub](https://github.com/ZGCTroy/CamI2V/tree/main)

---

##  Abstract

Generating high-quality, temporally coherent videos from sparse image inputs, particularly single images, remains a significant challenge, with outputs often exhibiting visual artifacts such as noise and limited resolution. This study investigates the enhancement of single-image diffusion-based video generation, specifically focusing on outputs from the CamI2V model, through the systematic application and combination of post-processing techniques. Specifically, we explore video denoising using FastDVDnet and video super-resolution using Upscale-A-Video, evaluating their individual and sequential impacts on video quality as follows.
- Denoising only (FastDVDnet)
- Upscaling only (Upscale-A-Video)
- Denoising followed by upscaling
- Upscaling followed by denoising
  
Experiments were conducted on diverse indoor scenes, assessing performance using Peak Signal-to-Noise Ratio (PSNR) for pixel-level temporal consistency and Structural Similarity Index Measure (SSIM) for temporal perceptual coherence. Our quantitative results show modest differences between methods, with high PSNR standard deviations making definitive conclusions challenging. While denoising alone yielded the highest mean PSNR, and upscaling followed by denoising achieved the highest mean SSIM, these improvements were not always substantial across all metrics and were impacted by resolution inconsistencies. Qualitatively, all post-processing methods visibly reduced noise (see the demos on our [CV2-project-page](https://voytech-0.github.io/CV2-project-page/)). 

However, the study also highlights that inherent artifacts from the base generative model may limit the overall efficacy of post-processing. This work underscores the complexities in evaluating and enhancing single-image video generation and suggests that optimal strategies may involve improvements to the foundational models alongside post-processing.

---

##  CamI2V 

The `CamI2V` folder contains the code and ReadMe from the original [CamI2V GitHub](https://github.com/ZGCTroy/CamI2V/tree/main). This ReadMe includes all necessary steps necessary to run inference. 

We downloaded the [CamI2V_512x320@100k](https://huggingface.co/MuteApo/CamI2V/blob/main/512_cami2v_100k.pt) for higher resolution and better camera control. Addtionally, we downloaded [Qwen2-VL Captioner](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct-AWQ) to be able add captions to your own input images during video generation.

> Place the [CamI2V_512x320@100k](https://huggingface.co/MuteApo/CamI2V/blob/main/512_cami2v_100k.pt) model in the `ckpts` folder and the [Qwen2-VL Captioner](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct-AWQ) model in the `pretrained_models` folder.

### Running CamI2V on Snellius

To run this dashboard on Snellius, we have several job files:
- `env_cami2v.job` sets up the environment
- `install_cami2v` installs additional dependcies in the environment on snellius
- `cami2v.job` launches the dashboard for how long you want

In order to connect the dashboard to your localhost, you should take some extra steps. Assuming you have already installed your environment, the following steps should be taken:
1. Log in: `ssh -X scurXXXX@snellius.surf.nl`
2. Run the job: `sbatch cami2v.job`
3. Check job status: `squeue`
4. Find node under nodelist (i.e. `gcn25`)
5. Open a new powershell window
6. Create an SSH tunnel `ssh -L 7860:localhost:7860 -J scurXXXX@snellius.surf.nl scurXXXX@gcnXX` (replace `XX` with your actual node, adjust node if different)
7. Open [http://localhost:7860/](http://localhost:7860/) in your browser

---

The `Images` folder contains the input images used for video generation. Three of these images were provided by **3DUniversum**, the stakeholder of this project, and the other three are from the RealEstate10K dataset. 

As the focus of the project is not on improving the CamI2V pipeline itself, but rather extending it through post-processing methods, the inference on CamI2V is performed mostly on the default variables and weights from the original [CamI2V GitHub](https://github.com/ZGCTroy/CamI2V/tree/main) setup. An exception was made for the **look-left** movement, where we increased the Trace Exact Ratio (TER) from 0.1 (default) to 0.3 to obtain more camera movement within the same video length. 

We generated 3 distinct video movements (**pan-left**, **orbit-up**, **look-left**) from each of the 6 input images, producing a total of 18 initial videos. No text prompts were used as no qualitative difference was observed when adding them. 

---

##  PostProcessing Methods


