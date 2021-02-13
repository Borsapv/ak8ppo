Cíl
Vytvořit aplikaci pro tajemníka ústavu, která bude sloužit k řízení úvazků zaměstnanců.

1) Vytvořit kartu studijního plánu s jednotlivými předměty
    
2) Vytvořit kartu zaměstnance

3) Vytvořit kartu studijní skupiny

4) Propojení předmětů a studijních skupin = štítek 

5) Přiřazení zaměstnanců ke štítkům
    Musí být pokryta hodinová dotace na jednotlivé předměty (musí to někdo odučit), současně musí být pohlídáno, že zaměstnanci učí celkově počet hodin dle svého úvazku. (500b = 100%)
    
    
Modely 
1) Studijní plány
    - Zobrazí formulář s poli, tlačítko save ... 
    - Do pole Studijní plán načte již zadané studijní plány s možností výběru.
    - Další zadané údaje uloží po stistku save do databáze jako jednotlivé předměty (povinné, nepovinné pole?) a přiřadí je ke zvolenému plánu. 
    - Pokud plán neexistuje, vytvoří se v db nový záznam. 

    
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
    
    
Databáze
    - tabulka studijních plánů
    - tabulka studijních oborů
    - tabulka předmětů
    - tabulka zaměstnanců
    - tabulka počtů studentů