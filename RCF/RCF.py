import time

from select import select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:/Users/selenium/work space/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(2)
driver.get(
    "https://regqc.sifyitest.com/rcfmodec22/reg_details.php?q=N2Q2ZGRhNDA1NjFlZTY3OTBkNjc4YTZlNWNlNGIwYmN8MjQ5MDAwMDE1")
driver.find_element(By.XPATH, "(//input[@id='opt_cat'])[1]").click()
alert = driver.switch_to.alert
alert.accept()
driver.find_element(By.XPATH, "//input[@id='optdisability'][1]").click()

Dropdown1 = Select(driver.find_element(By.XPATH, "//*[@id='disability_type']"))
D1 = Dropdown1.select_by_index(1)
print(driver.current_url)
print(driver.title)  # p = property m = method
# assert  driver.find_element(By.XPATH, "//*[@id='disability_type']").get_attribute("value") =="OA" (Applicable only wneh u enter in AUto ssusgestive drop down)


# assert "OA" in D1 (only messages not dropdowns)
# Locators ID, Name, ClassName, Css, Xpath, Link text and partial link text
# Css -> Tagname[attribute = 'value'], ".ClassNmae", "#ID"
# X path -> //Tagname[@attribute = 'value']
# tag name starts with 'a' anchar then we can use link test or partial link test.

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
CheckBoxes = driver.find_elements(By.ID, "checkBoxOption")
for checkbox in CheckBoxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        checkbox.is_selected()
        break
radios = driver.find_elements(By.CLASS_NAME, "radioButton")
for radio in radios:
    if radio.get_attribute("Value") == "Radio2":
        radio.click()
        radio.is_selected()
        break
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("hari")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)
assert "hari" in alerttext

if alerttext == "hari":
    print("Successfully executed")
else:
    print("Failed")

if "hari" in alerttext:
    print("Successfully executed")
else:
    print("Failed")
alert.accept()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
driver.find_element(By.CSS_SELECTOR, ".search-button").click()
products = driver.find_elements(By.XPATH, "(//div[@class='product'])")
count = len(products)
assert count == 3
if count > 0 in products:
    print("Count equals to 3")
else:
    print("Count not equal to 3")
for product in products:
    if product == "Cucumber - 1 Kg":
        product.click()
