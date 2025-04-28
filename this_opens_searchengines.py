import webbrowser
import os
import sys

# --- Configuration ---
# Add URLs of reverse image search / facial recognition sites you want to use.
# Note: These typically lead to the upload page or main search page.
SEARCH_SITES = [
    "https://images.google.com/",        # Google Images (Global)
    "https://www.bing.com/visualsearch", # Bing Visual Search (Global)
    "https://tineye.com/",               # TinEye (Specialized reverse search)
    "https://yandex.com/images/",        # Yandex Images (Strong in Eastern Europe/Russia)
    "https://image.baidu.com/",          # Baidu Images (Primarily Chinese web content)
    "https://pic.sogou.com/"             # Sogou Images (Primarily Chinese web content)
    # Add other relevant sites here if you find them.
    # Be aware that dedicated facial recognition sites like PimEyes or FaceCheck.ID
    # have specific terms, costs, and ethical considerations.
]

# --- Functions ---

def open_search_sites(image_path):
    """
    Opens specified search sites in the default web browser.
    It doesn't upload the image, just opens the sites for manual upload.
    """
    print(f"Opening search pages for image: {image_path}")
    print("Please manually upload the image to each site that opens.")

    opened_count = 0
    for url in SEARCH_SITES:
        print(f"Opening: {url}")
        try:
            if not webbrowser.open_new_tab(url):
                 # Try open as fallback if open_new_tab fails on some systems
                 if not webbrowser.open(url):
                     print(f"  Could not open browser for {url}")
                     continue
            opened_count += 1
        except Exception as e:
            print(f"  Error opening {url}: {e}")

    if opened_count > 0:
        print(f"\nOpened {opened_count} browser tabs/windows.")
        print("You will need to manually upload or paste your image into each service.")
    else:
        print("\nCould not open any web browser tabs automatically.")
        print("Please open your browser manually and navigate to the desired search sites.")

def get_image_path_from_user():
    """Prompts the user for the image path and validates it."""
    while True:
        image_path = input("Please enter the full path to the image file: ")
        # Basic check for existence
        if os.path.exists(image_path) and os.path.isfile(image_path):
            # Basic check for image file extension (can be improved)
            supported_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp')
            if image_path.lower().endswith(supported_extensions):
                return image_path
            else:
                print(f"Warning: File '{os.path.basename(image_path)}' might not be a supported image type.")
                confirm = input("Do you want to continue anyway? (y/n): ").lower()
                if confirm == 'y':
                    return image_path
                else:
                     print("Please provide a path to a valid image file.")
        else:
            print(f"Error: File not found or is not a file: '{image_path}'")
        print("-" * 20)


# --- Main Execution ---
if __name__ == "__main__":
    print("--- Image Search Opener ---")
    print("This script will open web browser tabs for reverse image search sites.")
    print("You need to manually upload your image to each site.")
    print("Warning: Respect site Terms of Service and privacy considerations.")
    print("-" * 28)

    try:
        image_path = get_image_path_from_user()
        open_search_sites(image_path)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

    print("\nScript finished.") 
