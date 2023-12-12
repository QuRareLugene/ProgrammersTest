def solution(bandage, health, attacks):
    CurHealth = health
    MaxHealth = health
    AtkCount = 0
    bonus = 0

    for sec in range(attacks[-1][0]+1):
        if(sec == attacks[AtkCount][0]):
            CurHealth -= attacks[AtkCount][1]
            AtkCount += 1
            bonus = 0
            if CurHealth <= 0:
                return -1
        elif(CurHealth < MaxHealth):
            bonus += 1
            CurHealth += bandage[1]
            if(bonus == bandage[0]):
                CurHealth += bandage[2]
                bonus = 0
            if(CurHealth > MaxHealth):
                CurHealth = MaxHealth
        #print(f'time = {sec} | bonus = {bonus} | CurHealth = {CurHealth}')
                
    return CurHealth