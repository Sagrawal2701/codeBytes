# codeBytes
Methodology:

• Library Used: Open CV

• Framework Used: Flask
(Programming Languages Used: HTML, CSS, Python)

• For Edit Page:
Brightness: To increase brightness, we added some values to each 
channel and brightness was increased.

Contrast: Mid tones are eliminated. Image will contain higher 
number of dark/blacks and whites/highlights.

Blur: We used normal open cv blur function which is average 
blurring.

Sharpen: we used kernel or convolution matrix for sharping image
For max: [[-1,-1,-1], [-1, 9,-1],[-1,-1,-1]]
For min: [[0,-1,0], [-1,5,-1], [0,-1,0]]

Denoise: Performed image denoising using Non-local Means 
Denoising algorithm with several computational optimizations. 
Noise expected to be a gaussian white noise.

Rotate: rotate() method is used to rotate a 2D array in multiples of
90 degrees.

Resize: We used cv2.resize() which reduces the number of pixels 
from an image.

Filters: We implemented several filters like Color-pop, cool, etc. 
by using different methods.

• For Nightmode Page:
We implemented a night-mode feature which aims to utilise a dual 
channel prior-based method for low illumination image 
enhancement with a single image. Taking the dark channel into 
consideration removes block effects in some regions and helps see 
various details from dark images clearly.

• For Live Effects Page:
We implemented 12 live filters using OpenCV we got the frame 
feed from user webcam then we used haarcascade to recognize 
frontal facial features and then attached PNG files (clip arts like 
sunglasses, moustache, ipl team bands, etc.) on various facial 
positions.


• Link to Github Repository of the project:
https://github.com/Sagrawal2701/codeByte
