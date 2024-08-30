from selenium import webdriver

class DriverFactory:

    @staticmethod
    def get_driver(browser_name="chrome"):
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")  # Run in headless mode
            options.add_argument('--no-sandbox')  # Required for Docker
            options.add_argument('--disable-dev-shm-usage')  # Required for Docker
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920x1080")
            driver = webdriver.Chrome(options=options)
        else:
            raise ValueError("Browser not supported")
        driver.maximize_window()
        return driver
