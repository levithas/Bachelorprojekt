
### Was soll die App tun?

#### Stichpunkte:
- Berechnung der Schlafphasen
	- aus Sensordaten von der Gadgetbridge-App
	- vorbereiten für andere Datenquellen?
- Importieren von Modellen zur Berechnung der Schlafphasen
- Exportieren von Sensordaten und Schlafdaten
- Möglichkeit zum "Spenden" der eigenen Schlafdaten für das Modell-Training
	- Anonymisieren dieser Daten vor dem abschicken
	- (Datenserver?)
- Einfache Visualisierung des Schlafverlaufes
- Es können die Analysen verschiedener Modelle untereinander verglichen werden und man kann (subjektiv) entscheiden, welches Modell am besten zu den eigenen Erfahrungen passt
	- (War ich oft wach? Hab ich erholsam geschlafen? Stimmen die Einschlaf und Aufwach Uhrzeiten?)

#### Use-Cases:
#### Must-Have:

- Verbindung zu Gadgetbridge aufbauen
- Sensordaten Anfrageintervall an die Gadgetbridge einstellen
- Preprocessing der Daten
- Postprocessing des Outputs
- Modell importieren
- Modell Auswahl
- Sensordaten mit ausgewählten Modell verarbeiten
- Schlafdaten anschauen

#### Nice-To-Have:

- Daten zurück zur Gadgetbridge senden (2)
- Schlafdaten verschiedener Modelle vergleichen (2)
- Modelle bewerten (3)
- Schlafdaten anonymisiert publizieren (Zur Verwendung in Trainings) (3)
	- Datenserver müsste aufgesetzt werden (InfluxDB?, S3-Bucket?, Github?, Huggingface?)


#### NICHT-Ziele:

- Direkte Verbindung zur Smartwatch
- Smartwatch und Gadgetbridge dienen alleine der Datenerfassung
- Nicht das beste Machine Learning Modell, sondern nur Baseline



## Notizen:
- Unterschied Liveverarbeitung zu Batchverarbeitung
- 


### Warum eine eigene App?

- Flexiblerer Umgang mit Berechtigungen (z.B. Netzwerk/Internet)
- Mehr Freiheit in der Gestaltung des Nutzerinterface
	- Kein Bruch im Design nötig
- Programmstruktur kann verbessert werden
	- Softwarearchitektur, Design-Pattern, Sprache
		- Kotlin und Jetpack Composables
- Geringere Komplexität
- Eine bessere Erfahrung für mich, da etwas komplett eigenes Entwickelt wird

- Die App soll eine Basis bilden für weitere Entwicklungen im Bereich der Schlafphasenanalyse
	- Modell-Training auf dem Smartphone?
	- Unsupervised Learning?
	- Manuelles Labeling?
	- Vergleich von Modellen


Nachteil:
- Es muss dennoch die Gadgetbridge-App modifiziert werden um eine Kommunikation mit der neuen App zu ermöglichen
- Durch die unflexible Struktur der Gadgetbridge-App muss für JEDES Uhr-Modell eine eigene Anpassung geschrieben werden
	- Vorerst nur für BangleJS und Garmin


### Zusätzlich zur App-Entwicklung

- Python-Code zum/zur:
	- Datengewinnung von der Garmin-Webseite
	- Aufbereitung von Datensätzen für das Training
	- Laden, Trainieren, Speichern und Konvertieren für die Mobile Nutzung



# Aufwandsabschätzung:

#### App-Konnektivität mit Gadgetbridge (1,5 Wochen) (max. + 0,5 Woche)
- Ausarbeitung der Daten, welche über die Schnittstelle transferiert werden müssen
- Konzeption der Schnittstelle
- Implementierung der Schnittstelle
- Dokumentation des Prozesses

#### App-Modell-Management (2 Wochen) (max. + 1 Woche)
- Use-Cases in Klassenstrukturen und Schnittstellen umsetzen
- Implementierung der Klassen und Schnittstellen + Tests
- Dokumentation des Prozesses

#### App-Design (1,5 Wochen) (max. + 1 Woche)
- UI/UX definieren
	- Wie wird die App bedient usw.
- Mockups erstellen
	- Veranschaulichung und Festlegung des Designs
- Design implementieren
	- Umsetzen des Designs in Code
- Dokumentation des Prozesses

#### Modell-Implementierung (1 Wochen) (max. +0,5 Woche)
- Datenaufbereitung
- Modell-Training
- Modell-Evaluation
- Dokumentation des Prozesses und der Tools

#### Datensammlung (findet währenddessen statt)