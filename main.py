from yaml import load as yaml_load, FullLoader as yaml_FullLoader
import cv2

with open('settings.yml') as f:
    settings = yaml_load(f, Loader=yaml_FullLoader)

input_cap = cv2.VideoCapture(settings["input"])

if input_cap.isOpened():
    width = int(input_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(input_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(input_cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(input_cap.get(cv2.CAP_PROP_FRAME_COUNT))
    skip_frame = fps * settings["time quantum"]
    out = cv2.VideoWriter(settings["output"], cv2.VideoWriter_fourcc(*'mp4v'), settings["fps"], (width, height))
    count = 0
    while input_cap.isOpened():
        ret, frame = input_cap.read()
        if ret:
            out.write(frame)
            count += skip_frame
            percent = round((count / frame_count * 100), 1)
            if percent > 100:
                percent = 100
            print(f'\r{percent}% ', end="")
            input_cap.set(1, count)
        else:
            input_cap.release()
            break
