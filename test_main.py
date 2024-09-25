import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature('Menu Navigation')
@allure.suite('Main Menu Test Suite')
@allure.title('Test Main Menu Items Clickability')
@allure.description('Verifying that the main menu items on the TutorialsNinja website are clickable and load the correct pages.')
@allure.severity(allure.severity_level.CRITICAL)
def test_menu_item(driver):
    with allure.step('Opening the TutorialsNinja homepage'):
        driver.get('https://tutorialsninja.com/demo/')
    expected_menu_items = ["Desktops", "Laptops & Notebooks", "Components","Tablets", "Software", "Phones & PDAs", "Cameras", "MP3 Players"]

    with allure.step(f'Clicking on menu item: {expected_menu_items[0]}'):
        menu_item1 = driver.find_element(By.LINK_TEXT, expected_menu_items[0])
        menu_item1.click()

    with allure.step(f'Clicking on menu item: {expected_menu_items[1]}'):
        menu_item2 = driver.find_element(By.LINK_TEXT, expected_menu_items[1])
        menu_item2.click()

    with allure.step(f'Clicking on menu item: {expected_menu_items[2]}'):
        menu_item3 = driver.find_element(By.LINK_TEXT, expected_menu_items[2])
        menu_item3.click()

    with allure.step(f'Clicking on menu item: {expected_menu_items[3]}'):
        menu_item4 = driver.find_element(By.LINK_TEXT, expected_menu_items[3])
        menu_item4.click()
    with allure.step(f'Asserting page heading for: {expected_menu_items[3]}'):
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[3]

    with allure.step(f'Clicking on menu item: {expected_menu_items[4]}'):
        menu_item5 = driver.find_element(By.LINK_TEXT, expected_menu_items[4])
        menu_item5.click()
    with allure.step(f'Asserting page heading for: {expected_menu_items[4]}'):
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[4]
    with allure.step(f'Clicking on menu item: {expected_menu_items[5]}'):
        menu_item6 = driver.find_element(By.LINK_TEXT, expected_menu_items[5])
        menu_item6.click()
    with allure.step(f'Asserting page heading for: {expected_menu_items[5]}'):
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[5]
    with allure.step(f'Clicking on menu item: {expected_menu_items[6]}'):
        menu_item7 = driver.find_element(By.LINK_TEXT, expected_menu_items[6])
        menu_item7.click()

    with allure.step(f'Asserting page heading for: {expected_menu_items[6]}'):
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[6]

    with allure.step(f'Clicking on menu item: {expected_menu_items[7]}'):
        menu_item8 = driver.find_element(By.LINK_TEXT, expected_menu_items[7])
        menu_item8.click()

@pytest.mark.parametrize("menu_locator, submenu_locator, result_text", [
    (
            (By.PARTIAL_LINK_TEXT, 'Desktops'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[1]/a'),
            'PC'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Desktops'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[2]/a'),
            'Mac'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Laptops & Notebooks'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[1]/a'),
            'Macs'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Laptops & Notebooks'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[2]/a'),
            'Windows'
    )
])
@allure.feature('Menu Navigation')
@allure.suite('Menu Test Suite')
@allure.title('Test Menu and Submenu Navigation')
@allure.description('Test to ensure that menu and submenu links lead to correct pages.')
@allure.severity("critical")
def test_nested_menu(driver, menu_locator, submenu_locator, result_text):
    with allure.step("Open the TutorialsNinja demo site"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step(f"Hover over the menu and select submenu: {result_text}"):
        menu = driver.find_element(*menu_locator)
        submenu = driver.find_element(*submenu_locator)
        ActionChains(driver).move_to_element(menu).click(submenu).perform()

    with allure.step(f"Check that the page header matches '{result_text}'"):
        assert driver.find_element(By.TAG_NAME, 'h2').text == result_text

@allure.feature('Product Search')
@allure.suite('Search Functionality Tests')
@allure.title('Test Search for MacBook')
@allure.description(
    'This test verifies the search functionality by searching for MacBook and ensuring all products in the results contain "MacBook" in their name.')
@allure.severity("critical")
def test_search_product(driver):
    with allure.step("Navigate to the Tutorials Ninja homepage"):
        driver.get('https://tutorialsninja.com/demo/index.php?route=common/home')

    with allure.step("Enter 'MacBook' into the search field"):
        search = driver.find_element(By.NAME, 'search')
        search.send_keys('MacBook')

    with allure.step("Click on the search button"):
        button = driver.find_element(By.XPATH, '//*[@id="search"]/span/button')
        button.click()

    with allure.step("Validate search results"):
        products = driver.find_elements(By.TAG_NAME, 'h4')
        new_list = [elem.text for elem in products if 'MacBook' in elem.text]
        assert len(products) == len(new_list), "Some products do not contain 'MacBook' in their title"

@allure.feature('Shopping Cart')
@allure.suite('Add to Cart Functionality')
@allure.title('Test Adding MacBook to Cart')
@allure.description('This test adds a MacBook product to the cart, checks for the success message, and verifies that the cart contains 1 item and includes the MacBook.')
@allure.severity("critical")
def test_add_cart(driver):
    with allure.step("Navigate to the Tutorials Ninja homepage"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step("Add the first product (MacBook) to the cart"):
        product = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[1]')
        product.click()

    with allure.step("Verify success message appears"):
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success"))
        )

        assert "Success: You have added" in success_message.text

    with allure.step("Verify that the cart contains 1 item"):
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "cart-total"), "1 item(s)")
        )

    with allure.step("Open the cart and verify its contents"):
        cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "cart"))
        )
        cart_button.click()

        cart_contents = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.dropdown-menu.pull-right"))
        )

        assert "MacBook" in cart_contents.text, f"Expected 'MacBook' in cart, but got"
