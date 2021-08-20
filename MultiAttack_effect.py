def MultiAtk(doAtk1Aff,doAtk2Aff,doAtk3Aff,atk1,atk2,atk3):
#    return "This is nothing"
    atk = atk1+atk2+atk3
    atk1p = str(round(100 * atk1 / atk,1))
    atk2p = str(round(100 * atk2 / atk,1))
    atk3p = str(round(100 * atk3 / atk,1))
    result = ""
    if(atk2==0): #Exist no Multi Attack
        return ""
    else:
        if(atk3==0): #只有兩段攻擊
            result = "2回連續攻擊(傷害"+atk1p+"%-"+atk2p+"%，"
        else:
            result = "3回連續攻擊(傷害"+atk1p+"%-"+atk2p+"%-"+atk3p+"%，"
        if(doAtk1Aff):
            result = result + "第一擊附加能力/"
        if(doAtk2Aff):
            result = result + "第二擊附加能力/"
        if(doAtk3Aff):
            result = result + "第三擊附加能力"
    result = result + ')\n'
    return result
