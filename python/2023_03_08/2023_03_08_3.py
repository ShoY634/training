from __future__ import annotations


class Human:
    def __init__(self, age, sex, is_high_face, is_drink):
        self.age = age
        self.sex = sex
        self.is_high_face = is_high_face
        self.is_drink = is_drink
    
    def is_admission_club(self):
        if self.age >= 20:
            is_admited = True
        else:
            is_admited = False
        return is_admited
    
    def select_lady(self, lady: Human):
        if self.is_high_face == True and lady.is_high_face == True:
            is_success = True
            
        elif self.is_high_face == True and lady.is_high_face == False:
            is_success = True
            
        elif self.is_high_face == False and lady.is_high_face == True:
            is_success = False
            
        else:
            is_success = True
            
        return is_success
    
    def go_to_hotel(self, lady: Human):
        if self.is_drink == True and lady.is_drink == True:
            print("２人とも飲みすぎてガチ寝した")
        elif self.is_drink == True and lady.is_drink == False:
            print("勃たずにトラウマになって、以降一生インポになった")
        elif self.is_drink == False and lady.is_drink == True:
            print("始まる前に寝られたから苛つきながら寝てる女の胸もんだ")
        else:
            print("allnightfever")            
    
    def finalresult(self):
        if self.is_admission_club() == False:
            print("セキュリティに兄の免許証借りてんのばれた")
        elif self.select_lady(lady) == False:
            print("ナンパ成功しなかった。ラーメン食って家でしこって寝た")
        else:
            self.go_to_hotel(lady)
    
    
lady = Human(20, "female", True, True)
man = Human(23, "male", True, False)

man.finalresult()
