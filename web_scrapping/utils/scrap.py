from utils.getty import scrap_getty
from utils.istockphoto import scrap_istock_photo


def scrap():
    keywords = ["papa-johns-logo", "papa johns"]
    scrap_getty(keywords[0])
    scrap_istock_photo(keywords[1])