@allure.feature('Homepage Slider')
@allure.suite('Slider Navigation Tests')
@allure.title('Test Slider Navigation Functionality')
@allure.description('This test verifies that the slider on the homepage can navigate between images using the next and previous arrows.')
@allure.severity("normal")
def test_slider_functionality(driver):
    with allure.step("Navigate to the Tutorials Ninja homepage"):
        driver.get('https://tutorialsninja.com/demo/')

    with allure.step("Verify the slider is displayed"):
        slider = driver.find_element(By.CLASS_NAME, 'swiper-container')
        assert slider.is_displayed(), "Slider is not visible on the page"

    with allure.step("Capture the first slide image source"):
        first_slide = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img")
        first_slide_src = first_slide.get_attribute("src")

    with allure.step("Click on the next arrow and wait for the slide to change"):
        next_arrow = driver.find_element(By.CLASS_NAME, 'swiper-button-next')
        ActionChains(driver).move_to_element(slider).click(next_arrow).perform()

        WebDriverWait(driver, 10).until_not(
            EC.element_to_be_clickable(first_slide)
        )

    with allure.step("Verify the slide has changed"):
        new_slide = driver.find_element(By.CSS_SELECTOR, '.swiper-slide-active img')
        new_slide_src = new_slide.get_attribute("src")
        assert first_slide_src != new_slide_src, "Slider did not move to the next image."

    with allure.step("Click on the previous arrow and return to the first image"):
        prev_arrow = driver.find_element(By.CLASS_NAME, 'swiper-button-prev')
        prev_arrow.click()

        WebDriverWait(driver, 10).until_not(
            EC.element_to_be_clickable(new_slide)
        )

    with allure.step("Verify the slider returned to the first image"):
        reverted_slide_src = driver.find_element(By.CSS_SELECTOR, '.swiper-slide-active img').get_attribute("src")
        assert reverted_slide_src == first_slide_src, "Slider did not return to the first image."

@pytest.mark.parametrize("button, header, expected_text", [
    (
        (By.XPATH, '/html/body/footer/div/div/div[1]/ul/li[1]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "About Us"
    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[2]/ul/li[1]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "Contact Us"
    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[2]/ul/li[2]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "Product Returns"
    ),
    (
        (By.XPATH, "/html/body/footer/div/div/div[3]/ul/li[1]/a"),
        (By.XPATH, '//*[@id="content"]/h1'),
        "Find Your Favorite Brand"
    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[3]/ul/li[2]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "Purchase a Gift Certificate"
    )
])
@allure.feature('Footer Links Navigation')
@allure.suite('Footer Navigation Suite')
@allure.title('Test Footer Navigation to "{expected_text}" Page')
@allure.description('This test verifies that clicking footer links navigates to the correct pages by checking the page headers.')
@allure.severity("normal")
def test_footer(driver, button, header, expected_text):
    with allure.step("Navigate to the Tutorials Ninja homepage"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step(f"Click the footer link for {expected_text}"):
        footer_button = driver.find_element(*button)
        footer_button.click()

    with allure.step(f"Verify the page header matches '{expected_text}'"):
        footer_header_text = driver.find_element(*header).text
        assert footer_header_text == expected_text, f"Expected '{expected_text}' but got '{footer_header_text}'"

@allure.feature('Wishlist Functionality')
@allure.suite('User Actions')
@allure.title('Add Product to Wishlist')
@allure.description('Test to verify if a user can successfully add a product to the wishlist and view it.')
@allure.severity("critical")


@allure.feature('Wishlist Functionality')
@allure.suite('Add to Wishlist Tests')
@allure.title('Test Adding MacBook to Wishlist')
@allure.description('This test verifies adding a MacBook to the wishlist and checking that the product appears on the wishlist page.')
@allure.severity("critical")
def test_add_wishlist(driver, login):
    driver.get('https://tutorialsninja.com/demo/index.php?route=common/home')

    with allure.step('Click on the wishlist button of the first product'):
        wishlist_button = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[2]')
        wishlist_button.click()

    with allure.step('Verify success message is displayed'):
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-success"))
        )
        assert "Success: You have added" in success_message.text, "Failed to add product to wishlist"

    with allure.step('Check that the wishlist count updated to 1'):
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'wishlist-total'), '1')
        )
        assert '1' in driver.find_element(By.ID, 'wishlist-total').text, "Wishlist count did not update"

    with allure.step('Navigate to the wishlist page'):
        wishlist_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="wishlist-total"]'))
        )
        wishlist_link.click()

    with allure.step('Verify that the wishlist page is displayed'):
        WebDriverWait(driver, 10).until(EC.title_contains("Wish List"))

    with allure.step('Verify the product is displayed in the wishlist'):
        wishlist_product = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/table/tbody/tr/td[2]/a'))
        )
        assert wishlist_product.is_displayed(), "Product is not displayed in the wishlist"

