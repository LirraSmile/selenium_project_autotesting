from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    #инициализация Page Object, передача в конструктор 
    # экземпляра драйвера и url-адреса
    page = MainPage(browser, link)
    #открыть страницу
    page.open()
    #выполнить метод страницы - переход на страницу резистрация/логин
    page.go_to_login_page()
    