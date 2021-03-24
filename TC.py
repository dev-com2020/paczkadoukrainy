import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Respons_test import respons_check

class TC_complete_with_errors():
    def webdriver_choose(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url='https://paczkadoukrainy.pl')
        driver.maximize_window()
        print("Webdriver OK!")

    def parcelWeight(self):
        driver.find_element_by_name('parcelWeight').send_keys("10")
        driver.find_element_by_css_selector(".btn:nth-child(5)").click()
        time.sleep(3)
        print("Parcel weight OK!")

    def inpost_select(self):
        driver.find_element_by_css_selector('.row:nth-child(1) > .col-12 > .card .btn').click()
        print("Inpost select OK!")

    def deliveryType(self):
        driver.find_element_by_css_selector('.col-sm-5 .custom-control-label').click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='collapseTwoAndHalf']/div/section/div[1]/div/div/div[3]/div/label/span").click()
        driver.find_element_by_xpath('//*[@id="pickupPointKey"]/div[1]/input').click()
        print("Delivery Type select!")

    def adress_data(self):
        driver.find_element_by_xpath('//*[@id="pickupPointKey"]/div[2]/div/div/div[3]/div/div/span').click()
        driver.find_element_by_xpath('//*[@id="senderName"]').send_keys("Monika Mazurek")
        driver.find_element_by_xpath('//*[@id="senderPostalCode"]').send_keys("25-663")
        driver.find_element_by_xpath('//*[@id="senderCity"]').send_keys("Kielce")
        driver.find_element_by_xpath('//*[@id="senderStreet"]').send_keys("Olszewskiego")
        driver.find_element_by_xpath('//*[@id="senderHouseNumber"]').send_keys("6")
        driver.find_element_by_xpath('//*[@id="senderFlatNumber"]').send_keys("313")
        driver.find_element_by_xpath('//*[@id="senderPhone"]').send_keys("664540929")
        driver.find_element_by_xpath('//*[@id="senderEmail"]').send_keys("monika@sourceful.nl")
        driver.find_element_by_xpath('//*[@id="receiverName"]').send_keys("Наталя Иванова")
        driver.find_element_by_xpath('//*[@id="receiverPhone"]').send_keys("+48505032236")
        driver.find_element_by_xpath('//*[@id="receiverEmail"]').send_keys("natalia@ivanova.pl")
        driver.save_screenshot("bad_pick.png")
        print("Sender and Receiver data OK!")

    def declaration(self):
        driver.find_element_by_xpath('//*[@id="parcelItemDescription"]').send_keys("Czekoladki")
        driver.find_element_by_xpath('//*[@id="parcelItemQuantity"]').send_keys("2")
        driver.find_element_by_xpath('//*[@id="parcelItemWeight"]').send_keys("8")
        driver.find_element_by_xpath('//*[@id="parcelItemValueClientCurrency"]').send_keys("20")
        driver.find_element_by_xpath('//*[@id="dutyDeclaration"]/div/div[4]/div/button').click()
        driver.find_element_by_name('parcelItemDescription-1').send_keys("Kubek")
        driver.find_element_by_name('parcelItemQuantity-1').send_keys("1")
        driver.find_element_by_name('parcelItemWeight-1').send_keys("2")
        driver.find_element_by_name('parcelItemValueClientCurrency-1').send_keys("5")
        driver.save_screenshot("bad_kg.png")
        print("Declaration OK!")

    def checkedPoint(self):
        time.sleep(3)
        osw_1 = driver.find_element_by_xpath('.//*[@id="anchorOrderForm"]/fieldset/div[2]/div/div/label')
        osw_1.location_once_scrolled_into_view
        osw_1.click()
        driver.find_element_by_xpath('.//*[@id="anchorOrderForm"]/fieldset/div[3]/div/div/label').click()
        driver.find_element_by_xpath('.//*[@id="anchorOrderForm"]/fieldset/div[4]/div/div/label').click()
        driver.find_element_by_xpath('.//*[@id="anchorOrderForm"]/fieldset/div[5]/div/div/label').click()
        driver.save_screenshot("4osw.png")
        driver.find_element_by_xpath('//*[@id="btn_next_step"]').click()
        print("All requirements points check!")

    def payment(self):
        pay = driver.find_element_by_xpath('.//*[@id="js-calculator-content"]/section[2]/div[9]/div[2]/button')
        pay.location_once_scrolled_into_view
        pay.click()
        time.sleep(5)
        driver.save_screenshot("end.png")
        driver.close()
        print("all TC done!\nTest wykonano z błędnymi wartościami")

