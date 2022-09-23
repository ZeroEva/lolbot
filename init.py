from pywinauto.application import Application
from pywinauto.win32functions import SetFocus
from pywinauto import mouse, keyboard
import win32gui


def find_window(name):
    main_handle = win32gui.FindWindow(name, None)
    print(main_handle)
    window = Application().connect(handle=main_handle)
    window.top_window().set_focus()
    print(window.top_window().wrapper_object())

    mouse.click()
    keyboard.send_keys(
        "{ENTER}"
        "{VK_SHIFT down}"
        "pywinauto"
        "{VK_SHIFT up}"
        "{ENTER}"
    )



if __name__ == '__main__':
    find_window('Chrome_WidgetWin_1')
    # print("--------------------")
    # find_window('SunAwtFrame')
