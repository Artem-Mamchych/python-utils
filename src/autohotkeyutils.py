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
    """

def createMenu(key, name):
    pass

def createMenuHandler(name, code):
    put2ahkscript("")
    put2ahkscript("")
    put2ahkscript("")
    put2ahkscript("")
    pass

def addMenuItem(menuName, itemName, code):
    handler = itemName + 'Handler'
    put2ahkscript("Menu, %s, Add, %s, %s" % (menuName, itemName, handler))
    createMenuHandler(handler, code)
#    Menu, MyMenu2, Add, TEST_amamchych, amamchychLoginMH
    pass

def addSiteBookmark(menuName, itemName):
    put2ahkscript("Menu, %s, Add, %s, OpenInBrowserMenuHandler" % (menuName, itemName))
#    Menu, Submenu1, Add, https://reaper.wvrgroup.internal/index.html?p=email, OpenInBrowserMenuHandler
    pass

def addLoginAcc(menuName, itemName, username, password):
    handler = itemName + 'Handler'
    put2ahkscript("Menu, %s, Add, %s, %s" % (menuName, itemName, handler))

    handlers.append(handler + ":")
    handlers.append('clipboard = $("#username").val("%s"); $("#password").val("%s");  $("#rememberMe").attr("checked", true); $("a#form-submit:first").trigger("click");' % (username, password))
    handlers.append("Send ^v")
    handlers.append("return\n")
    pass

def assignMenuHotKey(key, menuName):
    put2ahkscript("#%s::Menu, %s, Show  ; i.e. press the Win-%s hotkey to show the menu.\n" % (key, menuName, key))
    pass

def hotKey(key, ahkCode):
    pass

def hotKeyClipboard(key, clipboardText):
    put2ahkscript("#%s::" % key)
    put2ahkscript("clipboard = %s" % clipboardText)
    put2ahkscript("Send ^v")
    put2ahkscript("return\n")
    pass

def writeCommonHandlers():
    put2ahkscript("OpenInBrowserMenuHandler:")
    put2ahkscript("Run %A_ThisMenuItem%")
    put2ahkscript("return\n")

def writeHandlers():
    writeCommonHandlers()
    for text in handlers:
        put2ahkscript(text)

def put2ahkscript(mesg):
    global ahk_file
    if not ahk_file:
        ahk_file = open("script.ahk", 'w')
    ahk_file.write("\n" + str(mesg))