import time

from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_guest_should_see_cart_button(browser):
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button, 'Cелектор кнопки не найден'
    print(button)
    time.sleep(30)
