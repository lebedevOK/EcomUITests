from selenium.webdriver.common.by import By

email_field_locator = (By.CSS_SELECTOR, "input#user_email")
password_field_locator = (By.CSS_SELECTOR, "input#user_password")
button_submit_locator = (By.CSS_SELECTOR, "input[type='submit'][value='Войти']")

error_message_locator = (By.XPATH, "//div[@class='text_to_center']/p[@class='alert' and text()]")
login_notice_locator = (By.XPATH, "//div[@class='text_to_center']/p[@class='notice' and normalize-space(text())]")

