# 🐍 Snake Game in Python

Ein klassisches **Snake-Spiel**, entwickelt in Python unter Verwendung des integrierten `turtle`-Moduls. Dieses Projekt wurde vollständig ohne externe Spiele-Engines umgesetzt, um grundlegende Konzepte der Spieleprogrammierung – wie Game Loops, Kollisionsabfragen, Raster-Bewegung und Frame-basierte Text-Animationen – praktisch anzuwenden.

## ✨ Features

* **Flüssige WASD-Steuerung:** Direkte Richtungswechsel mit integriertem Schutz gegen 180-Grad-Drehungen in den eigenen Körper.
* **Dynamisches Wachstum:** Jedes gefressene Futter-Objekt verlängert die Schlange um ein neues Körpersegment.
* **Schwebende „+1 Point!“-Animation:** Eine Frame-basierte Text-Animation steigt direkt an der Position des gefressenen Futters nach oben auf, ohne den Game Loop zu unterbrechen.
* **Live-Punktestand:** Aktuelle Score-Anzeige am oberen Bildschirmrand.
* **Game Over & Quick-Restart:** Automatische Erkennung von Wand- und Selbstkollisionen inklusive sofortiger Neustart-Funktion per Tastendruck (`R`).

## 🎮 Steuerung

| Taste | Aktion |
| :--- | :--- |
| **W** | Nach oben bewegen |
| **A** | Nach links bewegen |
| **S** | Nach unten bewegen |
| **D** | Nach rechts bewegen |
| **R** | Spiel nach Game Over neu starten |

## 🚀 Installation & Start

Da das Spiel ausschließlich auf Pythons Standardbibliothek (`turtle`, `time`, `random`) basiert, müssen keine zusätzlichen Pakete installiert werden.

1. **Repository klonen:**
   ```bash
   git clone [https://github.com](https://github.com/crysiszockt/Unleash-the-Snake.git)
   cd Unleash-the-Snake
   ```

2. **Spiel starten:**
   ```bash
   python snake.py
   ```
   *(Hinweis: Stelle sicher, dass Python 3 auf deinem System installiert ist und klicke nach dem Start einmal in das Spielfenster, um die Tastatursteuerung zu aktivieren.)*

## 🛠️ Verwendete Technologien

* **Python 3**
* **`turtle`** – Grafikausgabe, Fensterverwaltung und Tastatur-Events
* **`random`** – Zufällige Positionierung des Futters im 20x20-Pixel-Raster
* **`time`** – Steuerung der Spielgeschwindigkeit (Tick-Rate)

## 💡 Mögliche Erweiterungen

* Speichern eines dauerhaften Highscores in einer lokalen Datei
* Steigerung der Geschwindigkeit mit zunehmender Schlangenlänge
* Unterstützung der Pfeiltasten zusätzlich zu WASD
