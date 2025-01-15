from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
chromium = playwright.chromium
browser = chromium.launch(headless=False, slow_mo=100)#headless=True = running without opening the browser
page = browser.new_page()
page.goto("https://demo.opencart.com/admin/")

page.fill('#input-username','demo')
page.fill('#input-password','demo')
trials = 1
while trials !=0:
    try:
        print(trials)
        page.click('#form-login > div.text-end > button', timeout=1000)
        orders = page.text_content('#content > div.container-fluid > div:nth-child(1) > div:nth-child(1) > div > div.tile-body > h2', timeout=5000)
        trials =0
    except:
        trials +=1
print("orders:",orders)
browser.close()
