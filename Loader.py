#This is the loader.

import FormWritter
import configparser


try:
    f = open('config.ini')
    f.close()
except:
    print("exist no valid config, rebuilding one")
    config=configparser.ConfigParser()
    config['DEFAULT'] = {'continueExecution': '0',
                         'defaultuid': '601',
                         'defaultstage': '0',
                         'activeUIDAsk': '1',
                         'activeStageAsk': '1',
                         'withimage': '0',
                         'UIDSaveFileName': '0',
                         'DefaultOutputFileName':'out.txt'
                         }
    config['IMAGE'] = {'doRed'  : '[img=https://i.imgur.com/HagkEhI.png]',
                       'doFloat': '[img=https://i.imgur.com/XmW79pT.png]',
                       'doBlack': '[img=https://i.imgur.com/zUqTa3f.png]',
                       'doIron' : '[img=https://i.imgur.com/mAabf1v.png]',
                       'doWhite': '[img=https://i.imgur.com/j1OInog.png]',
                       'doAngel': '[img=https://i.imgur.com/AI5RzbP.png]',
                       'doAlien': '[img=https://i.imgur.com/yF6Pkql.png]',
                       'doUnded': '[img=https://i.imgur.com/cx7Tn5F.png]',
                       'doAncient': '[img=https://i.imgur.com/OU1J4wV.png]',
                       'doDevil': '[img=]',
                       'isZombieKiller': '[img=https://i.imgur.com/0ojGu6X.png]',
                       'isWitchKiller':  '[img=https://i.imgur.com/oBKserF.png]',
                       'doImWave':       '[img=https://i.imgur.com/g5IMjt4.png]',
                       'doImUlwave':     '[img=https://i.imgur.com/aaEP8kB.png]',
                       'doBreakShield':  '[img=https://i.imgur.com/Fj7kWnN.png]',
                       'doDoubleMoney':  '[img=https://i.imgur.com/Z1K6FrX.png]',
                       'doStopWave':     '[img=https://i.imgur.com/0dk3TCD.png]',
                       'doWave':         '[img=https://i.imgur.com/YOx8lKv.png]',
                       'doLowAtk':       '[img=https://i.imgur.com/Wycq7dq.png]',
                       'ulwave':         '[img=https://i.imgur.com/6N5gLaR.png]',
                       'doAtkUP':        '[img=https://i.imgur.com/iFBwnpR.png]',
                       'doSuperDmg'  :   '[img=https://i.imgur.com/Hw8Zo0B.png]',
                       'doCri'       :   '[img=https://i.imgur.com/dKiP1zw.png]',
                       'curse'       :   '[img=https://i.imgur.com/Pj26dNE.png]',
                       'doImAtkDown' :   '[img=https://i.imgur.com/IHiXuOn.png]',
                       'doUltraDmg'  :   '[img=https://i.imgur.com/VfkWmTd.png]',
                       'doOnlyAttack':   '[img=https://i.imgur.com/gLpCuYC.png]',
                       'doFarAtk'    :   '[img=https://i.imgur.com/n9qTz6q.png]',
                       'doSlow'      :   '[img=https://i.imgur.com/R2Cn32s.png]',
                       'doPush'      :   '[img=https://i.imgur.com/ajdMeLD.png]',
                       'doStop'      :   '[img=https://i.imgur.com/hior6Hu.png]',
                       'doAllAtk'    :   '[img=https://i.imgur.com/UHQ93CE.png]', #全方攻擊
                       'doImSlow'    :   '[img=https://i.imgur.com/iBsbRqh.png]',
                       'doCriEx'     :   '[img=https://i.imgur.com/GILpXI4.png]',
                       'doImAtk'     :   '[img=https://i.imgur.com/LHsCm3I.png]',
                       'doCri'       :   '[img=https://i.imgur.com/7DzzAX4.png]',
                       'doGoodAt'    :   '[img=https://i.imgur.com/AiBSF13.png]',
                       'doTeleport'  :   '[img=https://i.imgur.com/chaCcMx.png]', #傳送
                       
                       
                       

                       
                       'hpUP'     : '[img=https://i.imgur.com/DVhmvJt.png]',
                       'reserved1': '[img=https://i.imgur.com/wyOsQEN.png]',
                       'reserved2': '[img=https://i.imgur.com/97kDXAU.png]',
                       '波動抗性' : '[img=https://i.imgur.com/6NJnVza.png]',
                       '詛咒抗性' : '[img=https://i.imgur.com/PYaFCgC.png]',
                       '跑速增加' : '[img=https://i.imgur.com/ErL2CZW.png]',
                       '降攻耐性' : '[img=https://i.imgur.com/tcgnn1O.png]',
                       

                       }
                       
    with open("config.ini",'w') as configfile:
        config.write(configfile)


config = configparser.ConfigParser()
config.sections()
config.read('config.ini')
contiExe = 0
defaultuid = 1
defaultstage = 0
activeUIDAsk = 0
activeStageAsk = 0
withimage = 0   
#if(f
if('DEFAULT' in config):
    try:
        print("exist config, loading default settings")
        contiExe = int(config['DEFAULT']['continueExecution'])
        defaultuid = config['DEFAULT']['defaultuid']
        defaultstage = config['DEFAULT']['defaultstage']
        activeUIDAsk = config['DEFAULT']['activeUIDAsk']
        activeStageAsk = config['DEFAULT']['activeStageAsk']
        withimage = config['DEFAULT']['withimage']
    except:
        print("exist no valid config, please delete the config.ini and restart!")
if(contiExe ==1 and activeUIDAsk=='1'):
    try:
        while(1):
            print("Recursive execution mode")
            print("Remeber input UID = -1 to end execution")
            FormWritter.FormWritter(config,defaultstage,defaultuid)
    except Exception as EndExecution:
        print("End")
else:
    FormWritter.FormWritter(config,defaultuid,defaultstage)