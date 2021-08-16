import numpy as np
import csv
import Animation_Length as ani
##--------Constant Define------
uid = 620
#334 黑獸 size = 55, all larger than 55 have to have try protection
#442 黑傑
#270 皇獸
#319 白無垢 #381白傑
stage = 1;  #0 = stage1, 1 = stage2, 2 = stage3
##--------End Constant Define---
##POS
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

print(raw);
f.close();

#f = open(filename,'r',encoding="utf-8")
source=np.loadtxt(filename,dtype=np.str,delimiter=',',encoding="utf-8")
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
try:
    atk2= int(source[stage][59])
    atk3= int(source[stage][60])
    atk = atk1 + atk2 + atk3
    inter22 = int(source[stage][61])
    inter23 = int(source[stage][62])
    inter24 = inter21+inter22+inter23
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
    
if(doRed+doFloat+doBlack+doIron+doWhite+doAngel+doAlien+doUnded>0):
    existColor = True;
#Ability Calculation
doGoodAt = int(source[stage][23])   #善於攻擊
doSuperDmg = int(source[stage][30]) #超大傷害
doSuperHealth = int(source[stage][29]) #很耐打
doCastleDmg = int(source[stage][34]) #擅攻城
doWave = int(source[stage][35]) #波動%
doWave2 = int(source[stage][36])#波動段數
doPowerUp = int(source[stage][40]) #體降升攻體力門檻%
doPowerUp2 = int(source[stage][41]) #體降生攻%
doCri = int(source[stage][31]) #爆擊%
doUltraDmg = 0
doUltraHealth = 0
doCriEx = 0
doCriEx2 = 0
try:
    doUltraDmg = int(source[stage][81]) #極度傷害 #UR
    doUltraHealth = int(source[stage][80]) #極度耐打 #UR
    doCriEx = int(source[stage][82]) #渾身機率
    doCriEx2 = int(source[stage][83])#渾身倍率
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
curse = 0
curse2 = 0
try:
    curse = int(source[stage][92]) #詛咒機率
    curse2 = int(source[stage][93]) #詛咒時長

except:
    print("This cat is older than 9.8, not exist curse-relative def")
doSmallWave = 0
try:
    doSmallWave = int(source[stage][94])
except:
    print("This cat is older than 10.1, not exist small-wave")

#These not affect dmg or health
doStop = int(source[stage][25])  #暫停
doStop2 = int(source[stage][26]) #暫停時間
doSlow = int(source[stage][27]) #緩速
doSlow2 = int(source[stage][28]) #緩速時間
doSelfIron = int(source[stage][43]) #鋼鐵屬性
doLowAtk = int(source[stage][38]) #降攻%
doLowAtk2 = int(source[stage][39])#降攻時間
doLowAtk3 = int(source[stage][40])#降攻比例


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


##-----------
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
#    if(doU==1):
#        stri = stri + "紅"
    if(doUnded==1):
        stri = stri + "屍"
    existColor_G = bool(doRed+doFloat+doBlack+doIron+doAngel+doUnded)
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
    print(stri)


#Fill Atk Blenks
#1 Atk
if(not(doGoodAt==1 or doSuperDmg==1 or doUltraDmg==1)): #Check if need the Tempalte or not
    str1 = "Temp11"
else:
    str1 = stri;
i = 0
ansval = 1.0
for i in range(0,7):
    if(i<5):
        cst = 5 * i + 7
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
        cst = 5 * i + 7
        tempstr = "_hp."+str(i+1);
    else:
        cst = 0.5
        tempstr = "_hp.6";
    str2 = str1
  #  print(str2)
    str2 = str2.replace("Temp11", str(int(hp*cst)))
    if(doGoodAt):
        if(existColor_G):
            ansval = int(round(hp*cst*(1/0.5)))
            str2 = str2.replace("Temp12",str(ansval))
        if(existColor_N):
            ansval = int(round(hp*cst*(1/0.4)))
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
        cst = 5 * i + 7
        tempstr = "_hd."+str(i+1);
    else:
        cst = 0.5
        tempstr = "_hd.6";
    str2 = str1
 #   print(str2)
    str2 = str2.replace("Temp11", str(int(hp*cst/kb)))
    if(doGoodAt):
        if(existColor_G):
            ansval = int(round(hp*cst*(1/0.5)/kb))
            str2 = str2.replace("Temp12",str(ansval))
        if(existColor_N):
            ansval = int(round(hp*cst*(1/0.4)/kb))
            str2 = str2.replace("Temp13",str(ansval))
    if(doSuperHealth):
        if(existColor_G):
            ansval = int(round(hp*cst*5)/kb)
            str2 = str2.replace("Temp12",str(ansval))
        if(existColor_N):
            ansval = int(round(hp*cst*4)/kb)
            str2 = str2.replace("Temp13",str(ansval))
    if(doSuperHealth):
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
atkfq = max(atk_anil+1,inter1*2+inter24-1)
print("atkfq=")
print(atkfq)
atkfq = atkfq / 30
print(atkfq)
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
atk = (1+(doCri/100)*(1+doCriEx2*(doCri/100)))*atk
print(atk)
if(not(doGoodAt==1 or doSuperDmg==1 or doUltraDmg==1)): #Check if need the Tempalte or not
    str1 = "Temp11"
