
##--------Constant Define------
#uid = 608
#334 黑獸 size = 55, all larger than 55 have to have try protection
#442 黑傑 381 英傑
#270 皇獸
#530 白災 544黑災
#319 白無垢 #381白傑
#610 黑帝獸
#stage = 2;  #0 = stage1, 1 = stage2, 2 = stage3
##--------End Constant Define---
#Try load from argv to override uid and stage

def FormWritter(config,uid,stage):
#    defaultstage = config['DEFAULT']['defaultstage']
    activeUIDAsk = int(config['DEFAULT']['activeUIDAsk'])
    activeStageAsk = int(config['DEFAULT']['activeStageAsk'])
    activeModeAsk = int(config['DEFAULT']['activeModeAsk'])

    uid = int(config['DEFAULT']['defaultuid'])
    stage = int(config['DEFAULT']['defaultstage'])
    mode = config['DEFAULT']['defaultmode']

    withimage = config['DEFAULT']['withimage']
    maxlevel = int(config['CONST']['maxlevel'])
    instinctatk = float(config['CONST']['instinctatk']) + 1
    instincthp = float(config['CONST']['instincthp']) + 1

    import configparser
    import numpy as np
    import csv
    import Animation_Length as ani
    import MultiAttack_effect as ma
    import sys
    try:
        uid = int(sys.argv[1])
        stage = int(sys.argv[2])
    except:
        if(activeUIDAsk):
            print("Input UID:",end='')
            uid = int(input())
            if(uid==-1):
                raise Exception('EndExecution')
        if(activeStageAsk):
            print("Input Stage:",end='')
            stage = int(input())
        if(activeModeAsk):
            print("Input Mode:",end='')
            mode = int(input())
#        print("Not exist extra param")

    ##POS
    if(uid<10):
        filename = 'Unit/unit00'+str(uid)+'.csv'
    elif(uid<100):
        filename = 'Unit/unit0'+str(uid)+'.csv'
    else:
        filename = 'Unit/unit'+str(uid)+'.csv'
    print(filename)
    atk_anil = 0
    try:
        atk_anil = ani.getAniLength(uid,stage)
    except:
        print("Animation infor not exist or failed")
    atk_allinf =  187 #frame.
    ##POS
    #open files.
    f = open('raw.txt', 'r',encoding="utf-8")

    raw = f.read()

    #print(raw);
    f.close();

    #Solve Level Problem

    loadlevelmode = config['LEVEL']["mode"+str(mode)]
    loadleveldecreate = config['LEVEL']["mode"+str(mode)+"rd"]
    llm = loadlevelmode.split(',')
    lld = loadleveldecreate.split(',')
    print(llm)
    print(lld)
    intlld = []
    for i in range(0,5):
        if lld[i]=='-1':
            lld[i] = str(maxlevel*2)
    intlld.append(int(lld[0]))
    intlld.append(int(lld[1]))
    intlld.append(int(lld[2]))
    intlld.append(int(lld[3]))
    intlld.append(int(lld[4]))
    print(intlld)
    lld = [1] #slot one didn't use
    for i in range(1, maxlevel+2):
        if i<= intlld[0]:
            lld.append(1)
        elif i <= intlld[1]:
            lld.append(2)
        elif i <= intlld[2]:
            lld.append(4)
        elif i <= intlld[3]:
            lld.append(8)
        elif i <= intlld[4]:
            lld.append(16)
        else:
            lld.append(1)
    print(lld)
    #Create new table of lld
