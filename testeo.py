import requests

colonoscopy_config = {"block_id": 2990.0, "quality": 32.0, "bits": 2.0, "inter_parts": 0.0, "non_zero_pixels": 0.0,
                      "frame_width": 416.0,
                      "frame_height": 240.0, "movement_level": 124516.0, "mean": 0.0, "sub_mean_1": 0.0,
                      "sub_mean_2": 0.0,
                      "sub_mean_3": 0.0, "sub_mean_4": 0.0, "var_sub_blocks": 0.0, "sobel_h": 0.0, "sobel_v": 0.0,
                      "variance": 0.0,
                      "block_movement_h": 0.0, "block_movement_v": 0.0, "cost": 21334.5}

url = "http://localhost:9696/predict"
r = requests.post(url, json=colonoscopy_config)
print(r.json())

