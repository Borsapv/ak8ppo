Modely 
1) Studijní plány
    - Zobrazí formulář s poli, tlačítko save ... 
    - Do pole Studijní plán načte již zadané studijní plány a obory s možností výběru. Po výběru plánu se dofiltrují dostupné obory. 
    - Další zadané údaje uloží po stistku save do databáze jako jednotlivé předměty (povinné, nepovinné pole?) a přiřadí je ke zvolenému plánu. 
    - Pokud plán nebo obor neexistuje, vytvoří se v db nový záznam.  

    
2) Zaměstnanci
    - Zobrazí formulář s poli, tlačítko save ... 
    - Zadané údaje uloží po kliku na save do databáze

3) Počty studentů
    - Načte se z db tabulka, co řádek, to studijní obor, ve sloupcích formulář pro zadávání
    - U jednotlivých oborů se vyplní v rámci semestrů počty studentů v daném ročníku.
    - Uložení do databáze
    
4) Úvazkový list A
    - Zobrazení formuláře s výběrem zaměstnance
    
5) Úvazkový list B
    - Načtení tabulky z databáze s již přiřazenými předměty (pokud nějaké jsou)
    - součty hodin (bodů) výuky
    - kontrola úvazku a počtu přiřazených hodin
    - Načtení volných předmětů 
    - přiřazení volného předmětu k zaměstnanci
    - odebrání předmětu 
    
    
Databáze (nebo XML)
    - tabulka studijních plánů
    - tabulka studijních oborů
    - tabulka předmětů
    - tabulka zaměstnanců
    - tabulka počtů studentů 
