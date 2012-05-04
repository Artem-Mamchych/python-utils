"""
FEATURES::
diff tool:
gets diff beyond strings:
$("input#username").val("testss_qa1@homeaway.com"); $("input#password").val("test456");
$("input#username").val("amamchych@homeaway.com"); $("input#password").val("test456"); 
will return:
testss_qa1
and amamchych

menuObj = createMenu(key, name, )
menuObj.add(name)


API::
"""

description='main automation script for easy generating autohotkey menus'
version = 0.1 #all works!
usage = 'Usage: '
latest_version_url = ""

#Created on
#Author: Artem Mamchych
import sys
import subprocess
import os.path
import autohotkeyutils as ahk


version_string = "%s version: %s  Latest version available at:\n %s" % (sys.argv[0], str(version), latest_version_url)
home_dir = os.getcwd()
options = None
log_file = None

warnings = list()
executed_commands = list()

def doGenerate():
    print("doGenerate STARTED")
#    Login accounts
    ahk.addLoginAcc("Auth", "Test_testss_qa2", "testss_qa2@homeaway.com", "test456")
    ahk.addLoginAcc("Auth", "Test_amamchych", "amamchych@homeaway.com", "test456")
    ahk.addLoginAcc("Auth", "Test_spalamarchuk", "spalamarchuk@homeaway.com", "test456")
    ahk.addLoginAcc("Auth", "Test_testss_qa1", "testss_qa1@homeaway.com", "test456")
    ahk.addLoginAcc("Auth", "Test_ppi", "test_ppi@homeaway.com", "test456")
    ahk.addLoginAcc("Auth", "Test_yapstone", "test_yapstone@homeaway.com", "test456")
    ahk.addLoginAcc("Auth", "STAGE_ikrychun", "ikrychun@homeaway.com", "test456")
    ahk.addLoginAcc("Auth", "STAGE_mhrytsylo", "mhrytsylo@homeaway.com", "test456")

    ahk.addSiteBookmark("Bookmarks", "https://reaper.wvrgroup.internal/index.html?p=email")
    ahk.addSiteBookmark("Bookmarks", "https://reaper.wvrgroup.internal/index.html?p=request_templates")
    ahk.addSiteBookmark("Bookmarks", "https://reaper.wvrgroup.internal/index.html?p=inquiries")
    ahk.addSiteBookmark("Bookmarks", "https://reaper.wvrgroup.internal/index.html?p=haodash_dashboard")
    ahk.addSiteBookmark("Bookmarks", "https://reaper.wvrgroup.internal/index.html?p=travelerpayments")
    ahk.addSiteBookmark("Bookmarks", "https://reaper.wvrgroup.internal/index.html?p=owner_services")

    ahk.hotKeyClipboard("1", "$('input[name=first-name]').val('Artem'); $('input[name=last-name]').val('QHReservationTest1Z');  $('input[name=email]').val('amamchych@homeaway.com'); $('input[name=phone-number]').val('111-111-1111 x11111'); $('input[name=arrival-date]').val('04/27/2012'); $('input[name=departure-date]').val('04/28/2012'); $('#bookit-button').triggerHandler('click');")
    ahk.hotKeyClipboard("2", "$('#ccFirstName').val('Artem').removeClass('defInputValue'); $('#ccLastName').val('QHReservationTest2Z').removeClass('defInputValue');  $('#ccAddress').val('Capitalist hill').removeClass('defInputValue'); $('#state option:last').attr('selected', 'selected'); $('#ccCity').val('Huston').removeClass('defInputValue'); $('#ccCardNumber').val('4111111111111111').removeClass('defInputValue');  $('#agreement').attr('checked', true); $('#dateYear option:last').attr('selected', 'selected');  $('#ccZipcode').val('76019').removeClass('defInputValue'); $('#ccSecurityCode').val('123').removeClass('defInputValue'); $('#submit-payment').triggerHandler('click');")
    ahk.hotKeyClipboard("s", '$("#").val();')
    ahk.hotKeyClipboard("n", "$('input[name=]').val();")
    ahk.hotKeyClipboard("[", "amamchych@homeaway.com")
    ahk.hotKeyClipboard("]", "@4#1`%yNw*")
    ahk.writeHandlers()

    ahk.assignMenuHotKey("a", "Auth")
    ahk.assignMenuHotKey("b", "Bookmarks")
    print("DONE")
    pass

def call(cmd, log=True):
#    if log:
#        logExecutedCommand(cmd)
    if not options.echoMode:
        try:
            return subprocess.call(cmd, shell=True)
        except Exception:
            warning('[Error] executing command: ' + cmd)
            warning(str(sys.exc_info()[1]))

def callAndGetOutput(cmd, log=True):
#    if log:
#        logExecutedCommand(cmd)
    if options.echoMode:
        return ""

    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        (stdoutdata, stderrdata) = process.communicate()
        if stdoutdata:
            log2file("STDOUT: ")
            log2file(stdoutdata)
        if stderrdata:
            pass
#            logExecutedCommand("!!STDERR: " + str(stderrdata))
        if sys.version_info >= (3, 0):
            return str(stdoutdata, "utf-8") #converts binary string
        else:
            return str(stdoutdata)
    except Exception:
        warning('[Error] executing command: ' + cmd)
        warning(str(sys.exc_info()[1]))

def log(mesg):
    log2file('[DEBUG] ' + mesg)
    if options.debug_mode:
        print(mesg)

#All warning messages are cached and will be printed only on showWarnings() call
def warning(mesg):
    print('[WARN]>> ' + mesg)
    if mesg:
        log2file('[WARN] ' + mesg)
        warnings.append(mesg)

def log2file(mesg):
    global log_file
    if not log_file:
        log_file = open(os.path.join(home_dir, sys.argv[0] + '.log'), 'a')
    log_file.write("\n" + str(mesg))



def main():
    doGenerate()

if __name__ == "__main__":
    main()