import tarfile
import os
import subprocess

# Define the URL (check the latest dataset version from the official site)
cn_celeb_url = "http://www.openslr.org/resources/82/cn-celeb_v2.tar.gz"

# Define the output path
output_file = "CN-Celeb.tar.gz"

# Use wget to download
subprocess.run(["wget", "-O", output_file, cn_celeb_url])

extract_path = "data/CN-Celeb"  # Change this if needed

# Ensure the directory exists
os.makedirs(extract_path, exist_ok=True)

try:
    with tarfile.open(tar_path, "r:gz") as tar:
        tar.extractall(extract_path)
    print(f"Extraction completed! Files are in {extract_path}")
except tarfile.ReadError:
    print("Error: Tar file is corrupt or empty. Please check the download.")

