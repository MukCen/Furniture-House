import os

media_path = "media/goods_images"

for filename in os.listdir(media_path):
    if " " in filename:
        new_filename = filename.replace(" ", "_")
        os.rename(
            os.path.join(media_path, filename), os.path.join(media_path, new_filename)
        )
        print(f"Renamed: {filename} -> {new_filename}")
