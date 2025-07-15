import cv2
import PIL 

class VideoInput:
    def __init__(self, video_file):
        self.video_file = video_file
        self.handle = v =  cv2.VideoCapture(video_file)
        self.frame_count = int(v.get(cv2.CAP_PROP_FRAME_COUNT))
        self.width = v.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = v.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.fps = v.get(cv2.CAP_PROP_FPS)
        self.frame_step = 1.0 / self.fps
        self.current_time = 0
        self.current_frame = -1

    def next_frame(self):
        r,f = self.handle.read()
        self.current_frame += 1
        self.current_time += self.frame_step
        return r,f

def load_image(image):
    if type(image) != PIL.Image.Image:
        if type(image) == np.ndarray:
            image = PIL.Image.fromarray(image).convert('RGB')
        else:
            image = PIL.Image.open(image).convert('RGB')
    return image