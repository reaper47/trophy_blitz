import sys
import threading
import time
import psutil
import webbrowser
import pyautogui
import pywinauto

SECONDS_BEFORE_KILL = 30
            
def unleash_chaos(browser, url, refreshes, interval, lcd, refreshes_left):
    refreshes_left.setText('Initializing the blitz...')
    thread = threading.currentThread()
    thread_time = None

    webbrowser.open(url)
    browser += '.exe'
    browser_window = get_browser_window(browser.lower())
    num_opened = 0
    num_seconds = interval*60
    total_num_pages = refreshes

    while num_opened < total_num_pages and getattr(thread, 'do_run', True):
        webbrowser.open(url)
        num_opened += 1
        refreshes -= 1
        refreshes_left.setText('Opened {0}/{1} pages.'.format(num_opened, total_num_pages))

        if num_opened > 1 and num_opened != total_num_pages:
            thread_time = threading.Timer(SECONDS_BEFORE_KILL, lambda: kill_tab(browser_window))
            thread_time.start()

        if num_opened == total_num_pages:
            thread_time.join()
            thread_time = None
            refreshes_left.setText('Blitz completed. Please abort.')
            break
        
        seconds = 0
        while seconds < num_seconds and num_opened != refreshes and getattr(thread, 'do_run', True):     
            time.sleep(1)
            seconds += 1
            lcd.setProperty("value", num_seconds - seconds)

    if thread_time != None:
        thread_time.join()

def get_browser_window(browser):
    app = pywinauto.application.Application() 
    procs = get_procs(browser)
    app_window = None
    
    for proc in procs:
        try:
            app.connect(process=int(proc))
            app_window = app.top_window_()
            break
        except:
            pass
            
    return app_window

def get_procs(browser):
    procs = []
    for proc in psutil.process_iter():
        try:
            procs.append(proc.as_dict(attrs=['pid', 'name']))
        except:
            pass
            
    return [proc['pid'] for proc in procs if proc['name'] == browser]

def kill_tab(app):
    app.set_focus()
    pyautogui.hotkey('ctrl', 'w')
