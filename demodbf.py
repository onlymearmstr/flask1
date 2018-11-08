#coding=utf-8
from dbfpy import dbf
s=["老鹰","绿军","山猫","公牛","骑士","小牛","掘金","活塞","勇士","火箭","步行者","快船","湖人","灰熊","热火","雄鹿","狼","篮网","鹈鹕","纽约","魔术","76人","太阳","开拓者", "国王", "马刺", "雷霆", "猛龙", "爵士", "奇才", "51 自由球队", "playerid", "fname", "name", "overallrtg", "fgpbase", "threeptbas", "ftpbase", "dshootrang", "threeptatt", "dnkability", "dunkpack", "insidesc", "jump", "stlability", "blkability", "oreability", "dreability", "balability", "speed", "quick", "dribble", "dstrength", "fatigue", "offability", "defability", "dhardy", "primacy", "height", "weight", "bodytype", "muscletext", "hand", "team", "球员id", "姓", "名", "价值", "中投", "三分", "罚球", "射程", "三分姿势", "扣篮", "扣篮花样", "内线", "弹跳", "抢断", "盖帽", "前场篮板", "后场篮板", "传球", "速度", "敏捷", "运球", "力量", "体力", "进攻意识", "防守意识", "积极性", "重要性", "身高", "体重", "体型", "肌肉", "惯用手", "球队","LY","LJ","SM","GN","QS","XN","JJ","HS","YS","HJ","BXZ","KC","HR","HX","RH","XL","L","LW","TH","NY","MS","76R","TH","KTZ","GW","MC","LT","ML","JS","QC"]

def demo1():
    db = dbf.Dbf("./up/players.dbf",readOnly=1)
    a=""
    for row in db:
        a=a+"<tr>"
        a = a + "<td>" + row["FNAME"] + "</td>"
        a = a + "<td>" + row["NAME"] + "</td>"
        for i in range(35, 58):
            xm=s[i]
            zhi=row[xm]
            a = a +"<td>"+ bytes(zhi)+"</td>"
            a = a + "<td>" + bytes(row["HAND"]) + "</td>"
            a = a + "<td>" + bytes(row["TEAM"]) + "</td>"
        a = a +"</tr>"
    return a




if __name__ == '__main__':
    for i in range(32,64):
        s[i]=s[i].upper()
    #print s[32]
    print demo1()