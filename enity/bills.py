class Bill:
    def __init__(self,
                 Id=0,
                 Username='',
                 Type=0,
                 Money=0.0,
                 Time=None,
                 Mes='',
                 Update_at=None):
        self.Id = Id
        self.Username = Username
        self.Type = Type
        self.Money = Money
        self.Time = Time
        self.Mes = Mes
        self.Update_at = Update_at


if __name__ == '__main__':
    a = Bill()
    print(a)
