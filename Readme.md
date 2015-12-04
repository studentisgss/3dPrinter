Stampante 3D
============

Documentazione: [pagina wiki](../../wiki)

Per segnalare malfunzionamenti: [pagina issues](../../issues)

## Script `tools/send.py`

Lo script serve per testare la connessione con la stampante, interagendo in modo interattivo.

Utilizzarlo per inviare comandi [G-code](http://reprap.org/wiki/G-code). Ad esempio:
- `M106 S255` Per accendere la ventola al 100%
- `M106 S127` Per accendere la ventola al 50%
- `M106 S0` Per spegnere la ventola
- `M105` Per leggere la temperatura
- `M112` Per l'arresto di emergenza