class TC_bad_pickup():
    def webdriver_choose(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url='https://paczkadoukrainy.pl')
        driver.maximize_window()
        print("Webdriver OK!")

    def parcelWeight(self):
        driver.find_element_by_name('parcelWeight').send_keys("10")
        driver.find_element_by_css_selector(".btn:nth-child(5)").click()
        time.sleep(3)
        print("Parcel weight OK!")

    def inpost_select(self):
        driver.find_element_by_css_selector('.row:nth-child(1) > .col-12 > .card .btn').click()
        print("Inpost select OK!")

    def deliveryType(self):
        driver.find_element_by_css_selector('.col-sm-5 .custom-control-label').click()
        time.sleep(3)
        nova = driver.find_element_by_xpath("//*[@id='collapseTwoAndHalf']/div/section/div[1]/div/div/div[3]/div/label/span")
        nova.click()
        nova.location_once_scrolled_into_view
        driver.find_element_by_xpath('//*[@id="pickupPointKey"]/div[1]/input').click()
        driver.find_element_by_xpath('//*[@id="pickupPointKey"]/div[1]/input').send_keys("Cherkaska 18")
        driver.save_screenshot("bad_delivery.png")
        print("Delivery point not exist!")
        driver.close()
        print("TC#1 done!")

class TC_bad_kg():
    def webdriver_choose(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url='https://paczkadoukrainy.pl')
        driver.maximize_window()
        print("Webdriver OK!")

    def parcelWeight(self):
        driver.find_element_by_name('parcelWeight').send_keys("10")
        driver.find_element_by_css_selector(".btn:nth-child(5)").click()
        time.sleep(3)
        print("Parcel weight OK!")

    def inpost_select(self):
        driver.find_element_by_css_selector('.row:nth-child(1) > .col-12 > .card .btn').click()
        print("Inpost select OK!")

    def deliveryType(self):
        driver.find_element_by_css_selector('.col-sm-5 .custom-control-label').click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='collapseTwoAndHalf']/div/section/div[1]/div/div/div[3]/div/label/span").click()
        driver.find_element_by_xpath('//*[@id="pickupPointKey"]/div[1]/input').click()
        print("Delivery Type select!")
    def adress_data(self):
        driver.find_element_by_xpath('//*[@id="pickupPointKey"]/div[2]/div/div/div[3]/div/div/span').click()
        driver.find_element_by_xpath('//*[@id="senderName"]').send_keys("Monika Mazurek")
        driver.find_element_by_xpath('//*[@id="senderPostalCode"]').send_keys("25-663")
        driver.find_element_by_xpath('//*[@id="senderCity"]').send_keys("Kielce")
        driver.find_element_by_xpath('//*[@id="senderStreet"]').send_keys("Olszewskiego")
        driver.find_element_by_xpath('//*[@id="senderHouseNumber"]').send_keys("6")
        driver.find_element_by_xpath('//*[@id="senderFlatNumber"]').send_keys("313")
        driver.find_element_by_xpath('//*[@id="senderPhone"]').send_keys("664540929")
        driver.find_element_by_xpath('//*[@id="senderEmail"]').send_keys("monika@sourceful.nl")
        driver.find_element_by_xpath('//*[@id="receiverName"]').send_keys("Наталя Иванова")
        driver.find_element_by_xpath('//*[@id="receiverPhone"]').send_keys("+48505032236")
        driver.find_element_by_xpath('//*[@id="receiverEmail"]').send_keys("natalia@ivanova.pl")
        driver.save_screenshot("bad_pick.png")
        print("Sender and Receiver data OK!")
    def declaration(self):
        driver.find_element_by_xpath('//*[@id="parcelItemDescription"]').send_keys("Czekoladki")
        driver.find_element_by_xpath('//*[@id="parcelItemQuantity"]').send_keys("2")
        driver.find_element_by_xpath('//*[@id="parcelItemWeight"]').send_keys("10")
        driver.find_element_by_xpath('//*[@id="parcelItemValueClientCurrency"]').send_keys("20")
        driver.find_element_by_xpath('//*[@id="dutyDeclaration"]/div/div[4]/div/button').click()
        driver.find_element_by_name('parcelItemDescription-1').send_keys("Kubek")
        driver.find_element_by_name('parcelItemQuantity-1').send_keys("1")
        driver.find_element_by_name('parcelItemWeight-1').send_keys("2")
        driver.find_element_by_name('parcelItemValueClientCurrency-1').send_keys("5")
        driver.save_screenshot("bad_kg.png")
        print("Bad value in package declaration (kg>10), validator is OK!")

