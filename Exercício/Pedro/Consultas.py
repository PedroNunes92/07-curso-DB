import MySQLdb

class consulta:

    def __init__(self):
        self.db = MySQLdb.connect(host="127.0.0.1",    
                     user="Pedro",         
                     passwd="admin",  
                     db="Pedro")       
        self.cur = self.db.cursor()


    def SiteVisitas(self):
        self.cur.execute("select site, count(*) from Visited group by site")
        for row in self.cur.fetchall():
            print ("Site ", row[0], " foi visitado", row[1], "vezes.")

    def SiteSemVistas(self):
        self.cur.execute("select site from Visited where site is NULL")
        for row in self.cur.fetchall():
            print ("Esse site não teve visita: ", row[0])

    
    def MetriSurvey(self):
        self.cur.execute("select quant, count(*) from Survey group by quant")
        for row in self.cur.fetchall():
            print ("O ", row[0], " foi observado", row[1], "vezes.")
    
    def LevantPessoas(self):
        self.cur.execute("select person, count(*) from Survey group by person having count(*) > 2 ")
                       
        for row in self.cur.fetchall():
            print (row[0], "fez", row[1], "levantamentos.")

    def sobrenomeDYR(self):
        self.cur.execute("select * from Person where family LIKE '%D%Y%R'")
        for row in self.cur.fetchall():
            print (row[2])
        
    def Visitacoeslista(self):
        site = input("Digite uma lista de sites separados por espaço: ")
        site_lista = site.strip().split()

        for l in site_lista:
            self.cur.execute("select id,site from Visited where site = '%s'" %l)
                            
            for row in self.cur.fetchall():
                print ("id:", row[0],"site:", row[1])

    def ValorNULO(self):
        self.cur.execute("select  count(*) from Survey where (person is NULL) group by person")
        #coloquei person pq tem valores nulos
        for row in self.cur.fetchall():
            print ("Existem", row[0], "linhas com valor nulo.")

    def qntMedicoes(self):
        self.cur.execute("select person,count(*) from Survey group by person")
        for row in self.cur.fetchall():
            print (row[0], "fez", row[1], "medições")
       

obj = consulta()
#obj.SiteVisitas()
#obj.SiteSemVistas()
#obj.MetriSurvey()
#obj.LevantPessoas()
#obj.sobrenomeDYR()
#obj.Visitacoeslista()
#obj.ValorNULO()
#obj.qntMedicoes()
