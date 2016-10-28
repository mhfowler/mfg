from selenium import webdriver

BASE_URL = 'https://en.wikipedia.org/wiki/List_of_proverbial_phrases'

def search(q):
    """returns image urls from mediachain for a given query"""
    driver = webdriver.Firefox()
    driver.get('{}'.format(BASE_URL))
    img_els = driver.find_elements_by_css_selector('.img-responsive')
    imgs = [el.get_attribute('src') for el in img_els]
    driver.quit()
    return imgs


if __name__ == '__main__':
    import os
    print os.environ.get('PATH')
    print search('frog')