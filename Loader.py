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
                         'defaultuid': '383',
                         'defaultstage': '2',
                         'defaultmode' : '1',
                         'activeUIDAsk': '1',
                         'activeStageAsk': '1',
                         'activeModeAsk': '0',
                         'withimage': '0',
                         'UIDSaveFileName': '0',
                         'instinctatk' : '0',  #是否啟用本能
                         'instincthp' : '0',
                         'DefaultOutputFileName':'out.txt'
                         }
    config['LEVEL'] = {'mode1'  : '10,20,30,40,50', #Default Mode
                       'mode2'  : '30,50,70,90,130', #Default for R
                       'mode3'  : '30,40,50,60,70',  #Default for SR
                       'mode4'  : '30,40,45,50,60', #Default for SSR.
                       'mode5'  : '10,20,25,30,40', #Default for 巴哈姆特
                       'mode6'  : '10,20,30,40,50', #Default for 狂亂
                       'mode7'  : '60,80,100,120,130', #R/SR拓展
                       'mode8'  : '10,20,30,40,50',    #備用
                       'mode9'  : '10,20,30,40,50',    #備用
                       'mode1rd': ' -1,-1,-1,-1,-1', #不減益遞減
                       'mode2rd': ' 70,90,130,-1,-1', #Mode2的第一個遞減點,第二個,第三個,第四個,第五個, -1 = 留空
                       'mode3rd': ' 60,80,100,-1,-1',
                       'mode4rd': ' 60,80,100,-1,-1',
                       'mode5rd': ' 30,-1,-1,-1,-1',
                       'mode6rd': ' 20,-1,-1,-1,-1',
                       'mode7rd': ' 70,90,130,-1,-1',
                       'mode8rd': ' -1,-1,-1,-1,-1',
                       'mode9rd': ' -1,-1,-1,-1,-1'
                       
                       }
    config['CONST'] = {'maxlevel': '130'
                       }
    config['IMAGE'] = {'doRed'  : '[img=https://i.imgur.com/HagkEhI.png]',
                       'doFloat': '[img=https://i.imgur.com/XmW79pT.png]',
                       'doBlack': '[img=https://i.imgur.com/zUqTa3f.png]',
                       'doIron' : '[img=https://i.imgur.com/mAabf1v.png]',
                       'doWhite': '[img=https://i.imgur.com/j1OInog.png]',
                       'doAngel': '[img=https://i.imgur.com/AI5RzbP.png]',
                       'doAlien': '[img=https://i.imgur.com/yF6Pkql.png]',
                       'doUnded': '[img=https://i.imgur.com/cx7Tn5F.png]',
                       'doAncient':'[img=https://i.imgur.com/OU1J4wV.png]',
                       'doDevil': '[img=https://i.imgur.com/7leUuJl.jpg?2]',
                       'isZombieKiller': '[img=https://i.imgur.com/0ojGu6X.png]',
                       'isEvaKiller':   '[img=https://i.imgur.com/oBKserF.png]',
                       'isWitchKiller':  '[img=https://i.imgur.com/beOdZ0A.png]',
                       'doImWave':       '[img=https://i.imgur.com/g5IMjt4.png]',
                       'doImUlwave':     '[img=https://i.imgur.com/aaEP8kB.png]',
                       'doBreakShield':  '[img=https://i.imgur.com/Fj7kWnN.png]',
                       'doDoubleMoney':  '[img=https://i.imgur.com/Z1K6FrX.png]',
                       'doStopWave':     '[img=https://i.imgur.com/0dk3TCD.png]',
                       'doWave':         '[img=https://i.imgur.com/YOx8lKv.png]',
                       'doLowAtk':       '[img=https://i.imgur.com/Wycq7dq.png]',
                       'ulwave':         '[img=https://i.imgur.com/6N5gLaR.png]',
                       'doAtkUP':        '[img=https://i.imgur.com/iFBwnpR.png]',
                       'doUltraDmg'  :   '[img=https://i.imgur.com/Hw8Zo0B.png]',
                       'doCri'       :   '[img=https://i.imgur.com/dKiP1zw.png]',
                       'curse'       :   '[img=https://i.imgur.com/Pj26dNE.png]',
                       'doImAtkDown' :   '[img=https://i.imgur.com/IHiXuOn.png]',
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
                       'doPoison'    :   '[img=https://i.imgur.com/ofldtGL.png]', #毒擊
                       'sing'        :   '[img=https://i.imgur.com/AqvxGe6.png]',
                       'non-sing'    :   '[img=https://i.imgur.com/j2MtXjW.png]',
                       'contiatk'    :   '[img=https://i.imgur.com/veNQ90x.png]',
                     #  'doCri'       :   '[img=https://i.imgur.com/JqolgYZ.png]',               
                       'doSelfIron'  :   '[img=https://i.imgur.com/egTthQy.png]',
                       'doImPoison'  :   '[img=https://i.imgur.com/a78KkC0.png]',
                       'doCastleDmg' :   '[img=https://i.imgur.com/lK5O0wT.png]',
                       'doReborn'    :   '[img=https://i.imgur.com/I4gG2Qy.png]',
                       'doImPush'    :   '[img=https://i.imgur.com/hijWXn2.png]',
                       'doSuperDmg'  :   '[img=https://i.imgur.com/Bk1hfZw.png]',
                       'doImStop'    :   '[img=https://i.imgur.com/pjMjbvQ.png]',
                       'doUltraHealth':  '[img=https://i.imgur.com/fJ7pTzO.png]',
                       'doSuperHealth':  '[img=https://i.imgur.com/uEikACY.png]',
                       'doImCurse'   :   '[img=https://i.imgur.com/UXB5MVe.png]',
                       'doImTeleport' :  '[img=https://i.imgur.com/MDoxflp.png]',
                       'doSmallWave' :   '[img=https://i.imgur.com/VUUrEOI.jpg?1]',
                       'doBreakDevilShiled': '[img=https://i.imgur.com/ZzW9bow.png]',
                        
                       'hpUP'     : '[img=https://i.imgur.com/DVhmvJt.png]',
                       'atkUP'    : '[img=https://i.imgur.com/fmIp54Z.png]',
                       'KBUP'     : '[img=https://i.imgur.com/7ZEMrqe.png]',
                       'reserved1': '[img=https://i.imgur.com/wyOsQEN.png]',
                       'reserved2': '[img=https://i.imgur.com/97kDXAU.png]',
                       'reserved3': '[img=https://i.imgur.com/VfkWmTd.png]',
                       'reserved4': '[img=https://i.imgur.com/bTnjA9F.png]',
                       'reserved5': '[img=https://i.imgur.com/DCRST5X.png]',
                       'empty'    : '[img=https://i.imgur.com/VlCNJuM.png]',
                       'nointer'  : '[img=https://i.imgur.com/KqtrO2b.png]',#擊退反擊          
                       '波動抗性' : '[img=https://i.imgur.com/6NJnVza.png]',
                       '詛咒抗性' : '[img=https://i.imgur.com/PYaFCgC.png]',
                       '跑速增加' : '[img=https://i.imgur.com/ErL2CZW.png]',
                       '降攻耐性' : '[img=https://i.imgur.com/tcgnn1O.png]',
                       '傳送抗性' : '[img=https://i.imgur.com/mlLJnBI.png]',
                       '擊退抗性' : '[img=https://i.imgur.com/pRVfnWt.png]',
                       '緩速抗性' : '[img=https://i.imgur.com/0aAnwtB.png]',
                       '暫停抗性' : '[img=https://i.imgur.com/Q8CXnls.png]',
                       
                       
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
