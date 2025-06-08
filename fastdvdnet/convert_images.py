import torch
import numpy as np
import cv2

scene = {
    'key': 'scene001',
    'images': [],
    'cameras': []
}

# Load the .npz file
data = np.load("dust3r_data.npz")

# Extract the fields
imgs = data['imgs']  # Images (N, H, W, 3)
depths = data['depths']  # Depth maps (N, H, W) - if needed
c2ws = data['c2ws']  # Camera-to-world transformations (N, 4, 4)
principal_points = data['principal_points']  # (N, 2)
focals = data['focals']  # (N,) focal lengths

# Loop through each image and corresponding camera data
for i in range(len(imgs)):
    img = imgs[i]
    
    # Convert to (H, W, 3) if it's (3, H, W)
    if img.shape[0] == 3:
        img = np.transpose(img, (1, 2, 0))

    # Convert float images to uint8 if necessary
    if img.dtype != np.uint8:
        img = np.clip(img * 255.0, 0, 255).astype(np.uint8)

    # Encode image as JPEG byte buffer
    success, buffer = cv2.imencode('.jpg', img)
    if not success:
        print(f"Failed to encode image {i}")
        continue
    
    scene['images'].append(buffer)

    # Ensure values are plain floats
    fx = float(focals[i])
    fy = float(focals[i])
    cx, cy = map(float, principal_points[i])

    # Get the camera extrinsics (rotation and translation from c2ws)
    c2w = c2ws[i]  # 4x4 matrix
    R = c2w[:3, :3]  # Rotation part (3x3)
    T = c2w[:3, 3]   # Translation part (3x1)

    # Flatten and format the camera parameters for the scene
    cam_params = [fx, fy, cx, cy] + [0.0, 0.0] + R.flatten().tolist() + T.flatten().tolist()
    scene['cameras'].append(cam_params)

# Save the scene data to a .torch file
torch.save([scene], "test/scene001.torch")

# import torch
# scene = torch.load("test/scene001.torch")[0]
# print(f"Images: {len(scene['images'])}, Cameras: {len(scene['cameras'])}")
# print(f"First camera params: {scene['cameras'][0]}")
