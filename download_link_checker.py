from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# This tool is not done yet


if __name__ == "__main__":
    # Replace path with your path to chromedriver
    chromedriver_path = "C:/Users/allk3/Documents/myprogs/libraries/chromedriver-win64/chromedriver-win64/chromedriver.exe"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--auto-open-devtools-for-tabs")

    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.execute_cdp_cmd("Network.enable", {})

    requests = []

    def capture_request(request):
        if 'url' in request['request']:
            requests.append(request['request']['url'])

    driver.execute_cdp_cmd("Network.requestWillBeSent", {'request': capture_request})

    driver.get("https://download.gimp.org/gimp/v2.10/windows/gimp-2.10.38-setup.exe")

    time.sleep(10)

    download_button = driver.find_element(By.LINK_TEXT, "Download GIMP 2.10.34 directly")
    download_button.click()

    time.sleep(30)

    for request in requests:
        if "gimp" in request:
            print(request)

    driver.quit()
