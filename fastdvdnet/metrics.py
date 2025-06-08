import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr
import os
import sys
import pandas as pd
from tabulate import tabulate
import glob

def extract_frames(video_path, max_frames=None):
    """
    Extract frames from a video file
    
    Args:
        video_path (str): Path to the video file
        max_frames (int, optional): Maximum number of frames to extract. If None, extract all frames.
        
    Returns:
        list: List of frames as numpy arrays
    """
    frames = []
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        raise ValueError(f"Could not open video file: {video_path}")
    
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        # Convert BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append(frame)
        
        frame_count += 1
        if max_frames is not None and frame_count >= max_frames:
            break
    
    cap.release()
    return frames

def calculate_metrics(frames):
    """
    Calculate SSIM and PSNR between consecutive frames
    
    Args:
        frames (list): List of frames as numpy arrays
        
    Returns:
        dict: Dictionary containing lists of SSIM and PSNR values
    """
    if len(frames) < 2:
        return {"ssim": [], "psnr": []}
    
    ssim_values = []
    psnr_values = []
    
    for i in range(len(frames) - 1):
        frame1 = frames[i]
        frame2 = frames[i + 1]
        
        # Calculate SSIM
        # Convert to grayscale for SSIM
        gray1 = cv2.cvtColor(frame1, cv2.COLOR_RGB2GRAY)
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_RGB2GRAY)
        ssim_value = ssim(gray1, gray2, data_range=gray1.max() - gray1.min())
        ssim_values.append(ssim_value)
        
        # Calculate PSNR
        psnr_value = psnr(frame1, frame2)
        psnr_values.append(psnr_value)
    
    return {
        "ssim": ssim_values,
        "psnr": psnr_values
    }

def analyze_video(video_path, max_frames=None):
    """
    Analyze a video file and calculate SSIM and PSNR metrics
    
    Args:
        video_path (str): Path to the video file
        max_frames (int, optional): Maximum number of frames to extract
        
    Returns:
        dict: Dictionary containing metrics and basic video information
    """
    frames = extract_frames(video_path, max_frames)
    metrics = calculate_metrics(frames)
    
    # Calculate average metrics
    avg_ssim = np.mean(metrics["ssim"]) if metrics["ssim"] else 0
    avg_psnr = np.mean(metrics["psnr"]) if metrics["psnr"] else 0
    
    # Get video filename without path
    video_name = os.path.basename(video_path)
    
    return {
        "video_name": video_name,
        "frame_count": len(frames),
        "ssim_values": metrics["ssim"],
        "psnr_values": metrics["psnr"],
        "avg_ssim": avg_ssim,
        "avg_psnr": avg_psnr
    }

def analyze_videos(video_paths, max_frames=None, output_file=None):
    """
    Analyze multiple videos and output results in a table format
    
    Args:
        video_paths (list): List of paths to video files
        max_frames (int, optional): Maximum number of frames to extract
        output_file (str, optional): Path to output CSV file
        
    Returns:
        pd.DataFrame: DataFrame containing results for all videos
    """
    results = []
    
    for video_path in video_paths:
        try:
            print(f"Analyzing {os.path.basename(video_path)}...")
            video_result = analyze_video(video_path, max_frames)
            results.append({
                "Video": video_result["video_name"],
                "Frames": video_result["frame_count"],
                "Avg SSIM": video_result["avg_ssim"],
                "Avg PSNR": video_result["avg_psnr"]
            })
        except Exception as e:
            print(f"Error analyzing {video_path}: {e}")
    
    # Create DataFrame
    df = pd.DataFrame(results)
    
    # Print table
    if not df.empty:
        print("\nResults for individual videos:")
        print(tabulate(df, headers="keys", tablefmt="grid", floatfmt=".4f"))
        
        # Calculate and print overall averages
        overall_avg_ssim = df["Avg SSIM"].mean()
        overall_avg_psnr = df["Avg PSNR"].mean()
        
        print("\nOverall averages for the folder:")
        overall_df = pd.DataFrame({
            "Metric": ["Average SSIM", "Average PSNR"],
            "Value": [overall_avg_ssim, overall_avg_psnr]
        })
        print(tabulate(overall_df, headers="keys", tablefmt="grid", floatfmt=".4f"))
    
    # Save to CSV if output_file is provided
    if output_file and not df.empty:
        df.to_csv(output_file, index=False)
        print(f"\nResults saved to {output_file}")
    
    return df

# Example usage
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python metrics.py <video_folder> [--output <output_file>] [--max-frames <max_frames>]")
        sys.exit(1)
    
    # Parse arguments
    video_folder = sys.argv[1]
    output_file = None
    max_frames = 100  # Default to 100 frames for quick analysis
    
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--output":
            if i + 1 < len(sys.argv):
                output_file = sys.argv[i + 1]
                i += 2
            else:
                print("Error: Missing output file path")
                sys.exit(1)
        elif sys.argv[i] == "--max-frames":
            if i + 1 < len(sys.argv):
                try:
                    max_frames = int(sys.argv[i + 1])
                    i += 2
                except ValueError:
                    print(f"Error: Invalid max frames value: {sys.argv[i + 1]}")
                    sys.exit(1)
            else:
                print("Error: Missing max frames value")
                sys.exit(1)
        else:
            i += 1
    
    # Get all video files in the folder
    video_extensions = ['*.mp4', '*.avi', '*.mov', '*.mkv']  # Add more extensions if needed
    video_paths = []
    for ext in video_extensions:
        video_paths.extend(glob.glob(os.path.join(video_folder, ext)))
    
    if not video_paths:
        print(f"Error: No video files found in {video_folder}")
        sys.exit(1)
    
    # Analyze videos
    analyze_videos(video_paths, max_frames=max_frames, output_file=output_file)
