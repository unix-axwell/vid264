import base64

# Open the video file in binary mode
with open('input.mp4', 'rb') as video_file:
    # Read the whole file
    video_data = video_file.read()

# Encode the binary data to base64
base64_data = base64.b64encode(video_data)

# Decode the base64 data to text
text_data = base64_data.decode('utf-8')

# Write the text data to a file
with open('output.txt', 'w') as text_file:
    text_file.write(text_data)
