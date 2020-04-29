#-*-coding:utf-8 -*-
import os
if os.name=='posix':q='pip3'
else:q='pip'
bibl=['telnetlib','selenium','datetime','time','subprocess','socket','tftpy','templates','threading','platform','shutil']
for i in bibl:
	print(q+' install '+i)
	print(os.system(q+' install '+i+' --user'))
	


###Основной скрипт
def st(I,th1,tr):
    profile = FirefoxProfile()
    profile.set_preference("browser.download.folderList",2)
    profile.set_preference("browser.download.manager.showWhenStarting",False)
    profile.set_preference("browser.download.dir", tr)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk",'application/octet-stream')

    driver = webdriver.Firefox(firefox_profile=profile)

    popo=datetime.today().minute + datetime.today().hour*60 + datetime.today().day*24*60

    time.sleep(2)
    I=I.split('\n')
    IPall=[]
    for i in I:
        try:
            if i[-1]=='\r':
                IPall.append(i[:-1])
            else:IPall.append(i)
        except:pass
    TFTPIP=socket.gethostbyname(socket.gethostname())
    passandlog=[]
    time.sleep(2)
    log='admin'.encode('utf-8')
    passs=['POs802ml;s','polpol','pol','POs802ml']
    passandlog=[[log,j.encode('utf-8')] for j in passs]  
    command1='upload cfg_toTFTP %s dest_file dest_file' % TFTPIP
    command2='upload cfg_toTFTP %s dest_file' % TFTPIP
    command3='upload cfg_toTFTP tftp://%s/dest_file' % TFTPIP
    command4='upload cfg_toTFTP %s dest_file config_id 1' % TFTPIP
    command=[command1.encode('utf-8'),command2.encode('utf-8'),command3.encode('utf-8'),command4.encode('utf-8')]
    da=[]
    notconnect=[]
    nopass=[]
    downerror=[]
    connError=[]
    for IP in IPall:
        print("#"*100)
        if ping(IP):
            try:
                for i in passandlog:
                    with Telnet(IP,timeout=4) as tn:
                        print("CONNECT %s SWITCH" % IP) 
                        idint=logi(passandlog,tn,i)
                        if idint: 
                            print("LOGIN + AND PASS +")
                            namedate=tr+"\\%s-%s" % (IP,str(datetime.today().day)+'.'+str(datetime.today().month)+'.'+str(datetime.today().year))
                            if download(command,tn,tr,namedate):
                                da.append(IP)
                            else:downerror.append(IP)
                            break
                if idint==False:
                    print("NOT PASS")
                    nopass.append(IP)
            except:
                try:
                    driver.get('http://'+IP+'/')
                    for i in passandlog:
                        pa=passweb(i,driver)
                        if len(pa)!=0:
                            driver.switch_to_default_content()
                            time.sleep(3)
                            driver.switch_to_frame(1)
                            driver.find_element_by_css_selector(pa[0]).click()
                            time.sleep(1)
                            driver.switch_to_default_content()
                            time.sleep(3)
                            driver.switch_to_frame(2)
                            driver.find_element_by_css_selector(pa[1]).click()
                            time.sleep(3)
                            try:
                                alert = driver.switch_to_alert()
                                time.sleep(2)
                                alert.accept()
                                time.sleep(3)
                            except:pass
                            break
                    try:
                        namedate=tr+"\\%s-%s" % (IP,str(datetime.today().day)+'.'+str(datetime.today().month)+'.'+str(datetime.today().year))
                        os.rename(tr+'\\config.bin',namedate)
                        print("FIRE RENAME")
                        da.append(IP)
                    except:print("RENAME ERROR")
                except:
                    connError.append(IP)
                    print("CONNECT ERROR ■■■■■■■■■■■■")
        else:
            print("NOT CONNECT")
            notconnect.append(IP)

    driver.close()
    popo=(datetime.today().minute + datetime.today().hour*60 + datetime.today().day*24*60)-popo
    print("Spend %s minutes" % popo)
    fff='#'*50
    with open(tr+'\\NET.txt','w') as q:
        q.writelines('ADD:' + fff + '\n')
        for i in da:
            q.writelines(i+'\n')
        q.writelines('NOT ONLINE:' + fff + '\n')
        for i in notconnect:
            q.writelines(i+'\n')
        q.writelines('NOT PASS:' + fff + '\n')
        for i in nopass:
            q.writelines(i+'\n')
        q.writelines('DOWLOAD NERROR:' + fff + '\n')
        for i in downerror:
            q.writelines(i+'\n')
        q.writelines('TELNET CONNERROR:' + fff + '\n')
        for i in connError:
            q.writelines(i+'\n')
    th1.join()

