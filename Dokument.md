# La_1305
# Projekt-Dokumentation

Nicola Karrer, Carina Sutter

| Datum | Version | Zusammenfassung                                              |
| ----- | ------- | ------------------------------------------------------------ |
| 22.05 | 0.0.1   | Anfang vom Snake-game |
| 29.05 | 0.0.2 + 1.0.0   | Basis vom Snake-game gemacht und Pong erstellt |
| 05.06 | 1.0.0 + 1.0.0  | Snake-game verbessert und Tic Tac Toe gemacht |

## 1 Informieren

### 1.1 Ihr Projekt
Wir haben uns vorgenommen, Python kennen zu lernen und haben deshalb für den Start einfache Spiele entwickelt.

### 1.2 User Stories

S = Snakes | P = Pong | T = Tic Tac Toe

| US-№ | Beschreibung                       |
| ---- | ---------------------------------- |
| S1 | Der User kann mit den Pfeilentasten die Schlange steuern|
| S2 | Der User kann Äpfel essen |
| S3 | Wenn der User ein Apfel gegessen hat, wird die Schlange länger |
| S4 | Wenn der User ausversehen in sich selber schleicht, ist das Spiel vorbei |
| S5 | Das Spiel ist vorbei, wenn die Schlange gegen die Wand oder in sich selbst stösst, damit es eine Herausforderung und ein Ende gibt |
| S6 | Es gibt ein Haptmenü, bevor das Spiel startet, damit ich das Spiel starten oder Einstellungen ändern kann |
| S7 | Es gibt eine Punkteanzige, damit ich meinen Fortschritt und meine Leistung mitverfolgen kann|
| S8 | Es gibt eine Möglichkeit, das Spiel zu pausieren und fortzusetzen, damit ich bei Bedarf eine Pause machen kann |
| S9 | Man kann aus verschiedenen Schwierigkeitsgraden wählen (leicht, mittel, schwer), damit ich das Spiel an mein Können anpassen kann |
| P1 | Der erste Spieler kann mit den Tasten W und S seinen Balken bewegen |
| P2 | Der zweite Spieler kann mit den Pfeiltasten seinen Balken nach oben und nach unten bewegen |
| P3 | Der Ball prallt an den Balken und den Wänden ab |
| P4 | Der Ball wird mit jedem Aufprall schneller |
| P5 | Die Tore werden an einer Punkteanzeige angezeigt |
| T1 | Beim start wird ein 3x3 Feld generiert, in dem man Zeichen setzen kann |
| T2 | Der erste Spieler kann ein X in eines der freien Felder setzen |
| T3 | Der zweite Spieler kann ein O in eines der freien Felder setzen |
| T4 | Eine Meldung zeigt an, wer gewonnen hat oder ob es ein Unentschieden ist |
| T5 | Es gibt einen Knopf, mit dem man ein neues Spiel starten kann |

### 1.3 Testfälle

| TC-№ | Ausgangslage | Eingabe | Erwartete Ausgabe |
| ---- | ------------ | ------- | ----------------- |
| S1.A  | Spiel gestartet | Spieler drückt eine Pfeiltaste | Schlange ändert ihre Richtung |
| S2.A  | Spiel gestartet | Spieler isst einen Apfel | Der Apfel verschwindet |
| S3.A  | Spiel gestartet | Spieler isst einen Apfel | Die Schlange wird länger |
| S4.A  | Spiel gestartet | Spieler fährt in sich selbst hinein | Spiel geht zu Ende |
| S5.A  | Spiel gestartet | Spieler fährtin eine Wand | Spiel geht zu Ende |
| S6.A  | Spiel gestartet | - | Hauptmenu wird angezeigt |
| S7.A  | Spiel gestartet | Spieler stirbt | Punkteanzeige zeigt Fortschritt an |
| S8.A  | Spiel gestartet | Pause-Knopf drücken | Spiel wird angehalten |
| S9.A  | Spiel gestartet | Spieler wählt Schwierigkeitsgrad aus | Spiel startet in diesem Schwierigkeitsgrad |
| P1.A  | Spiel gestartet | Spieler drückt W | linker Balken geht nach oben |
| P1.B  | Spiel gestartet | Spieler drückt S | linker Balken geht nach unten |
| P2.A  | Spiel gestartet | Spieler drückt Pfeil nach oben | rechter Balken geht nach oben |
| P2.B  | Spiel gestartet | Spieler drückt Pfeil nach unten | rechter Balken geht nach unten |
| P3.A  | Spiel gestartet | - | Ball prallt ab |
| P4.A  | Spiel gestartet | Ball prallt ab | Ball wird schneller |
| P5.A  | Spiel gestartet | Tor geschossen | Punkteanzeige wird aktualisiert |
| T1.A  | Spiel gestartet | - | 3x3 Feld wird generiert |
| T2.A  | Spiel gestartet | Erster Spieler klickt auf ein Feld | Es wird ein X gesetzt |
| T3.A  | Spiel gestartet | Zweiter Spieler klickt auf ein Feld | Es wird ein O gesetzt |
| T4.A  | Spiel gestartet | Spiel beendet | Endresultat wird angezeigt |
| T5.A  | Spiel beendet | Auf "new game" Knopf gedrückt | Neues Spiel wird gestartet |


