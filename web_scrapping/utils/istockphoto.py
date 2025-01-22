import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import shutil


def scrap_istock_photo(keyword):
    # Categories to search and download images for
    categories = {
        f"{keyword}-shutterstock": f"https://www.istockphoto.com/search/2/image-film?phrase={keyword}"
    }

    for category, url in categories.items():
        print(url)
        i = 0
        os.makedirs(f"datasets/{category}", exist_ok=True)

        driver = webdriver.Chrome()

        driver.get(url)

        for page_number in range(1):
            images = []

            new_url = url

            driver.get(new_url)

            # Give some time for the images to load
            time.sleep(5)

            imgs = driver.find_elements(By.CLASS_NAME, "yGh0CfFS4AMLWjEE9W7v")
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

        driver.quit()
