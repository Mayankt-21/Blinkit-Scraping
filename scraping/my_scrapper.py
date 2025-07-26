
## Imports
import tempfile
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random
import requests
import json
import random
from pretty_data import pretty_data

def my_scrapper(lat, lon, l0_cat,l0_cat_id, l1_cat,l1_cat_id,delay=30):
    
    ## Setup temp_profile for Browser
    temp_profile = tempfile.mkdtemp()

    ## Set Browser Options
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={temp_profile}")
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.geolocation": 1
    })

    ## Set the Driver and call the site
    driver = webdriver.Chrome(options=options)
    URL = "https://blinkit.com/"
    driver.get(URL)

    ## Setup Spoof Location
    driver.execute_cdp_cmd("Emulation.setGeolocationOverride",{
        "latitude":float(lat),
        "longitude":float(lon),
        "accuracy":100
    })

    ## Allow Page to Detect the Spoof -> Click Detect my location from Spoof Location
    location_detector =driver.find_element(By.XPATH , "//button[contains(text() , 'Detect my location')]")
    location_detector.click()
    sleep(3)

    ## Call the Public Backend API for categories
    
    for attempt in range(3):
        print(f"attempt: {attempt+1}")
        try:
            category_api = f'https://blinkit.com/v1/layout/listing_widgets?l0_cat={l0_cat}&l1_cat={l1_cat}'
            selenium_cookies = driver.get_cookies()
            cookies = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in selenium_cookies])
            
            response = driver.execute_async_script("""
                const category_api = arguments[0]
                const lat = arguments[1]
                const lon = arguments[2]
                const callback = arguments[3];
                fetch(category_api, {
                    method: 'POST',
                    headers: {
                        'User-Agent': navigator.userAgent,
                        'auth_key': localStorage.getItem('authKey'),
                        'accept-encoding':'gzip, deflate, br, zstd',
                        'accept-language':'en-US,en;q=0.9',
                        'access_token':'null',
                        'content-type': 'application/json',
                        'accept': '*/*',
                        'lat':lat,
                        'lon':lon,
                        'app_client': 'consumer_web',
                        'platform': 'desktop_web',
                        'origin': 'https://blinkit.com',
                        'referer': 'https://blinkit.com',
                    },
                    body: JSON.stringify({})
                })
                .then(res => res.text())
                .then(data => callback(data))
                .catch(err => callback('ERROR: ' + err.message));
            """ , category_api,lat,lon)
            
            # with open("response.json","w",encoding="utf-8") as f:
            #     f.write(response)
            
            if '"is_success":false' not in response:
                df = pretty_data(json.loads(response),l0_cat,l0_cat_id, l1_cat,l1_cat_id,lat,lon)
                driver.quit()
                return df
            else:
                print(f"Error Fetching, Retrying in {delay} sec...")
                sleep(delay)
        except Exception as e:
            print(f"Exception handling, Retrying in {delay} sec...")
            sleep(delay)
    
    # print("Page Title:",driver.title)
    driver.quit()
    print("Max retries reached. Skipping entry...")
    return None