#raw = raw.replace(tempstr,str2)
    lc = []     #levelconst
    
    cal1 = int(llm[0])
    cal2 = "Lv"+str(cal1)
    raw = raw.replace('_lv1',cal2)
    ssum = 0
    for i in range(1,cal1+1):
        ssum = ssum + (1/lld[i])
    ssum = (4+ssum)/2
    lc.append(ssum)

    cal1 = int(llm[1])
    cal2 = "Lv"+str(cal1)
    raw = raw.replace('_lv2',cal2)
    ssum = 0
    for i in range(1,cal1+1):
        ssum = ssum + (1/lld[i])
    ssum = (4+ssum)/2
    lc.append(ssum)

    cal1 = int(llm[2])
    cal2 = "Lv"+str(cal1)
    ssum = 0
    for i in range(1,cal1+1):
        ssum = ssum + (1/lld[i])
    raw = raw.replace('_lv3',cal2)
    ssum = (4+ssum)/2
    lc.append(ssum)

    cal1 = int(llm[3])
    cal2 = "Lv"+str(cal1)
    ssum = 0
    for i in range(1,cal1+1):
        ssum = ssum + (1/lld[i])
    raw = raw.replace('_lv4',cal2)
    ssum = (4+ssum)/2
    lc.append(ssum)

    cal1 = int(llm[4])
    cal2 = "Lv"+str(cal1)
    ssum = 0
    for i in range(1,cal1+1):
        ssum = ssum + (1/lld[i])
    raw = raw.replace('_lv5',cal2)
    ssum = (4+ssum)/2
    lc.append(ssum)

    print(lc)
    
    #f = open(filename,'r',encoding="utf-8")
    #try open directly with np.loadtxt
    try:
        source=np.loadtxt(filename,dtype=str,delimiter=',',encoding="utf-8")
    except:
        print("Exist error with tradition Numpy open method, used compatible method to open")
        #use compatible mode for some special case like uid136.
        with open(filename,encoding="utf-8") as f:
            z0 = f.read().split('\n')
            z1 = z0[0].split(',')
            z2 = z0[1].split(',')
            z3 = z0[2].split(',')
            source = [z1,z2,z3]
    print(source)
    #txt = f.read()
    #end files.

    #Variation Initialize.
    hp = int(source[stage][0])  
    kb = int(source[stage][1])  #always lowcaps
    speed = int(source[stage][2]) #Raw, no need multiply.
    atk1= int(source[stage][3])
    atk2 = 0
    atk3 = 0
    atk = atk1 + atk2 + atk3
    inter21 = int(source[stage][13]) #攻發1
    inter22 = 0
    inter23 = 0
    inter24 = inter21
    doAtk1Aff = 0
    doAtk2Aff = 0
    doAtk3Aff = 0
    try:
        atk2= int(source[stage][59])
        atk3= int(source[stage][60])
        atk = atk1 + atk2 + atk3
        inter22 = int(source[stage][61])
        inter23 = int(source[stage][62])
        inter24 = max(inter21,inter22,inter23)
        doAtk1Aff = int(source[stage][63])#第一段攻擊是否有能力
        doAtk2Aff = int(source[stage][64])
        doAtk3Aff = int(source[stage][65])

    except:
        print('This cat is older than 6.0, not exist multiatk')
        atk = atk1
    inter1 = int(source[stage][4]) #間隔
    arange = int(source[stage][5]) #射程   #no need multiply.
    arrange2 = int(source[stage][44]) #感應射程 遠方攻擊用
    arrange3 = int(source[stage][45]) #延伸射程 遠方攻擊用
    price= int(source[stage][6])   #Chapter1
    sing=  int(source[stage][12])   #單體/範圍
    regen = int(source[stage][7]) #再生產

    #Color Enemy Enabler.
    existColor = False
    doRed=   int(source[stage][10])
    doFloat= int(source[stage][16])
    doBlack= int(source[stage][17])
    doIron=  int(source[stage][18])
    doWhite= int(source[stage][19])
    doAngel= int(source[stage][20])
    doAlien= int(source[stage][21])
    doUnded= int(source[stage][22])
    doAncient = 0
    doDevil = 0 
    try:
        doAncient= int(source[stage][78])
        doDevil=   int(source[stage][96])
    except:
        print("This cat is older than 7.0, not exist ancient")
    print("doDevil?")
    print(doDevil)
    if(doRed+doFloat+doBlack+doIron+doWhite+doAngel+doAlien+doUnded+doAncient+doDevil>0):
        existColor = True;
    #Ability Calculation
    doGoodAt = int(source[stage][23])   #善於攻擊
    doSuperDmg = int(source[stage][30]) #超大傷害
    doSuperHealth = int(source[stage][29]) #很耐打
    doCastleDmg = int(source[stage][34]) #擅攻城
    doOnlyAttack = int(source[stage][32]) #只能攻擊
    doDoubleMoney = int(source[stage][33])#很多金錢
    doWave = int(source[stage][35]) #波動%
    doWave2 = int(source[stage][36])#波動段數
    doPowerUp = int(source[stage][40]) #體降升攻體力門檻%
    doPowerUp2 = int(source[stage][41]) #體降生攻%
    doCri = int(source[stage][31]) #爆擊%
    doUltraDmg = 0
    doUltraHealth = 0
    doCriEx = 0
    doCriEx2 = 0
    doImAtk = 0
    doImAtk2 = 0
    try:
        doUltraDmg = int(source[stage][81]) #極度傷害 #UR
        doUltraHealth = int(source[stage][80]) #極度耐打 #UR
        doCriEx = int(source[stage][82]) #渾身機率
        doCriEx2 = int(source[stage][83])#渾身倍率
        doImAtk = int(source[stage][84]) #攻擊無效%
        doImAtk2 = int(source[stage][85]) #攻擊無效F
        atk = atk
        
    except:
        print("This cat is older than 7.0, not exist ultradmg like")
    ulwave = 0
    ulwave_dist = 0
    ulwave_range = 0
    ulwave_num = 0
    try:
        ulwave= int(source[stage][86])
        ulwave_dist= int(source[stage][87])
        ulwave_range= int(source[stage][88])
        ulwave_num= int(source[stage][89])
    except:
        print("This cat is older than 9.5, not exist ulwave-relate def")
    doCurse = 0
    doCurse2 = 0
    try:
        doCurse = int(source[stage][92]) #詛咒機率
        doCurse2 = int(source[stage][93]) #詛咒時長

    except:
        print("This cat is older than 9.8, not exist curse-relative def")
    doSmallWave = 0
    try:
        doSmallWave = int(source[stage][94])
    except:
        print("This cat is older than 10.1, not exist small-wave")

    #These not affect dmg or health
    doPush = int(source[stage][24]) #擊退
    doStop = int(source[stage][25])  #暫停
    doStop2 = int(source[stage][26]) #暫停時間
    doSlow = int(source[stage][27]) #緩速
    doSlow2 = int(source[stage][28]) #緩速時間
    doSelfIron = int(source[stage][43]) #鋼鐵屬性
    doLowAtk = int(source[stage][37]) #降攻%
    doLowAtk2 = int(source[stage][38])#降攻時間
    doLowAtk3 = int(source[stage][39])#降攻比例
    doReborn = int(source[stage][42]) #死前存活% #根性



    #Immunity
    doImWave = int(source[stage][46])
    doStopWave = int(source[stage][47])
    doImPush = int(source[stage][48])
    doImStop = int(source[stage][49])
    doImSlow = int(source[stage][50])
    doImAtkDown = int(source[stage][51])
    doImTeleport = 0
    doImCurse = 0
    try:
        doImTeleport = int(source[stage][75])
        doImCurse = int(source[stage][79])
    except:
        print("This cat is Older than teleport and ancient curse immune, not exist Teleport Immunnity")
    isZombieKiller = 0
    isWitchKiller = 0
    isEvaKiller = 0
    doAtkTime = -1
    doLifeTime = -1
    doBreaShield = 0
    doBreakDevilShield = 0
    #Other ability.
    try:
        isZombieKiller = int(source[stage][52])#殭屍殺手
        isWitchKiller = int(source[stage][53])#魔女殺手
        isEvaKiller = int(source[stage][77])#使徒殺手
        doAtkTime = int(source[stage][55])#攻擊回數, should be -1
        doLifeTime = int(source[stage][57])#生存時長, should be -1
        doBreakShield = int(source[stage][70]) #破盾機率
        #96-1 = 95
        doBreakDevilShield = int(source[stage][95])#破惡魔盾機率
        
    except:
        print("Not Exist Special Killer")
    SPDeathAni = 0
    doImUlwave = 0
    doImPoison = 0
    try:
        SPDeathAni = int(source[stage][67])
        doImPoison = int(source[stage][90])
        doImUlwave = int(source[stage][91])
        
    except:
        print("exist no death animation")
        

    ##--------------------------------------------
    #str.replace(old, new[, max])

    #Multiplier

    #Construct Template
    stri = "Temp11\n"
    #stri = stri + str(atk*7) + "\n"
    existColor_G = 0
    existColor_N = 0
    if(existColor):
        if(doRed==1):
            stri = stri + "紅"
        if(doFloat==1):
            stri = stri + "浮"
        if(doBlack==1):
            stri = stri + "黑"
        if(doIron==1):
            stri = stri + "鐵"
        if(doAngel==1):
            stri = stri + "天"
        if(doAlien==1):
            stri = stri + "星"
        if(doUnded==1):
            stri = stri + "屍"
        existColor_G = bool(doRed+doFloat+doBlack+doIron+doAngel+doUnded+doAlien)
        if(existColor_G):
            stri = stri + "Temp12\n"
            
        if(doWhite==1):
            stri = stri + "白"
        if(doAncient==1):
            stri = stri + "古"
        if(doDevil==1):
            stri = stri + "惡"
        existColor_N = bool(doWhite+doAncient+doDevil)
        if(existColor_N):
            stri = stri + "Temp13\n"
        print("Template:")
        print(stri)


    #Fill Atk Blenks
    atk = int(atk*instinctatk)
    hp = int(hp * instincthp)
    #1 Atk
    if(not(doGoodAt==1 or doSuperDmg==1 or doUltraDmg==1)): #Check if need the Tempalte or not
        str1 = "Temp11"
    else:
        str1 = stri;
    i = 0
    ansval = 1.0
    for i in range(0,7):
        if(i<5):
            cst = lc[i]
            tempstr = "_at."+str(i+1);
        else:
            cst = 0.5
            tempstr = "_at.6";
        str2 = str1
      #  print(doSuperDmg)
      #  print(str2)
        str2 = str2.replace("Temp11", str(int(atk*cst)))
        if(doGoodAt):
            if(existColor_G):
                ansval = int(round(atk*cst*1.8))
                str2 = str2.replace("Temp12",str(ansval))
            if(existColor_N):
                ansval = int(round(atk*cst*1.5))
                str2 = str2.replace("Temp13",str(ansval))
        if(doSuperDmg):
            if(existColor_G):
                ansval = int(round(atk*cst*4))
                str2 = str2.replace("Temp12",str(ansval))
            if(existColor_N):
                ansval = int(round(atk*cst*3))
                str2 = str2.replace("Temp13",str(ansval))
        if(doUltraDmg):
            if(existColor_G):
                ansval = int(round(atk*cst*6))
                str2 = str2.replace("Temp12",str(ansval))
            if(existColor_N):
                ansval = int(round(atk*cst*5))
                str2 = str2.replace("Temp13",str(ansval))
       # print(str2)
        raw = raw.replace(tempstr,str2)

    #2 Health
    if(doGoodAt==1 or doSuperHealth==1 or doUltraHealth==1): #Check if need the Tempalte or not
        str1 = stri
    else:
        str1 = "Temp11"

    i = 0
    for i in range(0,7):
        if(i<5):
            cst = lc[i]
            tempstr = "_hp."+str(i+1);
        else:
            cst = 0.5
            tempstr = "_hp.6";
        str2 = str1
      #  print(str2)
        str2 = str2.replace("Temp11", str(int(hp*cst)))
        if(doGoodAt):
            if(existColor_G):
                ansval = int(round(hp*cst*(1/0.4)))
                str2 = str2.replace("Temp12",str(ansval))
            if(existColor_N):
                ansval = int(round(hp*cst*(1/0.5)))
                str2 = str2.replace("Temp13",str(ansval))
        if(doSuperHealth):
            if(existColor_G):
                ansval = int(round(hp*cst*5))
                str2 = str2.replace("Temp12",str(ansval))
            if(existColor_N):
                ansval = int(round(hp*cst*4))
                str2 = str2.replace("Temp13",str(ansval))
        if(doUltraHealth):
            if(existColor_G):
                ansval = int(round(hp*cst*7))
                str2 = str2.replace("Temp12",str(ansval))
            if(existColor_N):
                ansval = int(round(hp*cst*6))
                str2 = str2.replace("Temp13",str(ansval))    
    #    print(str2)
        raw = raw.replace(tempstr,str2)


    #3 Hard
    if(doGoodAt==1 or doSuperHealth==1 or doUltraHealth==1): #Check if need the Tempalte or not
        str1 = stri
    else:
        str1 = "Temp11"

    i = 0
    for i in range(0,7):
        if(i<5):
            cst = lc[i]
            tempstr = "_hd."+str(i+1);
        else:
            cst = 0.5
            tempstr = "_hd.6";
        str2 = str1
     #   print(str2)
        str2 = str2.replace("Temp11", str(int(hp*cst/kb)))
        if(doGoodAt):
            if(existColor_G):
                ansval = int(round(hp*cst*(1/0.4)/kb))
                str2 = str2.replace("Temp12",str(ansval))
            if(existColor_N):
                ansval = int(round(hp*cst*(1/0.5)/kb))
                str2 = str2.replace("Temp13",str(ansval))
        if(doSuperHealth):
            if(existColor_G):
                ansval = int(round(hp*cst*5)/kb)
                str2 = str2.replace("Temp12",str(ansval))
            if(existColor_N):
                ansval = int(round(hp*cst*4)/kb)
                str2 = str2.replace("Temp13",str(ansval))
        if(doUltraHealth):
            if(existColor_G):
                ansval = int(round(hp*cst*7)/kb)
                str2 = str2.replace("Temp12",str(ansval))
            if(existColor_N):
                ansval = int(round(hp*cst*6)/kb)
                str2 = str2.replace("Temp13",str(ansval))  
    #    print(str2)
        raw = raw.replace(tempstr,str2)


    #4 dps
    #    inter24 = inter21
        #inter1 間隔
    atk_anil = atk_anil+1 #將動畫長度永久+1(從0/從1開始)
    atkfq = max(atk_anil,inter1*2+inter24-1)
    print("Atk Animation Length=",end='')
    print(atk_anil)
    print("Standard Analysis length=",end='')
    print(inter1*2+inter24-1)
    print("atkfq= ",end='')
    print(atkfq)
