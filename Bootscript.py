#grabbed this from a book on python for cybersecurity, lots of great stuff, will add to this to create more functionality. 
import winreg

reghive = winreg.HKEY_USERS
userSID = "<userSID>"
regpath = userSID+"\Environment"
# add registry logon script
key = winreg.OpenKey(reghive, regpath, 0,access=winreg.KEY_WRITE)
winreg.SetValueEx(key,"UserInitMprLogonScript",0,winreg.REG_SZ,command)
