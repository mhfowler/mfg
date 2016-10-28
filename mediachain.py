from selenium import webdriver

BASE_URL = 'http://images.mediachain.io/search'

def search(q):
    """returns image urls from mediachain for a given query"""
    driver = webdriver.Firefox()
    driver.get('{}/{}'.format(BASE_URL, q))
    img_els = driver.find_elements_by_css_selector('.img-responsive')
    imgs = [el.get_attribute('src') for el in img_els]
    driver.quit()
    return imgs
