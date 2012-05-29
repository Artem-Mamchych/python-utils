#Author: Artem Mamchych
import sys
import subprocess
import os.path
import autohotkeyutils as ahk

description='main automation script for easy generating autohotkey menus'
version = 0.1 #all works!
usage = 'Usage: '
latest_version_url = ""

version_string = "%s version: %s  Latest version available at:\n %s" % (sys.argv[0], str(version), latest_version_url)
home_dir = os.getcwd()
options = None
log_file = None

warnings = list()
executed_commands = list()

def bindNumberKeys():
#hotKeyPasteText should be inited on the top of script
    ahk.hotKeyPasteText("0", "D:\Dropbox\dev\git\git-homeaway-nopass.ppk")
    ahk.hotKeyPasteText("1", "$('input[name=arrival-date]').val('07/01/2012'); $('input[name=departure-date]').val('07/02/2012'); $('input[name=first-name]').val('Artem'); $('input[name=last-name]').val('QHEditQuoteTest2');  $('input[name=email]').val('amamchych@homeaway.com'); $('input[name=phone-number]').val('111-111-1111 x11111'); $('#bookit-button').triggerHandler('click');")
    ahk.hotKeyPasteText("2", "$('#ccFirstName').val('Artem').removeClass('defInputValue'); $('#ccLastName').val('QHEditQuoteTest').removeClass('defInputValue');  $('#ccAddress').val('Baker Street 221B ').removeClass('defInputValue'); $('#state option:last').attr('selected', 'selected'); $('#ccCity').val('Huston').removeClass('defInputValue'); $('#ccCardNumber').val('4111111111111111').removeClass('defInputValue');  $('#agreement').attr('checked', true); $('#dateYear option:last').removeClass('defInputValue').attr('selected', 'selected'); $('#dateMonth option:last').removeClass('defInputValue').attr('selected', 'selected');  $('#ccZipcode').val('76019').removeClass('defInputValue'); $('#ccSecurityCode').removeClass('defInputValue').val('123').removeClass('defInputValue'); $('#submit-payment').triggerHandler('click');")
    ahk.hotKeyPasteText("3", "http://localhost:8088/haolb/")
    ahk.hotKeyPasteText("4", "http://localhost:8088/haolb/")

#    ahk.hotKeyPasteText("`", "http://localhost:8088/haolb/121.932994.3243366/bookit.htm")


    ahk.hotKeyPasteText("s", '$("#").val();')
    ahk.hotKeyPasteText("n", "$('input[name=]').val();")
    ahk.hotKeyPasteText("[", "amamchych@homeaway.com")
    ahk.hotKeyPasteText("]", "@4#1`%yNw*2")
    ahk.hotKeyPasteText("t", "clean test -Dsurefire.useFile=false -Dtest=")
    ahk.hotKeyPasteText("u", "mvn -U clean deploy -Dmaven.test.skip=true -DskipTests -Dshould.deploy.to.TEST=true")
    pass

def doGenerate():
    print("doGenerate STARTED")
#    Login accounts
#    ahk.addLoginAcc("Auth", "Test_testss_qa2", "testss_qa2@homeaway.com", "test456")

    ahk.addDefaultHALoginAcc("Auth", "amamchych@homeaway.com")
    ahk.addDefaultHALoginAcc("Auth", "testss_qa2@homeaway.com")
    ahk.addDefaultHALoginAcc("Auth", "avolk@homeaway.com")
    ahk.addDefaultHALoginAcc("Auth", "spalamarchuk@homeaway.com")
    ahk.addDefaultHALoginAcc("Auth", "testss_qa1@homeaway.com")
    ahk.addDefaultHALoginAcc("Auth", "test_ppi@homeaway.com")
    ahk.addDefaultHALoginAcc("Auth", "test_yapstone@homeaway.com")
    ahk.addMenuSeparator("Auth")
    ahk.addDefaultHALoginAcc("Auth", "ikrychun@homeaway.com")
    ahk.addDefaultHALoginAcc("Auth", "mhrytsylo@homeaway.com")

    ahk.addLinguaShortcut("LinguaBundle", "jsmessages", "en_US")
    ahk.addLinguaShortcut("LinguaBundle", "jsmessages", "en_GB")
    ahk.addLinguaShortcut("LinguaBundle", "jsmessages", "fr_FR")
    ahk.addMenuSeparator("LinguaBundle")
    ahk.addLinguaShortcut("LinguaBundle", "messages", "en_US")
    ahk.addLinguaShortcut("LinguaBundle", "messages", "en_GB")
    ahk.addLinguaShortcut("LinguaBundle", "messages", "fr_FR")

    ahk.addSiteBookmark("Bookmarks", "https://reaper.wvrgroup.internal/index.html?p=email")
    ahk.addSiteBookmark("Bookmarks", "https://reaper.wvrgroup.internal/index.html?p=request_templates")
    ahk.addSiteBookmark("Bookmarks", "https://reaper.wvrgroup.internal/index.html?p=inquiries")
    ahk.addSiteBookmark("Bookmarks", "https://reaper.wvrgroup.internal/index.html?p=haodash_dashboard")
    ahk.addSiteBookmark("Bookmarks", "https://reaper.wvrgroup.internal/index.html?p=travelerpayments")
    ahk.addSiteBookmark("Bookmarks", "https://reaper.wvrgroup.internal/index.html?p=owner_services")
    ahk.addSiteBookmark("Bookmarks", "https://reaper.wvrgroup.internal/index.html?p=quote-service")
    ahk.addSiteBookmark("Bookmarks", "http://hao-email-service-test-01.wvrgroup.internal:8080/logs/stdout.log")
    ahk.addSiteBookmark("Bookmarks", "http://hao-email-service-test-02.wvrgroup.internal:8080/logs/stdout.log")

    ahk.addTypeTextMenuItem("Bookmarks", "Hello_text!") #Todo escape , chars

    ahk.writeInvertMouseScrollWheelHandler()
    ahk.writeHandlers()
    ahk.assignMenuHotKey("a", "Auth")
    ahk.assignMenuHotKey("b", "Bookmarks")
    ahk.assignMenuHotKey("m", "LinguaBundle")

    bindNumberKeys()
    ahk.close()
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