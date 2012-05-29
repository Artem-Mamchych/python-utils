import sys
import subprocess
import os.path
ahk_file = None
handlers = list()

def example():
    put2ahkscript("example")
    print("example")

tip1 = """
Menu, MyMenu2, Add, Test_testss_qa2, testss_qa2LoginMH
Menu, MyMenu2, Add, TEST_amamchych, amamchychLoginMH
Menu, MyMenu2, Add  ; Add a separator line.

testss_qa2LoginMH:
clipboard = $("input#username").val("testss_qa2@homeaway.com"); $("input#password").val("test456");  $("input#rememberMe").attr('checked', true); $('a#form-submit:first').trigger('click');
Send ^v
return

amamchychLoginMH:
clipboard = $("#username").val("amamchych@homeaway.com"); $("#password").val("test456");  $("#rememberMe").attr('checked', true); $('a#form-submit:first').trigger('click');
Send ^v
return

StringReplace, clipboard, clipboard, ABC, DEF, All ; ABC -> DEF

You can disable all built-in Windows hotkeys except Win+L and Win+U by making the following change to the registry (this should work on all OSes but a reboot is probably required):

HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer
NoWinKeys REG_DWORD 0x00000001 (1)

To disable or change an application's non-global hotkey (that is, a shortcut key that only works when that application is the active window), consider the following example which disables Control+P (Print) only for Notepad, leaving the key in effect for all other types of windows:
$^p::
IfWinActive ahk_class Notepad
    return  ; i.e. do nothing, which causes Control-P to do nothing in Notepad.
Send ^p
return

Add polkovniks phrases
    """
def createMenu(key, name):
    pass

def createMenuHandler(name, code):
    put2ahkscript("")
    put2ahkscript("")
    put2ahkscript("")
    put2ahkscript("")
    pass

add_features = """
http://www.autohotkey.com/docs/commands/Send.htm

Send Sincerely,{enter}John Smith  ; Types a two-line signature.
Send !fs ; Select the File->Save menu (Alt+F followed by S).
Send {End}+{Left 4} ; Jump to the end of the text then send four shift+left-arrow keystrokes.
"""

def addMenuSeparator(menuName):
    put2ahkscript("Menu, %s, Add" % menuName)

def addMenuItem(menuName, itemName, code):
    handler = itemName + 'Handler'
    put2ahkscript("Menu, %s, Add, %s, %s" % (menuName, itemName, handler))
    createMenuHandler(handler, code)

def addSiteBookmark(menuName, itemName):
    put2ahkscript("Menu, %s, Add, %s, OpenInBrowserMenuHandler" % (menuName, itemName))

def addSubMenu(menuName, subMenuName):
    print("Adding SubMenu: " + subMenuName)
    put2ahkscript("%s, MyMenu, Add, %s, :Submenu %s" % (menuName, subMenuName, subMenuName))
#    Menu, Submenu1, Add, https://reaper.wvrgroup.internal/index.html?p=email, OpenInBrowserMenuHandler

def addLinguaShortcut(menuName, bundleName, locale):
    print("Adding Lingua Shortcut %s:%s" % (bundleName, locale))
    itemName = "%s:%s" % (bundleName, locale)
    handler = 'LinguaHandler_%s_%s' % (bundleName, locale)
    put2ahkscript("Menu, %s, Add, %s, %s" % (menuName, itemName, handler))

    handlers.append(handler + ":")
    pasteTextHandler('$("input[name=category]").val("%s");$("#locale").val("%s");$("input[name=namespace]").val("haodash/uicore");$("input[name=version]").val("latest-writable");$("a.fetchBundle:first").trigger("click");' % (bundleName, locale))

def addDefaultHALoginAcc(menuName, username):
    print("Adding creds %s:%s" % (username, "test456"))
    itemName = username
    handler = itemName + 'Handler'
    put2ahkscript("Menu, %s, Add, %s, %s" % (menuName, itemName, handler))

    handlers.append(handler + ":")
    pasteTextHandler('$("#username").val("%s"); $("#password").val("%s");  $("#rememberMe").attr("checked", true); $("a#form-submit:first").trigger("click");' % (username, "test456"), pressEnter=True)