else:
    str1 = stri;
i = 0
for i in range(0,7):
    if(i<5):
        cst = 5 * i + 7
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
        ansval = int(round(atk*cst/atkfq,rdpoint))
    else:
        ansval = round(atk*cst/atkfq,rdpoint)
    str2 = str2.replace("Temp11", str(ansval))
    if(doGoodAt):
        if(existColor_G):
            if not rdpoint:
                ansval = int(round(atk*cst*1.8/atkfq,rdpoint))
            else:
                ansval = round(atk*cst*1.8/atkfq,rdpoint)
            str2 = str2.replace("Temp12", str(ansval))
        if(existColor_N):
            if not rdpoint:
                ansval = int(round(atk*cst*1.5/atkfq,rdpoint))
            else:
                ansval = round(atk*cst*1.5/atkfq,rdpoint)
            str2 = str2.replace("Temp13", str(ansval))
    if(doSuperDmg):
        if(existColor_G):
            if not rdpoint:
                ansval = int(round(atk*cst*4/atkfq,rdpoint))
            else:
                ansval = round(atk*cst*4/atkfq,rdpoint)
            str2 = str2.replace("Temp12", str(ansval))
        if(existColor_N):   
            if not rdpoint:
                ansval = int(round(atk*cst*3/atkfq,rdpoint))
            else:
                ansval = round(atk*cst*3/atkfq,rdpoint)
            str2 = str2.replace("Temp13", str(ansval))
    if(doUltraDmg):
        if(existColor_G):
            if not rdpoint:
                ansval = int(round(atk*cst*6/atkfq,rdpoint))
            else:
                ansval = round(atk*cst*4/atkfq,rdpoint)
            str2 = str2.replace("Temp12", str(ansval))
        if(existColor_N):   
            if not rdpoint:
                ansval = int(round(atk*cst*5/atkfq,rdpoint))
            else:
                ansval = round(atk*cst*3/atkfq,rdpoint)
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

str4 = str4 + "秒"
raw = raw.replace("_fq2",str4) #出招時間

raw = raw.replace("_fq1",str(round(atkfq,2))) #攻擊頻率
raw = raw.replace("_fq4",str(round((regen*2-254)/30,2))) #再生產

str7 = str(arange)
if(arrange2==0):
    str7 = str(arange)
else:
    str7 = "接觸點"+str(arange)+'\n'+"範圍"+str(arrange2)+"~"+str(arrange2+arrange3)
raw = raw.replace("_range",str7)
raw = raw.replace("_speed",str(speed))
raw = raw.replace("_KB",str(kb))
str6 = ""
if(arrange2!=0):
    str6 = str6 + "遠方"
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
doCri = int(source[stage][31]) #爆擊%
doUltraDmg = 0
doUltraHealth = 0
doCriEx = 0
doCriEx2 = 0
SPAbility = ""
if(existColor):
    if(doGoodAt):   
        SPAbility = SPAbility + "對"+colortemplate+"屬性的敵人傷害傷害1.5倍(1.8倍)\n"
        SPAbility = SPAbility + "受到"+colortemplate+"屬性的敵人傷害減少50%(60%)\n"
    if(doSuperDmg):
        SPAbility = SPAbility + "對"+colortemplate+"屬性敵人造成3倍(4倍)傷害\n"
    if(doSuperHealth):
        SPAbility = SPAbility + "受到"+colortemplate+"屬性敵人攻擊的傷害減至1/4(1/5)"

if(doCri>0):
    SPAbility = SPAbility + str(doCri) + "%機率使出會心一擊\n"
if(doCriEx>0):
    SPAbility = SPAbility + str(doCriEx) + "%機率使出"+str(doCriEx2)+"%渾身一擊\n"
if(doSmallWave):
    SPAbility = SPAbility + "小波動\n"
if(doImWave):
    SPAbility = SPAbility + "波動無效\n"
if(doStopWave):
    SPAbility = SPAbility + "波動滅止\n"
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

raw = raw.replace("_AB1",SPAbility)
f = open('out.txt', 'w',encoding="utf-8")
f.write(raw)
f.close();
