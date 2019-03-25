import time
from selenium import webdriver

#"http://psychology.duapp.com/admin/test_list.php" dass
#"http://psychology.duapp.com/admin/testnew_list.php" trauma
#//*[@id="main"]/div/div[1]/a[3]
class WebSnap(object):
    """websnapshot
    """
    _browser = None

    def __init__(self):
        self._browser = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver_win32\\chromedriver")
        self._browser.set_window_size(1400, 1400)
        self._browser.maximize_window() 

    def login(self):
        """login"""
        ret = False
        self._browser.get("http://bdxl.dev.ftbj.net/admin/test_list.php")
        self._browser.find_element_by_id("userid").click()
        self._browser.find_element_by_id("userid").send_keys("admin")
        self._browser.find_element_by_id("password").click()
        self._browser.find_element_by_id("password").send_keys("123456")
        self._browser.find_element_by_id("loginBtn").click()

        while True:
            allbreak = False
            time.sleep(2)
            elems = self._browser.find_elements_by_class_name("div2")
            length = len(elems)
            markaddr = "DAS测试列表"
            for i in range(0, length):
                #print elems[i].get_attribute("href")
                if elems[i].text == markaddr:
                    allbreak = True
                    ret = True
                    break

            if allbreak:
                break

        return ret

    def goto_page_one(self):
        """go to page 1"""
        """addr = "http://psychology.duapp.com/action/listAction.php?action=adtestlist"
        elems = self._browser.find_elements_by_class_name("div2")
        length = len(elems)
        for i in range(0, length):
            if elems[i].get_attribute("href") == addr:
                elems[i].click()"""
        elem = self._browser.find_element_by_xpath('//*[@id="main"]/div/div[1]/a[3]')
        elem.click()


    def goto_page_two(self):
        """go to page 2"""
        """addr = "http://psychology.duapp.com/action/listAction.php?action=adnewtestlist"
        elems = self._browser.find_elements_by_class_name("div2")
        length = len(elems)
        for i in range(0, length):
            if elems[i].get_attribute("href") == addr:
                elems[i].click()"""
        elem = self._browser.find_element_by_xpath('//*[@id="main"]/div/div[1]/a[4]')
        elem.click()

    def goto_page_mood(self):
        """go to mood page"""
        elem = self._browser.find_element_by_xpath('//*[@id="main"]/div/div[1]/a[2]')
        elem.click()

    def table_page_loaded(self):
        """if a table page is loaded"""
        trs = self._browser.find_elements_by_tag_name("tr")
        if len(trs) == 21:
            return True
        else:
            return False

    def flip(self):
        """flip to next page"""
        #next_btn = self._browser.find_element_by_class_name("prv")
        next_btn = self._browser.find_element_by_class_name("next")
        if next_btn != None:
            next_btn.click()

    def snap_shot(self, name):
        """print screen"""
        self._browser.save_screenshot("D:\\output\\" + str(name) + ".png")

    def yscroll_off(self):
        """scroll y"""
        self._browser.execute_script("window.scroll(0, 40);")

if __name__ == "__main__":
    OP = WebSnap()
    if OP.login() is True:
        OP.goto_page_one()
        #OP.goto_page_two()
        #OP.goto_page_mood()

        for n in range(0, 2600):#1141, 968, 116
            #OP.yscroll_off()
           # time.sleep(1)
            OP.snap_shot(n + 1)
            OP.flip()
            while not OP.table_page_loaded():
                time.sleep(1)

        input("its done please press Enter")
