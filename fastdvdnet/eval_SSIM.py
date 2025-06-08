import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def compute_ssim_between_videos(original_path, denoised_path):
    cap_orig = cv2.VideoCapture(original_path)
    cap_den = cv2.VideoCapture(denoised_path)

    ssim_scores = []

    while True:
        ret1, frame1 = cap_orig.read()
        ret2, frame2 = cap_den.read()

        if not ret1 or not ret2:
            break

        gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

        # Resize if needed (in case dimensions are off)
        if gray1.shape != gray2.shape:
            gray2 = cv2.resize(gray2, (gray1.shape[1], gray1.shape[0]))

        score, _ = ssim(gray1, gray2, full=True)
        ssim_scores.append(score)

    cap_orig.release()
    cap_den.release()

    return np.mean(ssim_scores)

# SSIM between videos
print('garden_look-left_TER-0.3')
inter_ssim = compute_ssim_between_videos('3d_universum/garden_look-left_TER-0.3.mp4', 'results_hd/garden_look-left_TER-0.3_n150_g6_s30_p24_26_28/garden_look-left_TER-0.3_n150_g6_s30_p24_26_28_denoised.mp4')
print(f"{'SSIM (Original↔Denoised)':<20} {'-':<20} {'%.4f' % inter_ssim:<20} Closer to 1.0")

print('garden_orbit-up_standard')
inter_ssim = compute_ssim_between_videos('3d_universum/garden_orbit-up_standard.mp4', 'results_hd/garden_orbit-up_standard_n150_g6_s30_p24_26_28/garden_orbit-up_standard_n150_g6_s30_p24_26_28_denoised.mp4')
print(f"{'SSIM (Original↔Denoised)':<20} {'-':<20} {'%.4f' % inter_ssim:<20} Closer to 1.0")

print('garden_pan-left_standard')
inter_ssim = compute_ssim_between_videos('3d_universum/garden_pan-left_standard.mp4', 'results_hd/garden_pan-left_standard_n150_g6_s30_p24_26_28/garden_pan-left_standard_n150_g6_s30_p24_26_28_denoised.mp4')
print(f"{'SSIM (Original↔Denoised)':<20} {'-':<20} {'%.4f' % inter_ssim:<20} Closer to 1.0")

print('TV_look-left_TER-0.3')
inter_ssim = compute_ssim_between_videos('3d_universum/TV_look-left_TER-0.3.mp4', 'results_hd/TV_look-left_TER-0.3_n150_g6_s30_p24_26_28/TV_look-left_TER-0.3_n150_g6_s30_p24_26_28_denoised.mp4')
print(f"{'SSIM (Original↔Denoised)':<20} {'-':<20} {'%.4f' % inter_ssim:<20} Closer to 1.0")

print('TV_orbit-up_standard')
inter_ssim = compute_ssim_between_videos('3d_universum/TV_orbit-up_standard.mp4', 'results_hd/TV_orbit-up_standard_n150_g6_s30_p24_26_28/TV_orbit-up_standard_n150_g6_s30_p24_26_28_denoised.mp4')
print(f"{'SSIM (Original↔Denoised)':<20} {'-':<20} {'%.4f' % inter_ssim:<20} Closer to 1.0")

print('TV_pan-left_standard')
inter_ssim = compute_ssim_between_videos('3d_universum/TV_pan-left_standard.mp4', 'results_hd/TV_pan-left_standard_n150_g6_s30_p24_26_28/TV_pan-left_standard_n150_g6_s30_p24_26_28_denoised.mp4')
print(f"{'SSIM (Original↔Denoised)':<20} {'-':<20} {'%.4f' % inter_ssim:<20} Closer to 1.0")



print('bathroom_look-left_TER-0.3')
inter_ssim = compute_ssim_between_videos('real_estate/bathroom_look-left_TER-0.3.mp4', 'results_hd/bathroom_look-left_TER-0.3_n150_g6_s30_p24_26_28/bathroom_look-left_TER-0.3_n150_g6_s30_p24_26_28_denoised.mp4')
print(f"{'SSIM (Original↔Denoised)':<20} {'-':<20} {'%.4f' % inter_ssim:<20} Closer to 1.0")
# inter_ssim = compute_ssim_between_videos('demo1.mp4', 'noisy_demo1.mp4')
# print(f"{'SSIM (Original↔Noisy)':<20} {'-':<20} {'%.4f' % inter_ssim:<20} Closer to 1.0")