def passweb(i,driver):
    driver.switch_to_default_content()
    try:
        driver.switch_to_frame(0)
        driver.find_element_by_css_selector('#pass').click()
        driver.find_element_by_css_selector('#pass').send_keys(i[1].decode('utf-8'))
        time.sleep(2)
        driver.find_element_by_css_selector('input.btnText:nth-child(1)').click()
        time.sleep(2)
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(0)
        try:
            driver.find_element_by_css_selector('#tabTool > tbody > tr > td').click()
            return ['#tag1 > tbody > tr:nth-child(4) > td','#c1']
        except: 
            driver.find_element_by_css_selector('#tabLoginContent > tbody > tr:nth-child(3) > td:nth-child(3) > input').click()
            return []
    except:
        driver.find_element_by_css_selector('#passwd').click()
        driver.find_element_by_css_selector('#passwd').send_keys(i[1].decode('utf-8'))
        driver.find_element_by_css_selector('input.btnText:nth-child(1)').click()

        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        try:
            driver.switch_to_frame(2)
            driver.find_element_by_css_selector('#tabApplyContent > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > input:nth-child(1)').click()
            time.sleep(10)
            driver.switch_to_default_content()
            driver.switch_to_frame(0)
            driver.find_element_by_css_selector('#tabTool > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > font:nth-child(1)').click()
            return ['#tag1 > tbody:nth-child(1) > tr:nth-child(2)','#tabResetContent > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > input:nth-child(1)']
        except:
            driver.switch_to_default_content()
            driver.find_element_by_css_selector('.btnText').click()
            return []


###Скачивание файлов с коммутатора
def download(command,tn,tr,namedate):
    try:
        for i in command:
            tn.write(i+b'\n')
            time.sleep(1.5)
            tn.read_very_eager()
        print("FILE DOWNLOAD")
        try:
            time.sleep(1)
            os.rename(tr+'\\dest_file',namedate)
            time.sleep(0.5)
            print("FILE RENAME")
            return True
        except:
            print("RENAME ERROR")
            return False
    except:
        print("DOWNLOAD ERROR")    
        return False


###Авторизаация в коммутаторе
def logi(passandlog,tn,i):
    time.sleep(1.5)
    text=tn.read_very_eager()
    for j in range(2):
        if 'UserName' in text.decode('utf-8') or 'login' in text.decode('utf-8'):
            tn.write(i[0]+b'\n')
            time.sleep(1.5)
            tn.read_very_eager()
            time.sleep(0.5)
            tn.write(i[1]+b'\n')
            time.sleep(1.5)
            text=tn.read_very_eager()
            time.sleep(0.5)
            if 'UserName' not in text.decode('utf-8') and 'login' not in text.decode('utf-8'):return True
        else:
            tn.write(i[1]+b'\n')
            time.sleep(1.5)
            text=tn.read_very_eager()
            if 'Password' not in text.decode('utf-8'):return True
    return False

###Проверка наличия коммутатора в сети
def ping(IP):
    com="ping -n 3 -w 100 %s" % IP
    a=subprocess.Popen(com)
    if a.wait()==0:return True
    else: return False

###Включние TFTP сервера
def TFTPser(*args):
    File=''
    for i in args:
        File+=i
    server = tftpy.TftpServer(tftproot=File)
    print("START TFTP SERVER")
    try:server.listen(socket.gethostbyname(socket.gethostname()), 69)
    except:server.listen(socket.gethostbyname(socket.gethostname()), 69)
    


def start():
    try:
        driver=webdriver.Firefox()
        driver.close()
    except:
        W=input('Введите адрес интерпритатора python--> ')
    Q=input('Адрес файла с IP адресами коммутаторов--> ')
    fileadd=input('Адрес папки для сохранения конфигурационных файлов--> ')
    I=''
    if '64' in platform.architecture()[0] and "Win" in platform.architecture()[1]:shutil.copyfile(r'geckto\w64\geckodriver.exe',W+'\\geckodriver.exe')
    if '32' in platform.architecture()[0] and "Win" in platform.architecture()[1]:shutil.copyfile(r'geckto\w32\geckodriver.exe',W+'\\geckodriver.exe')
    if '64' in platform.architecture()[0] and "Lin" in platform.architecture()[1]:shutil.copyfile(r'geckto\l64\geckodriver',W+'\\geckodriver')
    if '32' in platform.architecture()[0] and "Lin" in platform.architecture()[1]:shutil.copyfile(r'geckto\l32\geckodriver',W+'\\geckodriver')
    if Q!='' and os.path.exists(Q):
        try:
            with open(Q,'r') as q:
                for i in q:
                    I+=i
            print("FILE OPEN")
        except:print("ERROR")
        th1=Thread(target=TFTPser,args=fileadd)
        th2=Thread(target=st,args=(I,th1,fileadd))
        th1.start()
        th2.start()
    else:print("FILE NOT EXIST")

if __name__ == "__main__":
    start()
