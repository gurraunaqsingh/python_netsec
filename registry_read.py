#!/usr/bin/python

import _winreg

valName = "myKey"
try:
    with _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, "Software\\" + valName, 0, _winreg.KEY_READ) as key:
        if key:
            data = _winreg.QueryValueEx(key, "myVal")
            print(data)
except Exception as e:
    print(e)
