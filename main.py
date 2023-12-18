class Main:
    def __init__(self):
        self.risuaidat = "#" * 40
        self.rivarit = "\n" * 2
        self.tahdet = "*" * 40
    
        

    def tervehdys(self):
        print("Tervetuloa käyttämään laskurisovellusta!", end=self.rivarit)
        print(
            self.tahdet,
            "     ----------------------------",
            "  ** | (C) Codak Software, 2023 | **",
            "     ----------------------------",
 
            self.tahdet,
       
            sep="\n", end=self.rivarit)
            
        return None
    


def main():
    main = Main()
    main.tervehdys()
    valikko = Valikko()

def ohjelman_lopetus():
    print("Kiitos ohjelman käytöstä!")


if __name__ == "__main__":
    main()




