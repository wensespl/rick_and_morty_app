import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

capabilities = dict(
    platformName="Android",
    automationName="UiAutomator2",
    deviceName="Pixel 2 API 29",
    appPackage="com.example.rick_and_morty_app",
    appActivity=".MainActivity",
)
options = UiAutomator2Options().load_capabilities(capabilities)

appium_server_url = "http://localhost:4723"


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_title(self) -> None:
        wait = WebDriverWait(self.driver, 20)

        waiting_for = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "Rick and Morty")
            )
        )
        title = self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="Rick and Morty"
        )

        self.assertEqual(title.get_attribute("content-desc"), "Rick and Morty")

    def test_equal_title(self) -> None:
        wait = WebDriverWait(self.driver, 20)

        waiting_for = wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Morty Smith"))
        )
        card = self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="Morty Smith"
        )
        card_text = card.get_attribute("content-desc")
        card.click()

        waiting_for = wait.until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Morty Smith"))
        )
        title = self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="Morty Smith"
        )
        title_text = title.get_attribute("content-desc")

        self.assertEqual(title_text, card_text)

    def test_search_button(self) -> None:
        wait = WebDriverWait(self.driver, 20)

        waiting_for = wait.until(
            EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.Button"))
        )
        button = self.driver.find_element(
            by=AppiumBy.CLASS_NAME, value="android.widget.Button"
        )
        button.click()

        waiting_for = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.CLASS_NAME, "android.widget.EditText")
            )
        )
        search_EditText = self.driver.find_element(
            by=AppiumBy.CLASS_NAME, value="android.widget.EditText"
        )

        self.assertEqual(search_EditText.get_attribute("hint"), "Search")

    def test_search_text(self) -> None:
        wait = WebDriverWait(self.driver, 20)

        waiting_for = wait.until(
            EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.Button"))
        )
        button = self.driver.find_element(
            by=AppiumBy.CLASS_NAME, value="android.widget.Button"
        )
        button.click()

        waiting_for = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.CLASS_NAME, "android.widget.EditText")
            )
        )
        search_EditText = self.driver.find_element(
            by=AppiumBy.CLASS_NAME, value="android.widget.EditText"
        )
        search_EditText.send_keys("rick")

        text = search_EditText.text

        waiting_for = wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Rick Sanchez"))
        )
        option = self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="Rick Sanchez"
        )
        option.click()

        waiting_for = wait.until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Episodes"))
        )
        title = self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="Rick Sanchez"
        )
        title_text = title.get_attribute("content-desc")

        self.assertEqual("Rick Sanchez", title_text)
        self.assertEqual(text, "rick")

    def test_scroll(self) -> None:
        wait = WebDriverWait(self.driver, 20)

        waiting_for = wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Morty Smith"))
        )

        self.driver.swipe(779, 1679, 784, 352)
        self.driver.swipe(779, 1637, 791, 321)

        waiting_for = wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Antenna Morty"))
        )
        card = self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="Antenna Morty"
        )
        card_text = card.get_attribute("content-desc")
        card.click()

        waiting_for = wait.until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Antenna Morty"))
        )
        title = self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="Antenna Morty"
        )
        title_text = title.get_attribute("content-desc")

        self.assertEqual(title_text, card_text)


if __name__ == "__main__":
    unittest.main()
