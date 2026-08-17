from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

BASE='http://127.0.0.1:8000'

def make_driver(w,h):
    o=Options()
    o.add_argument('--headless=new')
    o.add_argument('--no-sandbox')
    o.add_argument('--disable-gpu')
    o.add_argument('--hide-scrollbars')
    o.add_argument('--force-device-scale-factor=1')
    o.add_argument(f'--window-size={w},{h}')
    d=webdriver.Chrome(options=o)
    d.set_window_size(w,h)
    return d

def capture(path, xpath, out, w, h, offset=-92):
    d=make_driver(w,h)
    try:
        d.get(BASE+path)
        WebDriverWait(d,10).until(lambda x: x.execute_script('return document.readyState')=='complete')
        d.execute_script("document.documentElement.style.scrollBehavior='auto';")
        el=WebDriverWait(d,10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        d.execute_script("arguments[0].scrollIntoView({block:'start',inline:'nearest'});",el)
        d.execute_script(f"window.scrollBy(0,{offset});")
        time.sleep(1.1)
        # Force reveal items visible for deterministic QA only.
        d.execute_script("document.querySelectorAll('.reveal').forEach(e=>e.classList.add('show','visible'))")
        time.sleep(.25)
        d.save_screenshot(out)
        print(out, d.execute_script('return [window.scrollX,window.scrollY,document.documentElement.scrollWidth,document.documentElement.scrollHeight]'))
    finally:
        d.quit()

capture('/', "//*[contains(normalize-space(.),'설명보다')][self::h2 or self::div][1]", 'qa2/home-impact-desktop.png', 1440,1200)
capture('/', "//h3[normalize-space()='Jobiverse']", 'qa2/home-projects-desktop.png', 1440,1200)
capture('/', "//*[contains(normalize-space(.),'설명보다')][self::h2 or self::div][1]", 'qa2/home-impact-mobile.png', 390,844, -72)
capture('/', "//h3[normalize-space()='Jobiverse']", 'qa2/home-projects-mobile.png', 390,844, -72)
capture('/projects/jobiverse.html', "//*[contains(normalize-space(.),'결과는 느낌이 아니라')][self::h2 or self::div][1]", 'qa2/jobiverse-results-desktop.png', 1440,1200)
capture('/projects/jobiverse.html', "//*[contains(normalize-space(.),'결과는 느낌이 아니라')][self::h2 or self::div][1]", 'qa2/jobiverse-results-mobile.png', 390,844, -72)
capture('/projects/jobiverse.html', "//*[contains(normalize-space(.),'직무 정보는 많지만')][self::h2 or self::div][1]", 'qa2/jobiverse-problem-desktop.png', 1440,1200)