## 2 Planen

| AP-№ | Frist | Zuständig | Beschreibung | geplante Zeit |
| ---- | ----- | --------- | ------------ | ------------- |
| S1.1  | 22.05.24 | Carina |                   | 60min |
| S2.1  | 29.05.24 | Carina |                   | 50min |
| S3.1  | 29.05.24 | Carina |                   | 50min |
| S4.1  | 29.05.24 | Carina |                   | 50min |
| S5.1  | 29.05.24 | Carina |                   | 75min |
| S6.1  | 05.06.24 | Carina |                   | 20min |
| S7.1  | 05.06.24 | Carina |                   | 20min |
| S8.1  | 05.06.24 | Carina |                   | 20min |
| S9.1  | 05.06.24 | Carina |                   | 75min |
| P1.1  | 29.05.24 | Nicola |                   | 20min |
| P2.1  | 29.05.24 | Nicola |                   | 20min |
| P3.1  | 29.05.24 | Nicola |                   | 45min |
| P4.1  | 29.05.24 | Nicola |                   | 45min |
| P5.1  | 29.05.24 | Nicola |                   | 30min |
| T1.1  | 05.06.24 | Nicola |                   | 50min |
| T2.1  | 05.06.24 | Nicola |                   | 30min |
| T3.1  | 05.06.24 | Nicola |                   | 30min |
| T4.1  | 05.06.24 | Nicola |                   | 35min |
| T5.1  | 05.06.24 | Nicola |                   | 35min |


## 3 Entscheiden

Wir haben uns dazu entschieden, dass Carina das Snake-game macht und ich das Pong-spiel und Tic Tac Toe, da dass Snake-game bestimmt schwieriger ist.

## 4 Realisieren

| AP-№ | Datum | Zuständig | geplante Zeit | tatsächliche Zeit |
| ---- | ----- | --------- | ------------- | ----------------- |
| S1.1  | 22.05.24 | Carina | 60min | 60min |
| S2.1  | 29.05.24 | Carina | 50min | 50min |
| S3.1  | 29.05.24 | Carina | 50min | 50min |
| S4.1  | 29.05.24 | Carina | 50min | 50min |
| S5.1  | 29.05.24 | Carina | 75min | 75min |
| S6.1  | 05.06.24 | Carina | 20min | 20min |
| S7.1  | 05.06.24 | Carina | 20min | 20min |
| S8.1  | 05.06.24 | Carina | 20min | 20min |
| S9.1  | 05.06.24 | Carina | 75min | 75min |
| P1.1  | 29.05.24 | Nicola | 20min | 20min |
| P2.1  | 29.05.24 | Nicola | 20min | 20min |
| P3.1  | 29.05.24 | Nicola | 45min | 45min |
| P4.1  | 29.05.24 | Nicola | 45min | 45min |
| P5.1  | 29.05.24 | Nicola | 30min | 30min |
| T1.1  | 05.06.24 | Nicola | 50min | 50min |
| T2.1  | 05.06.24 | Nicola | 30min | 30min |
| T3.1  | 05.06.24 | Nicola | 30min | 30min |
| T4.1  | 05.06.24 | Nicola | 35min | 35min |
| T5.1  | 05.06.24 | Nicola | 35min | 35min |


## 5 Kontrollieren

| TC-№ | Datum | Resultat | Tester |
| ---- | ----- | -------- | ------ |
| S1.1  | 12.06.24 |  | Carina |
| S2.1  | 12.06.24 |  | Carina |
| S3.1  | 12.06.24 |  | Carina |
| S4.1  | 12.06.24 |  | Carina |
| S5.1  | 12.06.24 |  | Carina |
| S6.1  | 12.06.24 |  | Carina |
| S7.1  | 12.06.24 |  | Carina |
| S8.1  | 12.06.24 |  | Carina |
| S9.1  | 12.06.24 |  | Carina |
| P1.1  | 12.06.24 |  | Nicola |
| P1.2  | 12.06.24 |  | Nicola |
| P2.1  | 12.06.24 |  | Nicola |
| P2.2  | 12.06.24 |  | Nicola |
| P3.1  | 12.06.24 |  | Nicola |
| P4.1  | 12.06.24 |  | Nicola |
| P5.1  | 12.06.24 |  | Nicola |
| T1.1  | 12.06.24 |  | Nicola |
| T2.1  | 12.06.24 |  | Nicola |
| T3.1  | 12.06.24 |  | Nicola |
| T4.1  | 12.06.24 |  | Nicola |
| T5.1  | 12.06.24 |  | Nicola |


## 6 Auswerten

Das Projekt hat spass gemacht und wir haben viel Neues dazu gelernt. Wir denken auch, dass wir gut gearbeitet haben und diese kurze Zeit einiges schaffen konnten. Viele Schwierigkeiten gab es bei uns nicht und im Team gab es auch keine Probleme.

1.3 Testfälle schreiben
2 Planen Beschreibung
*3 Entscheiden Länger
*4 Realisieren Tatsächliche Zeit
5 Kontrollieren Testen