#    atkfq = atkfq / 30
#    print(atkfq)
    rdpoint = 0
    ansval = 1.0
    #Here is the final pos where used variation atk, calculate the expectation of dmg
    '''
    doCri = int(source[stage][31]) #爆擊%
    doUltraDmg = 0
    doUltraHealth = 0
    doCriEx = 0
    doCriEx2 = 0
    '''
    print(atk)
    atk = (1+(doCri/100))*(1+(doCriEx2/100)*(doCriEx/100))*atk
    print("加權後攻擊力:")
    print(atk)
    print(atk_anil)
    print("攻擊力計入爆渾期望值，不計入波動/血量降增攻")
    if(not(doGoodAt==1 or doSuperDmg==1 or doUltraDmg==1)): #Check if need the Tempalte or not
        str1 = "Temp11"
    else:
        str1 = stri;
    i = 0
    for i in range(0,7):
        if(i<5):
            cst = lc[i]
            tempstr = "_dp."+str(i+1);
            rdpoint = 0
        else:
            cst = 0.5
            tempstr = "_dp.6";
            rdpoint = 1
        str2 = str1
    #    print(doSuperDmg)
      #  print(str2)
        if not rdpoint:
            ansval = int(round(atk*cst*30/atkfq,rdpoint))
        else:
            ansval = round(atk*cst*30/atkfq,rdpoint)
        str2 = str2.replace("Temp11", str(ansval))
        if(doGoodAt):
            if(existColor_G):
                if not rdpoint:
                    ansval = int(round(atk*cst*1.8*30/atkfq,rdpoint))
                else:
                    ansval = round(atk*cst*1.8*30/atkfq,rdpoint)
                str2 = str2.replace("Temp12", str(ansval))
            if(existColor_N):
                if not rdpoint:
                    ansval = int(round(atk*cst*1.5*30/atkfq,rdpoint))
                else:
                    ansval = round(atk*cst*1.5*30/atkfq,rdpoint)
                str2 = str2.replace("Temp13", str(ansval))
        if(doSuperDmg):
            if(existColor_G):
                if not rdpoint:
                    ansval = int(round(atk*cst*4*30/atkfq,rdpoint))
                else:
                    ansval = round(atk*cst*4*30/atkfq,rdpoint)
                str2 = str2.replace("Temp12", str(ansval))
            if(existColor_N):   
                if not rdpoint:
                    ansval = int(round(atk*cst*3*30/atkfq,rdpoint))
                else:
                    ansval = round(atk*cst*3*30/atkfq,rdpoint)
                str2 = str2.replace("Temp13", str(ansval))
        if(doUltraDmg):
            if(existColor_G):
                if not rdpoint:
                    ansval = int(round(atk*cst*6*30/atkfq,rdpoint))
                else:
                    ansval = round(atk*cst*4*30/atkfq,rdpoint)
                str2 = str2.replace("Temp12", str(ansval))
            if(existColor_N):   
                if not rdpoint:
                    ansval = int(round(atk*cst*5*30/atkfq,rdpoint))
                else:
                    ansval = round(atk*cst*3*30/atkfq,rdpoint)
                str2 = str2.replace("Temp13", str(ansval))

      #  print(str2)
        raw = raw.replace(tempstr,str2)


        #endAuto

    #raw = raw.replace("_fq1") Unknown Message.

    #Frequency, Need Consider MultiAttack
    try:
        str4 = str(round(inter21/30,2))
        if(inter22>0):
            str4 = str4 +"秒\n/ " + str(round(inter22/30,2))
        if(inter23>0):
            str4 = str4 +"秒\n/ " + str(round(inter23/30,2))
    except:
        print("No MultiAttack")

    str4 = str4 + " 秒"
    raw = raw.replace("_fq2",str4) #出招時間

    raw = raw.replace("_fq1",str(round(atkfq/30,2))+" 秒/下") #攻擊頻率
    realregen = regen*2-254
    if(realregen<=60):
        realregen = 60        
    raw = raw.replace("_fq4",str(round(realregen/30,2))) #再生產

    str7 = str(arange)
    if(arrange2==0):
        str7 = str(arange)
    else:
        if(arrange3>=0):
            str7 = "接觸點"+str(arange)+'\n'+"範圍"+str(arrange2)+"~"+str(arrange2+arrange3)
        else:
            str7 = "接觸點"+str(arange)+'\n'+"範圍"+str(arrange2+arrange3)+"~"+str(arrange2)
            
    raw = raw.replace("_range",str7)
    raw = raw.replace("_speed",str(speed))
    raw = raw.replace("_KB",str(kb))
    atk_inter = round((atkfq-atk_anil)/30,2)
    print("間隔: "+str(atk_inter))
    raw = raw.replace("_fq3",(str(atk_inter)+"秒"))  #間隔
    atkleft = atk_anil - inter24  #收招
    if(atkleft<0):
        print("Error on _fq5's calculation, if make sure it's completely exist cat uid and stage, please report")
    raw = raw.replace("_fq5",(str(round(atkleft/30,2))+"秒" ))
    print("收招:"+str(atkleft))
    str6 = ""
    if(arrange2!=0):
        if(arrange3>=0):
            str6 = str6 + "遠方"
        else:
            str6 = str6 + "全方"
    if(sing==0):
        str6 = str6 + "單體"
    else:
        str6 = str6 + "範圍"
    raw = raw.replace("_sing ",str6)
    raw = raw.replace("_pr1",str(price))
    raw = raw.replace("_pr2",str(int(price*1.5)))
    raw = raw.replace("_pr3",str(int(price*2)))
    #print(temp[0][0])
    #print(temp[0][3])
    #fio.close()


    #Construct Special Ability.
    colortemplate = stri.replace('Temp11','')
    colortemplate = colortemplate.replace('Temp12','')
    colortemplate = colortemplate.replace('Temp13','')
    colortemplate = colortemplate.replace('\n','')
    print(colortemplate)
    SPAbility = ""
    SPAbility = SPAbility + ma.MultiAtk(doAtk1Aff,doAtk2Aff,doAtk3Aff,atk1,atk2,atk3)
    if(existColor):
        if(doGoodAt):   
            SPAbility = SPAbility + "對"+colortemplate+"屬性的敵人傷害傷害1.5倍(1.8倍)\n"
            SPAbility = SPAbility + "受到"+colortemplate+"屬性的敵人傷害減少50%(60%)\n"
        if(doSuperDmg):
            SPAbility = SPAbility + "對"+colortemplate+"屬性敵人造成3倍(4倍)傷害\n"
        if(doSuperHealth):
            SPAbility = SPAbility + "受到"+colortemplate+"屬性敵人攻擊的傷害減至1/4(1/5)\n"
        if(doUltraDmg):
            SPAbility = SPAbility + "對"+colortemplate+"屬性敵人造成5倍(6倍)傷害\n"
        if(doUltraHealth):
            SPAbility = SPAbility + "受到"+colortemplate+"屬性敵人攻擊的傷害減至1/6(1/7)\n"
        if(doSlow):
            SPAbility = SPAbility + str(doSlow)+"%機率緩速"+colortemplate+"屬性的敵人"+str(round(doSlow2/30,2))+"秒("+str(round(doSlow2*1.2/30,2))+"秒)\n"
        if(doPush):
            SPAbility = SPAbility + str(doPush)+"%機率擊退"+colortemplate+"屬性的敵人\n"
        if(doStop):
            SPAbility = SPAbility + str(doStop)+"%機率暫停"+colortemplate+"屬性的敵人"+str(round(doStop2/30,2))+"秒("+str(round(doStop2*1.2/30,2))+"秒)\n"
        if(doLowAtk):
            SPAbility = SPAbility + str(doLowAtk)+"%機率降低"+colortemplate+"屬性的敵人攻擊力"+str(doLowAtk3)+"% "+str(round(doLowAtk2/30,2))+"秒("+str(round(doLowAtk2*1.2/30,2))+"秒)\n"
        if(doOnlyAttack):
            SPAbility = SPAbility + "只能攻擊"+colortemplate+"屬性的敵人\n"
        if(doCurse):
            SPAbility = SPAbility + str(doCurse) +"%機率詛咒"+colortemplate+"屬性的敵人"+str(round(doCurse2/30,2))+"秒("+str(round(doCurse2*1.2/30,2))+"秒)\n"
        if(doImAtk):
            SPAbility = SPAbility + "受到"+colortemplate+"屬性敵人的攻擊時"+str(doImAtk)+"%機率發動攻擊無效"+str(round(doImAtk2/30,1))+"秒("+str(round(doImAtk2*1.2/30,1))+"秒)\n"
    if(arrange2!=0):
        if(arrange3>=0):
            SPAbility = SPAbility + "遠方攻擊\n"
        else:
            SPAbility = SPAbility + "全方位攻擊\n"
    if(doCri>0):
        SPAbility = SPAbility + str(doCri) + "%機率使出會心一擊\n"
    if(doCriEx>0):
        SPAbility = SPAbility + str(doCriEx) + "%機率使出"+str(doCriEx2+100)+"%渾身一擊\n"
    if(doAtkTime==1):
        SPAbility = SPAbility + "一回攻擊\n"
    if(inter1==0):
        SPAbility = SPAbility + "擊退反擊\n"
    if(ulwave):
        SPAbility = SPAbility + str(ulwave) + "%機率放出Lv"+str(ulwave_num)+"烈波(出現位置"+str(int(ulwave_dist/4))+"~"+str(int((ulwave_dist+ulwave_range)/4))+")\n"
    if(doWave):
        if(doSmallWave):
            SPAbility = SPAbility + str(doWave) + "%機率放出Lv"+str(doWave2)+"小波動\n"
        else:
            SPAbility = SPAbility + str(doWave) + "%機率放出Lv"+str(doWave2)+"波動\n"
    if(doPowerUp):
        SPAbility = SPAbility + "血量"+str(doPowerUp)+"%以下攻擊力"+str(round(1+doPowerUp2/100,2))+"倍\n"
    if(doCastleDmg):
        SPAbility = SPAbility + "善於攻城(4倍傷害)\n"
    if(doDoubleMoney):
        SPAbility = SPAbility + "擊倒敵人獲得兩倍金錢\n"
    if(doReborn):
        SPAbility = SPAbility + str(doReborn)+"%機率以1血存活一次\n"
    if(doImWave):
        SPAbility = SPAbility + "波動無效\n"
    if(doStopWave):
        SPAbility = SPAbility + "波動滅止\n"
    if(doImUlwave):
        SPAbility = SPAbility + "烈波無效\n"
    if(doImPoison):
        SPAbility = SPAbility + "毒擊無效\n"
    if(doImPush):
        SPAbility = SPAbility + "擊退無效\n"
    if(doImStop):
        SPAbility = SPAbility + "暫停無效\n"
    if(doImSlow):
        SPAbility = SPAbility + "緩速無效\n"
    if(doImAtkDown):
        SPAbility = SPAbility + "降攻無效\n"
    if(doImTeleport):
        SPAbility = SPAbility + "傳送無效\n"
    if(doImCurse):
        SPAbility = SPAbility + "詛咒無效\n"
    if(isZombieKiller):
        SPAbility = SPAbility + "殭屍殺手\n"
    if(isWitchKiller):
        SPAbility = SPAbility + "魔女殺手\n"
    if(isEvaKiller):
        SPAbility = SPAbility + "EVA殺手\n"
    print(SPAbility)
    if(config['DEFAULT']['withimage']=='1'):
        import imgdrawer
        SPAbility=imgdrawer.imgdrawer(SPAbility,colortemplate,config)
    print(SPAbility)

    raw = raw.replace("_AB1",SPAbility)
    dynname = int(config['DEFAULT']['UIDSaveFileName'])
    savefilename = 'out.txt'
    if(not dynname):
        savefilename = config['DEFAULT']['DefaultOutputFileName']
    else:
        savefilename = str(uid)+"_"+str(stage)+'.txt'


    f = open(savefilename, 'w',encoding="utf-8")
    f.write(raw)
    f.close();
    print("Done!")
    return 'true'
