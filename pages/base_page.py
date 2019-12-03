class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    # Open required page/link
    def open(self):
        self.browser.get(self.url)