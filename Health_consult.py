from requests import get
from bs4 import BeautifulSoup as bts
from googlesearch import search


class HealthConsultation:
    def __init__(self):
        self.author = "Rigeru"
        self.website = "website:halodoc.com"
        self.parser = "html.parser"
        self.lang = "id"
        self.index = "String"
        self.num_result = 10 
        
    def SearchKey(self):
         self.key = input("What do you want to search for: ")
         
    def GoogleSearch(self):
        self.list, generator = [], search(f"{self.key} gejala {self.website}", num_results=self.num_result, lang=self.lang)
        for link in generator:
            self.list.append(link)
    
    def ParseResult(self):
        self.result = []
        for link in self.list:
            a = get(link)
            parsed = bts(a.text, self.parser)
            self.result.append(parsed)
        
    def TitleShow(self):
        print("These are the title that matches your keywords")
        for x in range(self.num_result):
            title = self.result[x].title.get_text().split('-')[0]
            print(f"    {x+1} ~ {title}")
        
    def InputResult(self):
        while type(self.index) != "int" and self.index != 0:
            try:
                self.index = int(input("Which title do you want to seek to?\nIndex : ")) - 1
                break
            except:
                pass
            print("\n\nPlease input only integers")
    
    def IndexResult(self):
        
        # Reviewer Name
        Reviewed = self.result[self.index].find('a', class_="article__reviewer--name")
        if type(Reviewed) == 'NoneType': Reviewed = self.result[self.index].find('a', class_="article__reviewer--name ng-star-inserted")
        print("\n\n\n\n\n\n\n\n\n\n\n")
        print(f"Result Reviewed By: {Reviewed.string}\n")

        # All the H2's , texts
        for h2 in self.result[self.index].find_all('h2'):
            if h2.text in ["Topik Terkini", "Artikel Terkait", "Berlangganan Artikel Halodoc", "Konsultasi dengan Ahlinya"]: pass
            else:
                print('# '+h2.text)
                for text in h2.find_next_siblings():
                    if text.name == 'h2':
                        print('\n---------------\n')
                        break
                    else:
                        if text.get_text(strip=True) == "Referensi:": print()
                        print(text.get_text(strip=True))
                    
    def BrainProgram(self):
        self.SearchKey()
        self.GoogleSearch()
        self.ParseResult()
        while True:
            self.TitleShow()
            self.InputResult()
            self.IndexResult()
 
if __name__ == '__main__':
    H = HealthConsultation()
    H.BrainProgram()
