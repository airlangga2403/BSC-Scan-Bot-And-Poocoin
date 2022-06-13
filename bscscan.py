from datetime import datetime
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException


def is_number_tryexcept(s):   
    try:
        float(s)
        return True
    except ValueError:
        return False

def split_word(word):
    return [char for char in word]


def check_bsc():
    x = 0
    y = 5 # start from 5
    while True:
        # Links
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        web = webdriver.Chrome(options=options)  
        web.set_window_position(-10000,0)


        web.minimize_window()
        web.implicitly_wait(5)       
        check_address = open('C:/Coding/PYTHON/Selenium Test/random_website/list/check_address.txt','r')
        for i, line in enumerate(check_address):
            if i == x:
                web.get('https://bscscan.com/address/{}'.format(line))
                with open('C:/Coding/PYTHON/Selenium Test/random_website/checked_address/bsc.txt','a') as f:
                    f.write('[')
                    f.write('\n')
                    f.write("Address : ")
                    a = line.strip('\n')
                    f.write(a)
                    f.write('\n')
                    dateTimeObj = datetime.now()
                    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S)")
                    f.write("Date : " + str(timestampStr) + " GMT +7")
                    f.write('\n')
                    f.write('\n')
                    f.write("-------------------")
                    f.close()                    
                continue
        time.sleep(1)       
        get_token = web.find_elements_by_xpath("//span[contains(@class,'list-name hash-tag text-truncate')]")
        get_token_value = web.find_elements_by_xpath("//span[contains(@class,'list-amount link-hover__item hash-tag hash-tag--md text-truncate')]")
        get_href = web.find_elements_by_xpath("//a[contains(@class,'link-hover d-flex justify-content-between align-items-center')]")
        count = 0
        token = []
        token_value = []
        links = []
        token_price = []
        for elem in get_token:
            print_token = elem.get_attribute('innerText')
            token.append(print_token)
        
        for j in get_token_value:
            print_value_token = j.get_attribute('innerText')
            string = print_value_token.replace("," , "")
            stringz = string.split()
            for i in range(len(stringz)):
                if is_number_tryexcept(stringz[i]):
                    temp = stringz[i]
                    token_value.append(temp)
            count +=1

        for link in get_href:
            print_get_href = link.get_attribute('href')
            splitz  = split_word(str(print_get_href))
            strt = 26
            end = 68
            res = ''.join([sub for sub in splitz])[strt : end]
            links.append(res)
        # // POOCOIN
        assets = []
        for a in range(len(links)):
            web_url = links[a]
            web.get('https://poocoin.app/tokens/{}'.format(web_url))
            time.sleep(1)
            try:
                get_price_token = web.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]")
                price = get_price_token.get_attribute('innerText')
                string = price.replace("$","").replace(",","")
                token_price.append(string)
            except NoSuchElementException:
                token_price.append(0)
            # Hitung Assets
            tok_value = float(token_value[a])
            tok_price = float(token_price[a])
            total = tok_value*tok_price
            assets.append(total)
        # hitung All Assets
        all_assets = sum(assets)
        for k in range (len(token)):
            with open('C:/Coding/PYTHON/Selenium Test/random_website/checked_address/bsc.txt','a') as f:
                    f.write('\n')
                    f.write('- ')
                    f.write(token[k])
                    f.write(" | Value : ")
                    f.write(str(token_value[k]))
                    f.write(" | Price : ")
                    f.write(str(token_price[k]))
                    f.write(" | Total Price : $" + str(assets[k]))
                    f.write(" | Contract Adress : ")
                    f.write(links[k])
                    f.close()     
        with open('C:/Coding/PYTHON/Selenium Test/random_website/checked_address/bsc.txt','a') as f:
            f.write('\n')
            f.write("-------------------")
            f.write('\n')
            f.write('Total Token : ')
            f.write(str(count))
            f.write('\n')
            f.write('Total Assets : $')
            f.write(str(all_assets))
            f.write('\n')
            f.write(']')
            f.close()
        time.sleep(2)
        x = x+1
        y = y+1
        print("Run Ke  : {no}" .format(no = x))
        web.close()

def check_polygon():
    x = 0
    y = 5 # start from 5
    while True:
        # Links
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        web = webdriver.Chrome(options=options)  
        web.set_window_position(-10000,0)


        web.minimize_window()
        web.implicitly_wait(5)       
        check_address = open('C:/Coding/PYTHON/Selenium Test/random_website/list/check_address.txt','r')
        for i, line in enumerate(check_address):
            if i == x:
                web.get('https://polygonscan.com/address/{}'.format(line))
                with open('C:/Coding/PYTHON/Selenium Test/random_website/checked_address/polygon.txt','a') as f:
                    f.write('[')
                    f.write('\n')
                    f.write("Address : ")
                    a = line.strip('\n')
                    f.write(a)
                    f.write('\n')
                    dateTimeObj = datetime.now()
                    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S)")
                    f.write("Date : " + str(timestampStr) + " GMT +7")
                    f.write('\n')
                    f.write('\n')
                    f.write("-------------------")
                    f.close()                    
                continue
        time.sleep(1)       
        get_token = web.find_elements_by_xpath("//span[contains(@class,'list-name hash-tag text-truncate')]")
        get_token_value = web.find_elements_by_xpath("//span[contains(@class,'list-amount link-hover__item hash-tag hash-tag--md text-truncate')]")
        get_href = web.find_elements_by_xpath("//a[contains(@class,'link-hover d-flex justify-content-between align-items-center')]")
        get_value_price = web.find_elements_by_xpath("//span[contains(@class,'list-usd-value d-block')]")
        count = 0
        token = []
        token_value = []
        value_price = []
        links = []
        for elem in get_token:
            print_token = elem.get_attribute('innerText')
            token.append(print_token)
        
        for j in get_token_value:
            print_value_token = j.get_attribute('innerText')
            string = print_value_token.replace("," , "")
            stringz = string.split()
            for i in range(len(stringz)):
                if is_number_tryexcept(stringz[i]):
                    temp = stringz[i]
                    token_value.append(temp)
            count +=1

        for elem in get_value_price:
            print_value_price = elem.get_attribute('innerText')
            value_price.append(print_value_price)

        for link in get_href:
            print_get_href = link.get_attribute('href')
            splitz  = split_word(str(print_get_href))
            strt = 26
            end = 68
            res = ''.join([sub for sub in splitz])[strt : end]
            links.append(res)

        for k in range (len(token)):
            with open('C:/Coding/PYTHON/Selenium Test/random_website/checked_address/polygon.txt','a') as f:
                    f.write('\n')
                    f.write('- ')
                    f.write(token[k])
                    f.write(" | Value : ")
                    f.write(str(token_value[k]))
                    f.write(" | Token Value Price : ")
                    if k < len(value_price):
                        f.write(str(value_price[k]))
                    f.write(" | Contract Adress : ")
                    f.write(links[k])
                    f.close()     
        with open('C:/Coding/PYTHON/Selenium Test/random_website/checked_address/polygon.txt','a') as f:
            f.write('\n')
            f.write("-------------------")
            f.write('\n')
            f.write('Total Token : ')
            f.write(str(count))
            f.write('\n')
            f.write(']')
            f.close()
        time.sleep(2)
        x = x+1
        y = y+1
        print("Run Ke  : {no}" .format(no = x))
        web.close()

def main():
    while(True):
        check_bsc()
        # check_polygon()

if __name__ == "__main__":
    main()

