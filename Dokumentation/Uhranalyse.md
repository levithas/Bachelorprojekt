Vergleich zwischen Garmin Venu 3 und BangleJS 2

CPU: 1500MHz			64MHz 
Internal Storage: 8GB		256kB RAM, 1MB flash (8MB external)


Schlaftracking:
Die Venu 3 analysiert den Schlaf direkt nach dem Aufstehen. Es wird einem ein Verlauf über die Nacht mit Schlaf und Wachphasen angezeigt. Die Daten werden dann später auf die App übertragen.

Für die BangleJS wäre es sinnvoller, wenn nur die Sensordaten gespeichert werden und die Schlafphasenanalyse auf der Companion-App berechnet wird.
Nachteil hier wäre, dass die Uhr einen nicht in einer Schlafphase wecken kann, da diese erst hinterher ermittelt werden.

Am besten sollte ein sehr kleines LSTM-Modell auf den Daten der Garmin trainiert werden und geprüft werden, ob es überhaupt möglich ist bei der begrenzten Speichergröße ein ausreichendes Modell zu erhalten.

