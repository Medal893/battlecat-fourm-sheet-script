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
