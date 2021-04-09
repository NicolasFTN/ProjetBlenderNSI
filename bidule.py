class Processus:
    def __init__(self,duree,moment,priorite):
        self.moment = moment
        self.duree = duree
        self.etat = "prêt"
        self.chrono = 0
        
    def set_etat(self, etat):
        self.etat = etat
        
    def set_priorite(self, priorite):
        self.priorite = priorite
        
    def terminer(self, moment):
        self.chrono += 1
        if self.duree == self.chrono:
            self.etat = "terminer"
            
    def bloqué(self,duree):
        if self.duree == 0
        self.etat = "bloqué"
        
    

