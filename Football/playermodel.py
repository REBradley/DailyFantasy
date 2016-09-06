class stat(object):
    def __init__(self, stat, coeff):
        self.stat = stat
        self.coeff = coeff
    def pts(self):
        return self.stat*self.coeff


class NflPlayer(object):
    """
    Model of the actors within a Fantasy Football lineup.
    """
    def __init__(self, name=None, position=None, team=None, salary=None, *args, **kwargs):
        self.name = name
        self.position = position
        self.team = team
        self.salary = salary
    
        #Offense and Special Teams
        self.rushyards = stat(0, 0.1)
        self.rushTD = stat(0, 6)
        self.passyards = stat(0, 0.04)
        self.passTD = stat(0, 4)
        self.INT = stat(0, -1)
        self.recyards = stat(0, 0.1)
        self.recTD = stat(0, 6)
        self.rec = stat(0, 0.5)
        self.kotd = stat(0, 6)
        self.prtd = stat(0, 6)
        self.fumlst = stat(0, -2)
        self.fumrecTD = stat(0, 6)
        self.twoptconvscor = stat(0, 2)
        self.twoptconpass = stat(0, 2)
        self.fg19 = stat(0, 3)
        self.fg29 = stat(0, 3)
        self.fg39 = stat(0, 3)
        self.fg49 = stat(0, 4)
        self.fg50 = stat(0, 5)
        self.XP = stat(0, 1)
        
        #Defense
        self.sack = stat(0, 1)
        self.fumrec = stat(0, 2)
        self.defTD = stat(0, 6)
        self.xpret = stat(0, 2)
        self.safety = stat(0, 2)
        self.block = stat(0, 2)
        self.dint = stat(0, 2)
        self.panot = stat(0, 10)
        self.pasix = stat(0, 7)
        self.pathirteen = stat(0, 4)
        self.patwenty = stat(0, 1)
        self.pathirtyfour = stat(0, -1)
        self.pamax = stat(0, -4)
    
    def fantasy_points(self):
        total_score = (self.rushyards.pts() + self.rushTD.pts() + self.passyards.pts()
                        + self.passTD.pts() + self.INT.pts() + self.recyards.pts()
                        + self.recTD.pts() + self.rec.pts() + self.kotd.pts() + self.prtd.pts()
                        + self.fumlst.pts() + self.fumrecTD.pts() + self.twoptconvscor.pts()
                        + self.twoptconpass.pts() + self.fg19.pts() + self.fg29.pts() + self.fg39.pts()
                        + self.fg49.pts() + self.fg50.pts() + self.XP.pts() + self.sack.pts() + self.fumrec.pts()
                        + self.defTD.pts() + self.xpret.pts() + self.safety.pts() + self.block.pts()
                        + self.dint.pts() + self.panot.pts() + self.pasix.pts() + self.pathirteen.pts()
                        + self.patwenty.pts() + self.pathirtyfour.pts() + self.pamax.pts())
        return total_score


    @property
    def scoring_vector(self):






