class Search:
    def __init__(self, Usn=" ", Pass=" "):
        self.Usn = Usn
        self.Pass = Pass

    def GetUsn(self):
        return self.Usn
    def SetUsn(self, Usn):
        self.Usn = Usn

    def GetPass(self):
        return self.Pass
    def SetPass(self, Pass):
        self.Pass = Pass

    def __str__(self):
        return "USN: {0}\nPass: {1}\n".format(self.Usn, self.Pass)
