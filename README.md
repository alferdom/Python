# Hra Snake s A* algoritmem v pyGletu
### Jazyk: Python 3.9 s knihovnou pyGlet

### Popis funkce:

Hra Snake ovládáná pomocí šipek na klávesnici, ESC pro ukončení a Enter pro přepínaní mezi módy obrazovky.
Jde o snězení jablíčka hadem a navýšení tak velikosti hada. 
Aréna je dvojího typu. Defaultně nekonečná, teda had se po přelezení stěny vrátí z protější strany
a po zapnutí je zde neviditelná stěna na konci okna, do které had narazí a hra skončí.

Dále je zde implementovaný základní A* algoritmus pro hledání nejkratší cesty k jablíčku v aktuální pozici, 
jenž se zapíná pomocí přepínače a ruší možnost hada ovládat ručně.


### Návod spuštění:

`python -m SnakePYT [-h] [-s INT] [-v INT] [-f] [--astar] [--wall]`

Do příkazového řádku, nacházející se v adresáři s balíčkem SnakePYT, vložit příkaz python -m SnakePYT -h.
Zobrazí se informační tabulka s případnými volitelnými rožšiřujícími argumenty.
Pro defaultní nastavení hry spustit bez přepínačů a argumentů pomocí python -m SnakePYT.
Pro spuštění hry s A* algoritmem, použíjte přepínač --astar nebo -a.