# snakepong-wout-felix


## opgave

de opgave was om een snakepong-game te maken, een voorbeeld van deze game is
[hier](https://twitter.com/Pcordemans/status/979060961645678593?s=20)

1. Maak een analyse van het probleem, bedenk welke componenten je allemaal nodig hebt en beschrijf dit in een README.md. Hierbij verwacht ik ook een schema van de code.

2. Deel de code op in de functionele game logic en de weergave. Je mag de weergave beperken tot een print in de console. Je hoeft het spel niet real-time kunnen spelen.

3. Voorzie testen voor de game logic. Je hoeft niet alles te testen.


## Analyse

om de game te maken heb je een paar componenten nodig:

* Een bal
* een paddle
* een snake
* een tail van de snake
* de borders
* de keyboard inputs
* en de main game loop

Het schema van de code ziet er als volgt uit:

![schema](img/Snakepong_Schema.png)

## game logica

de game logica is opgedeeld in een paar klassen zoals weergegeven in het schema hierboven.

## Testen

Er zijn testen voor de Ball klasse voorzien en testen voor de Keyboard klasse die eigenlijk ook de movement bepaald.
