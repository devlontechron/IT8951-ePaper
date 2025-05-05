import os
import time
from glob import glob
from PIL import Image
from display import Display
from inkycal.image import InkyImage  # Assuming InkyImage is defined in inkycal.image

# Configuration
EPAPER_MODEL = "10.3 epaper class"  # Replace with your actual ePaper model name
IMAGE_FOLDER = "..\pics\" # Path to the folder containing images
DISPLAY_CYCLE_INTERVAL = 300  # 5 minutes in seconds

def main():
    # Initialize the Display class
    display = Display(EPAPER_MODEL)

    # Calibrate the display before starting
    print("Calibrating the display...")
    display.calibrate()

    # Get all .jpg files from the folder
    image_files = glob(os.path.join(IMAGE_FOLDER, "*.jpg"))
    if not image_files:
        print("No images found in the specified folder.")
        return

    # Start the display cycle
    print("Starting the display cycle...")
    while True:
        for image_path in image_files:
            print(f"Processing image: {image_path}")

            # Load and process the image using InkyImage
            inky_image = InkyImage(image_path)
            resized_image = inky_image.resize(display.get_display_size(EPAPER_MODEL))
            processed_image = inky_image.image_to_palette(resized_image, palette="16gray")

            print("Calibrating the display...")
            display.calibrate()

            # Render the image on the ePaper display
            print("Rendering image on the display...")
            display.render(processed_image)

            # Wait for the next cycle
            print(f"Waiting for {DISPLAY_CYCLE_INTERVAL} seconds...")
            time.sleep(DISPLAY_CYCLE_INTERVAL)

if __name__ == "__main__":
    main()