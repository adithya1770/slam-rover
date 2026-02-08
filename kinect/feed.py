import freenect
import cv2
import numpy as np
import time

def get_ir():
    ir_feed, _ = freenect.sync_get_video(format=freenect.VIDEO_IR)
    return ir_feed

# Define grid size
rows, cols = 4, 4
frame_height, frame_width = 480, 640
cell_h = frame_height // rows
cell_w = frame_width // cols

while True:
    for angle in angles:
        print(f"Tilting to {angle}°")
        freenect.set_tilt_degs(angle)
        time.sleep(1)

        # Capture IR and depth frame
        depth, _ = freenect.sync_get_depth(format=freenect.DEPTH_MM)
        ir_img = get_ir()
        ir_8bit = np.uint8(ir_img)
        cv2.imshow("Kinect IR Feed", ir_8bit)

        # Prepare depth image for visualization
        depth_display = np.uint8((depth / np.max(depth)) * 255)
        depth_colored = cv2.applyColorMap(depth_display, cv2.COLORMAP_JET)

        # Dictionary to hold average distances
        avg_distances = {}

        # Loop through 4x4 gridaas
        for i in range(rows):
            for j in range(cols):
                y1 = i * cell_h
                y2 = (i + 1) * cell_h
                x1 = j * cell_w
                x2 = (j + 1) * cell_w

                region = depth[y1:y2, x1:x2]
                avg_dist = np.mean(region)
                key = f"R{i+1}C{j+1}"
                avg_distances[key] = avg_dist

                # Draw rectangle and write distance on image
                cv2.rectangle(depth_colored, (x1, y1), (x2, y2), (255, 255, 255), 1)
                cv2.putText(depth_colored, f"{int(avg_dist)}", (x1 + 5, y1 + 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)

        print(avg_distances)

        # Show the depth feed
        cv2.imshow("Kinect Depth Feed", depth_colored)

        time.sleep(0.01)

        if cv2.waitKey(1) == 27:
            break

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
