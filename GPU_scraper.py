from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from twilio.rest import Client

WINDOW_SIZE = "1920, 1080"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

# THESE ARE YOUR TWILIO CREDS
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token = ""

client = Client(account_sid, auth_token)
message = client.messages.create

print("Starting the search")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324")

title = driver.title
print(title)

def twilio_text_XboxXinstock():
    message(to="PHONE", from_="TWILIO_PHONENUMBER", body="Xbox X IN STOCK! https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324")

el = driver.find_element_by_tag_name('body')
str = el.text
if(str.find("Add to Cart") != -1):
    twilio_text_XboxXinstock()

print('Finished looking for xbox at Best Buy')

# Looking for PS5 at Best Buy
driver.get("https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149")
print(driver.title)
# Best Buy PS5 Function
def twilio_text_PS5instock():
    message(to="PHONE", from_="TWILIO_PHONENUMBER",, body="PS5 IN STOCK! https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149")

el = driver.find_element_by_tag_name('body')
str = el.text
if(str.find("Add to Cart") != -1):
    twilio_text_PS5instock()

print('finished looking for PS5 at Best Buy')

# PS5 on AMAZON checker
driver.get("https://www.amazon.com/PlayStation-5-Digital/dp/B08FC6MR62?ref_=ast_sto_dp")
print(driver.title)

def twilio_text_PS5amazon():
    message(to="PHONE", from_="TWILIO_PHONENUMBER",, body="https://www.amazon.com/PlayStation-5-Digital/dp/B08FC6MR62?ref_=ast_sto_dp")

el = driver.find_element_by_tag_name('body')
str = el.text
if(str.find("Add to Cart") != -1):
    twilio_text_PS5amazon()

print('Finished looking for PS5 on amazon')

# 3080ti search at Best Buy
driver.get("https://www.bestbuy.com/site/evga-nvidia-geforce-rtx-3080-ti-ftw3-ultra-gaming-12gb-gddr6x-pci-express-4-0-graphics-card/6467808.p?skuId=6467808")
print(driver.title)

def twilio_text_3080tibestbuy():
    message(to="PHONE", from_="TWILIO_PHONENUMBER",, body=" 3080 ti at Best Buy!! https://www.bestbuy.com/site/evga-nvidia-geforce-rtx-3080-ti-ftw3-ultra-gaming-12gb-gddr6x-pci-express-4-0-graphics-card/6467808.p?skuId=6467808")

el = driver.find_element_by_tag_name('body')
str = el.text
if(str.find("Add to Cart") != -1):
    twilio_text_3080tibestbuy()

print('Finished looking for 3080 ti at best buy')

# 3090 checking best buy
driver.get("https://www.bestbuy.com/site/evga-geforce-rtx-3090-xc3-ultra-gaming-24gb-gddr6-pci-express-4-0-graphics-card/6434198.p?skuId=6434198")
print(driver.title)

def twilio_text_3090bestbuy():
    message(to="PHONE", from_="TWILIO_PHONENUMBER",, body="https://www.bestbuy.com/site/evga-geforce-rtx-3090-xc3-ultra-gaming-24gb-gddr6-pci-express-4-0-graphics-card/6434198.p?skuId=6434198")

el = driver.find_element_by_tag_name('body')
str = el.text
if(str.find("Add to Cart") != -1):
    twilio_text_3090bestbuy()

driver.close()
print('Finished looking for 3090 at best buy')

# PS5 on GAMESTOP checker
driver = webdriver.Chrome()
driver.get("https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5-digital-edition/11108141.html?condition=New")
print(driver.title)

def twilio_text_PS5gamestop_digital():
    message(to="PHONE", from_="TWILIO_PHONENUMBER",, body="PS5 available at Gamestop! https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5-digital-edition/11108141.html?condition=New")

el = driver.find_element_by_tag_name('body')
str = el.text
if(str.find("ADD TO CART") != -1):
    twilio_text_PS5gamestop_digital()

print('Finished looking for PS5 digital on GAMESTOP')

# PS5 on GAMESTOP checker
driver.get("https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5/11108140.html?condition=New")
print(driver.title)

def twilio_text_PS5gamestop():
    message(to="PHONE", from_="TWILIO_PHONENUMBER",, body=" PS5 available at Gamestop! https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5/11108140.html?condition=New")

el = driver.find_element_by_tag_name('body')
str = el.text
if(str.find("ADD TO CART") != -1):
    twilio_text_PS5gamestop()

driver.close()
print('Finished looking for PS5 on GAMESTOP')

print('SEARCH COMPLETE')