def addLoginAcc(menuName, itemName, username, password):
    print("Adding creds %s:%s" % (username, password))
    handler = itemName + 'Handler'
    put2ahkscript("Menu, %s, Add, %s, %s" % (menuName, itemName, handler))

    handlers.append(handler + ":")
    pasteTextHandler('$("#username").val("%s"); $("#password").val("%s");  $("#rememberMe").attr("checked", true); $("a#form-submit:first").trigger("click");' % (username, password))

def assignMenuHotKey(key, menuName):
    put2ahkscript("#%s::Menu, %s, Show  ; i.e. press the Win-%s hotkey to show the menu.\n" % (key, menuName, key))

def hotKey(key, ahkCode):
    pass
##m::
#Run Notepad
#return

def addTypeTextMenuItem(menuName, textToPrint):
    if not "," in textToPrint:
        put2ahkscript("Menu, %s, Add, %s, %s" % (menuName, textToPrint, "TypeTextMenuHandler"))
    else:
        print(textToPrint + " contains illegal characters!!!")

def hotKeyPasteText(key, clipboardText):
#    if len(clipboardText) >= 60:
    hotKeyClipboard(key, clipboardText) #It's faster
#    else:
#        print("Adding PasteText hotKey on Win+%s button" % key)
#        put2ahkscript("#%s::" % key)
#        put2ahkscript("SendInput "+ clipboardText)
#        put2ahkscript("return\n")

def hotKeyClipboard(key, clipboardText, saveClipboardContent=False):
    print("Adding Clipboard hotKey on Win+%s button" % key)
    put2ahkscript("#%s::" % key)
    if saveClipboardContent:
        clipboardSave()
    put2ahkscript("clipboard = %s" % clipboardText)
    put2ahkscript("Send ^v")
    if saveClipboardContent:
        clipboardRestore()
    put2ahkscript("return\n")

def writeCommonHandlers():
    put2ahkscript("OpenInBrowserMenuHandler:")
    put2ahkscript("Run %A_ThisMenuItem%")
    put2ahkscript("return\n")
    put2ahkscript("TypeTextMenuHandler:")
    put2ahkscript("SendInput %A_ThisMenuItem%")
    put2ahkscript("return\n")

def writeInvertMouseScrollWheelHandler():
    put2ahkscript("WheelUp::")
    put2ahkscript("Send {WheelDown}")
    put2ahkscript("Return")

    put2ahkscript("WheelDown::")
    put2ahkscript("Send {WheelUp}")
    put2ahkscript("Return")

def writeHandlers():
    writeCommonHandlers()
    for text in handlers:
        put2ahkscript(text)

def put2ahkscript(mesg):
    global ahk_file
    if not ahk_file:
        ahk_file = open("script.ahk", 'w')
        ahk_file.write("#SingleInstance force")
    ahk_file.write("\n" + str(mesg))

def close():
    ahk_file.close()

def clipboardSave():
    put2ahkscript("ClipSaved = %ClipboardAll%")

def clipboardRestore():
    put2ahkscript("clipboard = %ClipSaved%")

def pasteText(text, pressEnter=False):
    put2ahkscript("ClipSaved = %ClipboardAll%")
    put2ahkscript('clipboard = ' + text)
    put2ahkscript("ClipWait")
    put2ahkscript("Send ^v")
    put2ahkscript("clipboard = %ClipSaved%")
    put2ahkscript("return\n")

#Not uses clipboard; But has issue with not overridong win+key hotkeys
def printTextHandler(text, pressEnter=False):
    handlers.append("SendInput "+ text)
    if pressEnter:
        handlers.append("SendInput {enter}")
    handlers.append("return\n")

def pasteTextHandler(text, pressEnter=False):
    handlers.append("clipboard = %ClipSaved%")
    handlers.append('clipboard = ' + text)
    handlers.append("ClipWait")
    handlers.append("Send ^v")
    handlers.append("clipboard = %ClipSaved%")
    handlers.append("return\n")

#    #=Win ^=Ctrl +=Shift !=Alt
#    www.autohotkey.com/docs/commands/Send.htm
# Send {enter} - simulates human typing
#SendInput -  generally the preferred method to send keystrokes and mouse clicks because of its superior speed and reliability
#operating system limits SendInput to about 5000 characters