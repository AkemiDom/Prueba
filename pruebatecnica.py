import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Edge('msedgedriver.exe')

browser.get('https://www.amazon.com/ap/signin?ie=UTF8&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&language=es&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&switch_account=signin&ignoreAuthState=1&disableLoginPrepopulate=1&ref_=ap_sw_aa')
#iniciar sesion
elem = browser.find_elements(By.CSS_SELECTOR, 'input#ap_email'); elem[0].send_keys('angietejeda1217@gmail.com'); time.sleep(1)

elem = browser.find_elements(By.CSS_SELECTOR, 'input#continue'); elem[0].click(); time.sleep(1)

elem = browser.find_elements(By.CSS_SELECTOR, 'input#ap_password'); elem[0].send_keys('Aura1712.'); time.sleep(1)

elem = browser.find_elements(By.CSS_SELECTOR, 'input#signInSubmit'); elem[0].click(); time.sleep(1)
#cuenta
elem = browser.find_elements(By.CSS_SELECTOR, '#nav-link-accountList > span'); elem[0].click(); time.sleep(0.5)

elem = browser.find_elements(By.CSS_SELECTOR, '#a-page > div.a-container > div > div:nth-child(2) > div:nth-child(2) > a'); elem[0].click()
time.sleep(1)
#editar nombre
elem = browser.find_elements(By.CSS_SELECTOR, 'input#auth-cnep-edit-name-button'); elem[0].click(); time.sleep(1)

elem = browser.find_elements(By.CSS_SELECTOR, 'input#ap_customer_name'); elem[0].clear(); elem[0].send_keys('Angie Tejeda'); time.sleep(1)

elem = browser.find_elements(By.CSS_SELECTOR, 'input#cnep_1C_submit_button'); elem[0].click(); time.sleep(1)

elem = browser.find_elements(By.CSS_SELECTOR, '#breadcrumb_CNEP > li:nth-child(1) > span > a'); elem[0].click(); time.sleep(1)
#agregar direccion
elem = browser.find_elements(By.CSS_SELECTOR, '#a-page > div.a-container > div > div:nth-child(8) > div:nth-child(1) > div > div > ul > li:nth-child(1) > span > a'); elem[0].click(); time.sleep(1)

elem = browser.find_elements(By.CSS_SELECTOR, '#ya-myab-address-add-link > div > div'); elem[0].click(); time.sleep(1)

elem = browser.find_elements(By.CSS_SELECTOR, '#address-ui-widgets-enterAddressPhoneNumber'); elem[0].send_keys('8498758429'); time.sleep(1)

elem = browser.find_elements(By.CSS_SELECTOR, 'input#address-ui-widgets-enterAddressLine1'); elem[0].send_keys('4624 NW 74th Ave.'); time.sleep(1)

elem = browser.find_elements(By.CSS_SELECTOR, '#awz-address-suggestion-0'); elem[0].click(); time.sleep(1)

elem = browser.find_elements(By.CSS_SELECTOR, '#address-ui-widgets-form-submit-button > span > input'); elem[0].click(); time.sleep(1)
#buscar 
elem = browser.find_elements(By.CSS_SELECTOR, '#twotabsearchtextbox'); elem[0].send_keys('iPhone 13 Pro Max Color Plateado de 512GB'); time.sleep(1); elem[0].send_keys(Keys.ENTER)

elem = browser.find_elements(By.CSS_SELECTOR, '#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.sg-row > div.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span:nth-child(4) > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(4) > div > div > div > div > div > div > div > div.sg-col.sg-col-4-of-12.sg-col-8-of-16.sg-col-12-of-20.s-list-col-right > div > div > div.a-section.a-spacing-none.puis-padding-right-small.s-title-instructions-style > h2 > a > span'); elem[0].click(); time.sleep(3)
#agregar al carrito
elem = browser.find_elements(By.CSS_SELECTOR, '#a-autoid-28-announce > div > div'); elem[0].click(); time.sleep(2)

elem = browser.find_elements(By.CSS_SELECTOR, '#add-to-cart-form > div > span.a-button.a-button-normal.a-spacing-small.a-button-primary.a-button-icon.qa-atc-button > span > input'); elem[0].click(); time.sleep(1)

elem = browser.find_elements(By.CSS_SELECTOR, '#root > div > div > div > div.feature_SideSheet.celwidget > div > div.ss-right-enter-done > div > div.a-section > div:nth-child(2) > div.a-column.a-span4.a-span-last > div > div > div > span > span.a-button.qa-warranty-no-thanks-button > span > button');elem[0].click();time.sleep(3)

elem = browser.find_elements(By.CSS_SELECTOR, '#root > div > div > div > div.feature_SideSheet.celwidget > div > div.ss-right-enter-done > div > div > div.a-section.a-spacing-none.a-padding-base.hucStatus > div > div > div.a-fixed-left-grid-col.a-col-right > div.a-row.a-spacing-top-small.sidesheetCartButtonStack > span'); elem[0].click(); time.sleep(1)

os.system("pause")