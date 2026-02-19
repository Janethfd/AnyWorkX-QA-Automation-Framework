def test_fund_wallet_navigation(driver):
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="wallet_icon").click()
    driver.find_element(by=AppiumBy.TEXT, value="Fund").click()
    
    amount_input = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
    amount_input.send_keys("5000")
    
    driver.find_element(by=AppiumBy.TEXT, value="Continue").click()
   
    assert driver.find_element(by=AppiumBy.TEXT, value="Complete Payment").is_displayed()