class TC_validate_form_adress():
    def webdriver_choose(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url='https://paczkadoukrainy.pl')
        driver.maximize_window()
        print("Webdriver OK!")

    def parcelWeight(self):
        driver.find_element_by_name('parcelWeight').send_keys("10")
        driver.find_element_by_css_selector(".btn:nth-child(5)").click()
        time.sleep(3)
        print("Parcel weight OK!")

    def inpost_select(self):
        driver.find_element_by_css_selector('.row:nth-child(1) > .col-12 > .card .btn').click()
        print("Inpost select OK!")

    def deliveryType(self):
        driver.find_element_by_css_selector('.col-sm-5 .custom-control-label').click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='collapseTwoAndHalf']/div/section/div[1]/div/div/div[3]/div/label/span").click()
        driver.find_element_by_xpath('//*[@id="pickupPointKey"]/div[1]/input').click()
        print("Delivery Type select!")

    def adress_data(self):
        driver.find_element_by_xpath('//*[@id="pickupPointKey"]/div[2]/div/div/div[3]/div/div/span').click()
        driver.find_element_by_xpath('//*[@id="senderName"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="senderPostalCode"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="senderCity"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="senderStreet"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="senderHouseNumber"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="senderFlatNumber"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="senderPhone"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="senderEmail"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="receiverName"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="receiverPhone"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="receiverEmail"]').send_keys("")
        driver.save_screenshot("bad_pick.png")
        print("Form input null - validator is OK!")



def main():
    print("-" * 20)
    print("Przypadki testów funkcjonalnych dla https://paczkadoukrainy.pl")
    print("-" * 20)
    print("Wybierz test:\n1.uruchom test z błędnymi danymi\n2.uruchom tc#1 ukazujący błędny adres odbioru"
          "\n3.uruchom tc#2 ukazujący błędną ilość kg w deklaracji\n4.uruchom tc#3 ukazujący działanie walidatora formularza adresowego"
          "\n5.uruchom test responsywności strony")
    wybor = input("wprowadź:(1-5)")
    if(wybor == "1"):
        run = TC_complete_with_errors()
        run.webdriver_choose()
        run.parcelWeight()
        run.inpost_select()
        run.deliveryType()
        run.adress_data()
        run.declaration()
        run.checkedPoint()
        run.payment()
    elif(wybor == "2"):
        run_tc1 = TC_bad_pickup()
        run_tc1.webdriver_choose()
        run_tc1.parcelWeight()
        run_tc1.inpost_select()
        run_tc1.deliveryType()
    elif(wybor == "3"):
        run_tc2 = TC_bad_kg()
        run_tc2.webdriver_choose()
        run_tc2.parcelWeight()
        run_tc2.inpost_select()
        run_tc2.deliveryType()
        run_tc2.adress_data()
        run_tc2.declaration()
    elif(wybor == "4"):
        run_tc3 = TC_validate_form_adress()
        run_tc3.webdriver_choose()
        run_tc3.parcelWeight()
        run_tc3.inpost_select()
        run_tc3.deliveryType()
        run_tc3.adress_data()
    elif(wybor == "5"):
        respons_check(900, "test900.png")
        respons_check(1200, "test1200.png")
        respons_check(1800, "test1800.png")
        respons_check(600, "test600.png")
    else:
        print("zły wybór")
        main()


if __name__ == "__main__":
    main()