print('bathroom_ordbit-up_standard')
inter_ssim = compute_ssim_between_videos('real_estate/bathroom_orbit-up_standard.mp4', 'results_hd/bathroom_orbit-up_standard_n150_g6_s30_p24_26_28/bathroom_orbit-up_standard_n150_g6_s30_p24_26_28_denoised.mp4')
print(f"{'SSIM (Original↔Denoised)':<20} {'-':<20} {'%.4f' % inter_ssim:<20} Closer to 1.0")
# inter_ssim = compute_ssim_between_videos('demo2.mp4', 'noisy_demo2.mp4')
# print(f"{'SSIM (Original↔Noisy)':<20} {'-':<20} {'%.4f' % inter_ssim:<20} Closer to 1.0")

print('bathroom_pan-left_standard')
inter_ssim = compute_ssim_between_videos('real_estate/bathroom_pan-left_standard.mp4', 'results_hd/bathroom_pan-left_standard_n150_g6_s30_p24_26_28/bathroom_pan-left_standard_n150_g6_s30_p24_26_28_denoised.mp4')
print(f"{'SSIM (Original↔Denoised)':<20} {'-':<20} {'%.4f' % inter_ssim:<20} Closer to 1.0")
# inter_ssim = compute_ssim_between_videos('demo3.mp4', 'noisy_demo3.mp4')
# print(f"{'SSIM (Original↔Noisy)':<20} {'-':<20} {'%.4f' % inter_ssim:<20} Closer to 1.0")

print('bed_look-left_TER-0.3')
inter_ssim = compute_ssim_between_videos('real_estate/bed_look-left_TER-0.3.mp4', 'results_hd/bed_look-left_TER-0.3_n150_g6_s30_p24_26_28/bed_look-left_TER-0.3_n150_g6_s30_p24_26_28_denoised.mp4')
print(f"{'SSIM (Original↔Denoised)':<20} {'-':<20} {'%.4f' % inter_ssim:<20} Closer to 1.0")

print('bed_orbit-up_standard')
inter_ssim = compute_ssim_between_videos('real_estate/bed_orbit-up_standard.mp4', 'results_hd/bed_orbit-up_standard_n150_g6_s30_p24_26_28/bed_orbit-up_standard_n150_g6_s30_p24_26_28_denoised.mp4')
print(f"{'SSIM (Original↔Denoised)':<20} {'-':<20} {'%.4f' % inter_ssim:<20} Closer to 1.0")

print('bed_pan-left_standard')
inter_ssim = compute_ssim_between_videos('real_estate/bed_pan-left_standard.mp4', 'results_hd/bed_pan-left_standard_n150_g6_s30_p24_26_28/bed_pan-left_standard_n150_g6_s30_p24_26_28_denoised.mp4')
print(f"{'SSIM (Original↔Denoised)':<20} {'-':<20} {'%.4f' % inter_ssim:<20} Closer to 1.0")

print('couch_look-left_TER-0.3')
inter_ssim = compute_ssim_between_videos('real_estate/couch_look-left_TER-0.3.mp4', 'results_hd/couch_look-left_TER-0.3_n150_g6_s30_p24_26_28/couch_look-left_TER-0.3_n150_g6_s30_p24_26_28_denoised.mp4')
print(f"{'SSIM (Original↔Denoised)':<20} {'-':<20} {'%.4f' % inter_ssim:<20} Closer to 1.0")

print('couch_orbit-up_standard')
inter_ssim = compute_ssim_between_videos('real_estate/couch_orbit-up_standard.mp4', 'results_hd/couch_orbit-up_standard_n150_g6_s30_p24_26_28/couch_orbit-up_standard_n150_g6_s30_p24_26_28_denoised.mp4')
print(f"{'SSIM (Original↔Denoised)':<20} {'-':<20} {'%.4f' % inter_ssim:<20} Closer to 1.0")

print('couch_pan-left_standard')
inter_ssim = compute_ssim_between_videos('real_estate/couch_pan-left_standard.mp4', 'results_hd/couch_pan-left_standard_n150_g6_s30_p24_26_28/couch_pan-left_standard_n150_g6_s30_p24_26_28_denoised.mp4')
print(f"{'SSIM (Original↔Denoised)':<20} {'-':<20} {'%.4f' % inter_ssim:<20} Closer to 1.0")

