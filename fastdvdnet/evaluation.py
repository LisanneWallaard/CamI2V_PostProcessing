import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def compute_flicker_index(video_path):
    cap = cv2.VideoCapture(video_path)
    prev_gray = None
    flicker_scores = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if prev_gray is not None:
            diff = gray.astype(np.float32) - prev_gray.astype(np.float32)
            flicker = np.mean(np.square(diff))  # Mean Squared Difference
            flicker_scores.append(flicker)

        prev_gray = gray

    cap.release()
    return np.mean(flicker_scores)  # Lower = more temporally stable

def psnr(img1, img2):
    mse = np.mean((img1.astype(np.float32) - img2.astype(np.float32)) ** 2)
    if mse == 0:
        return 100  # Perfect match
    PIXEL_MAX = 255.0
    return 20 * np.log10(PIXEL_MAX / np.sqrt(mse))

def compute_temporal_psnr(video_path):
    cap = cv2.VideoCapture(video_path)
    prev_gray = None
    psnr_scores = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if prev_gray is not None:
            psnr_score = psnr(gray, prev_gray)
            psnr_scores.append(psnr_score)

        prev_gray = gray

    cap.release()
    return np.mean(psnr_scores)

def compute_temporal_ssim(video_path):
    cap = cv2.VideoCapture(video_path)
    prev_gray = None
    ssim_scores = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if prev_gray is not None:
            score, _ = ssim(prev_gray, gray, full=True)
            ssim_scores.append(score)

        prev_gray = gray

    cap.release()
    return np.mean(ssim_scores)

def compare_videos(original_path, denoised_path):
    print(f"\n Comparing Temporal Consistency Metrics\n")
    print(f"{'Metric':<20} {'Original Video':<20} {'Denoised Video':<20} {'Ideal Value'}")
    print("-" * 75)

    # tPSNR
    orig_tpsnr = compute_temporal_psnr(original_path)
    den_tpsnr = compute_temporal_psnr(denoised_path)
    print(f"{'tPSNR (dB)':<20} {orig_tpsnr:<20.2f} {den_tpsnr:<20.2f} Higher is better")
    # print("   - Measures pixel-level stability between consecutive frames")
    # print("   - Higher is better (typically >30 dB indicates good temporal smoothness)")

    # tSSIM
    orig_tssim = compute_temporal_ssim(original_path)
    den_tssim = compute_temporal_ssim(denoised_path)
    print(f"{'tSSIM':<20} {orig_tssim:<20.4f} {den_tssim:<20.4f} Closer to 1.0")
    # print("   - Measures structural similarity between consecutive frames")
    # print("   - Closer to 1.0 is better (perfect structural consistency)")

    # Flicker Index
    orig_flicker = compute_flicker_index(original_path)
    den_flicker = compute_flicker_index(denoised_path)
    print(f"{'Flicker Index':<20} {orig_flicker:<20.2f} {den_flicker:<20.2f} Lower is better")
    # print("   - Measures how much each pixel flickers between frames")
    # print("   - Lower is better (high values indicate visible flicker)\n")

    print()

print("Denoised demo 1:")
compare_videos("demo1.mp4", "denoised_demo1.mp4")

print("Denoised demo 2:")
compare_videos("demo2.mp4", "denoised_demo2.mp4")