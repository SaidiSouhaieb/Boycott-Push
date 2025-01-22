import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import shutil


def scrap_getty(keyword):
    # url = f"https://www.gettyimages.com/photos/{keyword}"
    url = "https://www.gettyimages.com/search/2/image?family=creative%2Ceditorial&phrase=papa%20johns%20logo"
    categories = {f"{keyword}-getty": url}

    for category, url in categories.items():
        print(url)
        i = 0
        # Ensure the datasets/ directory exists
        os.makedirs(f"datasets/{category}", exist_ok=True)

        # Set up the Safari driver
        driver = webdriver.Chrome()
        # Open the URL
        driver.get(url)

        # pagination_number = driver.find_element(By.CLASS_NAME, 'JO4Dw2C5EjCB3iovKUcw').text
        # print(pagination_number)

        # for page_number in range(1, int(2) + 1):
        for page_number in range(1):
            images = []
            print(page_number)

            # new_url = url.replace('search_page=1', f'search_page={page_number}')
            new_url = url

            driver.get(new_url)

            # Give some time for the images to load
            time.sleep(5)
            imgs = driver.find_elements(By.CLASS_NAME, "BLA_wBUJrga_SkfJ8won")
            print(imgs)

            # Iterate over found images and download them
            for idx, img in enumerate(imgs):
                src = img.get_attribute("src")
                if src:
                    response = requests.get(src, stream=True)
                    if response.status_code == 200:
                        image_path = os.path.join(
                            f"datasets/{category}/", f"image_{i}.jpg"
                        )
                        with open(image_path, "wb") as out_file:
                            shutil.copyfileobj(response.raw, out_file)
                        print(f"Saved: {image_path}")
                        i += 1
                        pass
                    else:
                        print(f"Failed to retrieve image from {src}")
                else:
                    print(f"No src attribute found for image {idx}")

        # Close the browser for this category
        driver.quit()
