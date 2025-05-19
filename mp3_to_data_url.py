import base64

# Path to your MP3 file (assumes same directory)
file_path = "Electromagnetico.mp3"

# Read and encode the MP3 file
with open(file_path, "rb") as mp3_file:
    encoded_data = base64.b64encode(mp3_file.read()).decode("utf-8")

# Create data URL
data_url = f"data:audio/mpeg;base64,{encoded_data}"

# Optionally save to a text file to avoid printing millions of characters to the terminal
with open("Revolution_data_url.txt", "w") as out_file:
    out_file.write(data_url)

print("✅ Data URL saved to 'Revolution_data_url.txt'")
