def imgdrawer(SPAbility,colortemplate,config):

    print("this")
#    f = open(filename, 'r',encoding="utf-8")
    
 #   raw = f.read()
    edit = ""
#    print(raw)
    if(not colortemplate==""):
        if(not ((colortemplate.find("紅"))==-1)):
            edit = edit + config['IMAGE']['doRed']
            print("exist red.")
        if(not ((colortemplate.find("浮"))==-1)):
            edit = edit + config['IMAGE']['doFloat']
            print("exist float.")
        if(not ((colortemplate.find("黑"))==-1)):
            edit = edit + config['IMAGE']['doBlack']
            print("exist black.")
        if(not ((colortemplate.find("鐵"))==-1)):
            edit = edit + config['IMAGE']['doIron']
            print("exist iron.")
        if(not ((colortemplate.find("天"))==-1)):
            edit = edit + config['IMAGE']['doAngel']
            print("exist angel.")
        if(not ((colortemplate.find("星"))==-1)):
            edit = edit + config['IMAGE']['doAlien']
            print("exist alien.")
        if(not ((colortemplate.find("屍"))==-1)):
            edit = edit + config['IMAGE']['doUnded']
            print("exist unded.")
        if(not ((colortemplate.find("白"))==-1)):
            edit = edit + config['IMAGE']['doWhite']
            print("exist white.")
        if(not ((colortemplate.find("古"))==-1)):
            edit = edit + config['IMAGE']['doAncient']
            print("exist ancient.")
        if(not ((colortemplate.find("惡"))==-1)):
            edit = edit + config['IMAGE']['doDevil']
            print("exist devil.")

        print(edit)
    nSP = ""
    SPAbility = edit +'\n'+ SPAbility
    trypos = SPAbility.find('屬性的敵人傷害傷害1.5倍(1.8倍)')
    if(trypos!=-1):
        trypos = SPAbility.find('對',trypos-10)
        SPAbility = inserter(SPAbility,trypos,'doGoodAt',config)
        
    trypos = SPAbility.find('屬性敵人造成3倍(4倍)傷害)')
    if(trypos!=-1):
        trypos = SPAbility.find('對',trypos-10)
        SPAbility = inserter(SPAbility,trypos,'doSuperDmg',config)
        
    trypos = SPAbility.find('屬性敵人攻擊的傷害減至1/4(1/5)')
    if(trypos!=-1):
        trypos = SPAbility.find('受到',trypos-10)
        SPAbility = inserter(SPAbility,trypos,'doSuperHealth',config)
        
    trypos = SPAbility.find('屬性敵人造成5倍(6倍)傷害')
    if(trypos!=-1):
        trypos = SPAbility.find('對',trypos-10)
        SPAbility = inserter(SPAbility,trypos,'doUltraDmg',config)
        
    trypos = SPAbility.find('屬性敵人攻擊的傷害減至1/6(1/7)')
    if(trypos!=-1):
        trypos = SPAbility.find('受到',trypos-10)
        SPAbility = inserter(SPAbility,trypos,'doUltraHealth',config)
        
    trypos = SPAbility.find('%機率緩速')
    if(trypos!=-1):
        trypos = trypos-5
        if(trypos<0):
            trypos = 0
        trypos = SPAbility.find('\n',trypos)+1  
        SPAbility = inserter(SPAbility,trypos,'doSlow',config)
        
    trypos = SPAbility.find('%機率擊退')
    if(trypos!=-1):
        trypos = trypos-5
        if(trypos<0):
            trypos = 0
        trypos = SPAbility.find('\n',trypos)+1  
        SPAbility = inserter(SPAbility,trypos,'doPush',config)
        
    trypos = SPAbility.find('%機率暫停')
    if(trypos!=-1):
        trypos = trypos-5
        if(trypos<0):
            trypos = 0
        trypos = SPAbility.find('\n',trypos)+1  
        SPAbility = inserter(SPAbility,trypos,'doStop',config)
        
    trypos = SPAbility.find('%機率降低')
    if(trypos!=-1):
        trypos = trypos-5
        if(trypos<0):
            trypos = 0
        trypos = SPAbility.find('\n',trypos)+1  
        SPAbility = inserter(SPAbility,trypos,'doLowAtk',config)

    trypos = SPAbility.find('%機率詛咒')
    if(trypos!=-1):
        trypos = trypos-5
        if(trypos<0):
            trypos = 0
        trypos = SPAbility.find('\n',trypos)+1  
        SPAbility = inserter(SPAbility,trypos,'curse',config)

    trypos = SPAbility.find('%機率發動攻擊無效')
    if(trypos!=-1):
        trypos = SPAbility.find('受到',trypos-40)  #This might have bugs
        SPAbility = inserter(SPAbility,trypos,'doImAtk',config)

    trypos = SPAbility.find('%機率使出會心一擊')
    if(trypos!=-1):
        trypos = trypos-5
        if(trypos<0):
            trypos = 0
        trypos = SPAbility.find('\n',trypos)+1   
        SPAbility = inserter(SPAbility,trypos,'doCri',config)

    trypos = SPAbility.find('渾身一擊')
    if(trypos!=-1):
        trypos = SPAbility.find('%機率使出',trypos-14)
        trypos = trypos-5
        if(trypos<0):
            trypos = 0
        trypos = SPAbility.find('\n',trypos)+1  
        SPAbility = inserter(SPAbility,trypos,'doCriEx',config)

    trypos = SPAbility.find('%機率放出Lv')
    if(trypos!=-1):
        trypos3 = -1
        trypos2 = SPAbility.find('烈波(出現位置',trypos)
        if(trypos2!=-1):
            trypos3 = trypos-5
            if(trypos3<0):
                trypos3 = 0
            trypos = SPAbility.find('\n',trypos3)+1  
            SPAbility = inserter(SPAbility,trypos,'ulwave',config)
        else:
            trypos2 = SPAbility.find('小波動',trypos)
            if(trypos2!=-1):
                trypos = trypos-10
                if(trypos<0):
                    trypos = 0
                trypos3=SPAbility.find('\n',trypos)+1
                SPAbility = inserter(SPAbility,trypos3,'doOSmallWave',config)
            else:
                trypos = trypos-10
                if(trypos<0):
                    trypos=0
                trypos3=SPAbility.find('\n',trypos)+1
                SPAbility = inserter(SPAbility,trypos3,'doWave',config)
    trypos = SPAbility.find('以1血存活一次')
    if(trypos!=-1):
        trypos = SPAbility.find('\n',trypos-10)+1
        SPAbility = inserter(SPAbility,trypos,'doReborn',config)

    trypos = SPAbility.find('回連續攻擊')
    if(trypos!=-1):
        trypos = trypos-5
        if(trypos<0):
            trypos = 0
        trypos = SPAbility.find('\n',trypos)+1   
        SPAbility = inserter(SPAbility,trypos,'contiatk',config)
        
    trypos = SPAbility.find('一回攻擊')
    if(trypos!=-1):
        SPAbility = inserter(SPAbility,trypos,'empty',config)
    trypos = SPAbility.find('擊退反擊')
    if(trypos!=-1):
        SPAbility = inserter(SPAbility,trypos,'nointer',config)
    trypos = SPAbility.find('只能攻擊')
    if(trypos!=-1):
        SPAbility = inserter(SPAbility,trypos,'doOnlyAttack',config)
    trypos = SPAbility.find('遠方攻擊')
    if(trypos!=-1):
        SPAbility = inserter(SPAbility,trypos,'doFarAtk',config)
    trypos = SPAbility.find('全方位攻擊')
    if(trypos!=-1):
        SPAbility = inserter(SPAbility,trypos,'doAllAtk',config)
    trypos = SPAbility.find('善於攻城(4倍傷害)')
    if(trypos!=-1):
        SPAbility = inserter(SPAbility,trypos,'doCastleDmg',config)
    trypos = SPAbility.find('擊倒敵人獲得兩倍金錢')
    if(trypos!=-1):
        SPAbility = inserter(SPAbility,trypos,'doDoubleMoney',config)
    trypos = SPAbility.find('波動無效')
    if(trypos!=-1):
        SPAbility = inserter(SPAbility,trypos,'doImWave',config)
    trypos = SPAbility.find('波動滅止')
    if(trypos!=-1):
        SPAbility = inserter(SPAbility,trypos,'doImWave',config)
    trypos = SPAbility.find('烈波無效')
    if(trypos!=-1):
        SPAbility = inserter(SPAbility,trypos,'doImUlwave',config)
    trypos = SPAbility.find('毒擊無效')
    if(trypos!=-1):
        SPAbility = inserter(SPAbility,trypos,'doImPoison',config)
    trypos = SPAbility.find('擊退無效')
    if(trypos!=-1):
        SPAbility = inserter(SPAbility,trypos,'doImPush',config)
    trypos = SPAbility.find('暫停無效')
    if(trypos!=-1):
        SPAbility = inserter(SPAbility,trypos,'doImStop',config)
    trypos = SPAbility.find('緩速無效')
    if(trypos!=-1):
        SPAbility = inserter(SPAbility,trypos,'doImSlow',config)
    trypos = SPAbility.find('降攻無效')
    if(trypos!=-1):
        SPAbility = inserter(SPAbility,trypos,'doImAtkDown',config)
    trypos = SPAbility.find('傳送無效')
    if(trypos!=-1):
        SPAbility = inserter(SPAbility,trypos,'doImTeleport',config)
    trypos = SPAbility.find('詛咒無效')
    if(trypos!=-1):
        SPAbility = inserter(SPAbility,trypos,'doImCurse',config)
    trypos = SPAbility.find('殭屍殺手')
    if(trypos!=-1):
        SPAbility = inserter(SPAbility,trypos,'isZombieKiller',config)
    trypos = SPAbility.find('魔女殺手')
    if(trypos!=-1):
        SPAbility = inserter(SPAbility,trypos,'isWitchKiller',config)
    trypos = SPAbility.find('EVA殺手')
    if(trypos!=-1):
        SPAbility = inserter(SPAbility,trypos,'isEvaKiller',config)


   
    return SPAbility







    
def inserter(str1,pos,name,config):
    try:
        inst = config['IMAGE'][name]
        str1 = str1[:pos]+inst+str1[pos:]
        return str1
    except:
        print("find ability of "+str(name)+", but fail to add image")
        return str1
