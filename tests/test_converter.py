from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/index.html")


def clear_hex():
    driver.find_element(By.ID, "hexInput").clear()


def clear_rgb():
    driver.find_element(By.ID, "rInput").clear()
    driver.find_element(By.ID, "gInput").clear()
    driver.find_element(By.ID, "bInput").clear()


def run_hex_test(value, expected_result=None, expected_error=None):
    clear_hex()

    driver.find_element(By.ID, "hexInput").send_keys(value)
    driver.find_element(By.ID, "hexToRgbBtn").click()

    if expected_result is not None:
        result = driver.find_element(By.ID, "rgbResult").text
        assert result == expected_result

    if expected_error is not None:
        error = driver.find_element(By.ID, "hexError").text
        assert expected_error in error


def run_rgb_test(r, g, b, expected_result=None, expected_error=None):
    clear_rgb()

    if r is not None:
        driver.find_element(By.ID, "rInput").send_keys(str(r))

    if g is not None:
        driver.find_element(By.ID, "gInput").send_keys(str(g))

    if b is not None:
        driver.find_element(By.ID, "bInput").send_keys(str(b))

    driver.find_element(By.ID, "rgbToHexBtn").click()

    if expected_result is not None:
        result = driver.find_element(By.ID, "hexResult").text
        assert result == expected_result

    if expected_error is not None:
        error = driver.find_element(By.ID, "rgbError").text
        assert expected_error in error


# 1. Valid HEX with #
run_hex_test(
    "#FF5733",
    expected_result="rgb(255, 87, 51)"
)
print("Test 1 passed: Valid HEX with #")


# 2. Valid HEX without #
run_hex_test(
    "00FF00",
    expected_result="rgb(0, 255, 0)"
)
print("Test 2 passed: Valid HEX without #")


# 3. Lowercase HEX
run_hex_test(
    "#ff0000",
    expected_result="rgb(255, 0, 0)"
)
print("Test 3 passed: Lowercase HEX")


# 4. Invalid HEX characters
run_hex_test(
    "#GGGGGG",
    expected_error="Invalid HEX"
)
print("Test 4 passed: Invalid HEX characters detected")


# 5. Too-short HEX
run_hex_test(
    "#FFF",
    expected_error="Invalid HEX"
)
print("Test 5 passed: Short HEX detected")


# 6. Empty HEX
clear_hex()

driver.find_element(By.ID, "hexToRgbBtn").click()

error = driver.find_element(By.ID, "hexError").text
assert "Please enter a HEX value" in error

print("Test 6 passed: Empty HEX detected")


# 7. Valid RGB
run_rgb_test(
    255, 87, 51,
    expected_result="#FF5733"
)
print("Test 7 passed: Valid RGB")


# 8. RGB lower boundary
run_rgb_test(
    0, 0, 0,
    expected_result="#000000"
)
print("Test 8 passed: RGB lower boundary")


# 9. RGB upper boundary
run_rgb_test(
    255, 255, 255,
    expected_result="#FFFFFF"
)
print("Test 9 passed: RGB upper boundary")


# 10. Missing RGB field
run_rgb_test(
    255, 0, None,
    expected_error="Please enter all three RGB values"
)
print("Test 10 passed: Missing RGB value detected")


# 11. Negative RGB value
run_rgb_test(
    -1, 50, 50,
    expected_error="0 to 255"
)
print("Test 11 passed: Negative RGB value detected")


# 12. RGB above 255
run_rgb_test(
    300, 20, 50,
    expected_error="0 to 255"
)
print("Test 12 passed: RGB value above 255 detected")


time.sleep(2)

driver.quit()

print("\nAll 12 Selenium tests passed successfully.")