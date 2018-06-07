import sys
import threading
import time
import psutil
import webbrowser
import pyautogui
import pywinauto

SECONDS_BEFORE_KILL = 30

def get_procs(browser):
    procs = []
    for proc in psutil.process_iter():
        try:
            procs.append(proc.as_dict(attrs=['pid', 'name']))
        except:
            pass
            
    return [proc['pid'] for proc in procs if proc['name'] == browser]
    
def get_browser_window(browser):
    print("Finding default browser process...")
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

def kill_tab(app):
    app.set_focus()
    pyautogui.hotkey('ctrl', 'w')
    
def unleash_chaos_cli():
    if args.web_browser not in ['chrome', 'firefox', 'MicrosoftEdge']:
            raise Exception(args.web_browser + " is not a browser. Select among 'chrome', 'firefox', 'MicrosoftEdge'.")
            
    webbrowser.open('https://news.ycombinator.com/')
    web_browser += '.exe'
    browser_window = get_browser_window(web_browser)

    while num_opened != npages:
        webbrowser.open(url)
        num_opened += 1
        num_refreshes -= 1

        if num_opened > 1:
            t = threading.Timer(SECONDS_BEFORE_KILL, lambda: kill_tab(browser_window)).start()
        
        seconds = 0
        while seconds < num_seconds and num_opened != npages:
            status = 'Opened: {0}/{1} | Seconds left: {2:3d}\r'.format(num_opened, npages, (num_seconds - seconds))
            sys.stdout.write(status)
            sys.stdout.flush()        
            time.sleep(1)
            seconds += 1
            
def unleash_chaos_gui(browser, url, refreshes, interval):
    webbrowser.open(url)
    browser += '.exe'
    browser_window = get_browser_window(browser)
    num_opened = 0
    num_seconds = interval*60

    while num_opened != refreshes:
        webbrowser.open(url)
        num_opened += 1
        refreshes -= 1

        if num_opened > 1:
            t = threading.Timer(SECONDS_BEFORE_KILL, lambda: kill_tab(browser_window)).start()
        
        seconds = 0
        while seconds < num_seconds and num_opened != refreshes:
            status = 'Opened: {0}/{1} | Seconds left: {2:3d}\r'.format(num_opened, refreshes, (num_seconds - seconds))
            sys.stdout.write(status)
            sys.stdout.flush()        
            time.sleep(1)
            seconds += 1
