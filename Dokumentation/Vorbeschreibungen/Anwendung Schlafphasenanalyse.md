### Erstellung des KI-Modells

In diesem Kapitel wird der gesamte Prozess der Erstellung des KI-Modells für die Schlafphasenanalyse anhand von Smartwatch-Daten detailliert beschrieben. Das Modell wurde mithilfe von Python und TensorFlow entwickelt, um auf Grundlage von Smartwatch-Daten Schlafphasen zu erkennen und zu klassifizieren. Der Prozess umfasst mehrere Schritte, angefangen bei der Datenerhebung, über die Datenvorverarbeitung und die Definition des Modells, bis hin zum Training und der abschließenden Evaluierung.

\subsection{Datenerhebung}

Für die Aufzeichnung der Daten wurde eine Garmin-Smartwatch über mehrere Nächte getragen. Es handelt sich hierbei um die Garmin Venu-3. Sie ist unter anderem ausgestattet mit Beschleundigungs und Herzfrequenzssensoren. Die Werte dieser Sensoren sowie eine Vorhersage der aktuellen Schlafphase lassen sich über die Webseite von Garmin abrufen. Es gibt jedoch keinen direkte Download oder Export Funktion um die Daten zu erhalten. Eine Untersuchung der Webseite über die browser-interne Netzwerkanalyse zeigt jedoch einen Aufruf eines REST-Services, welcher die benötigten Daten enthält. Über ein Python-Skript wurde dieser Aufruf mittels Curl modifiziert, so dass die Daten manuell abgefragt und gesammelt werden können.


\subsection{Datenaufbereitung}

Die Rohdaten sind nun vorhanden und müssen für die weitere Verwendung aufbereitet werden. So muss zum Beispiel der Zeitindex angepasst werden, da dieser Relativ auf einen gegebenen Wert gesetzt wurde. Außerdem werden die Bewegungsdaten und Herzschlagdaten auf einen gemeinsamen Zeitindex gemapped. Die aufbereiteten Daten werden als JSON-Datei abgelegt um sie für das Training einfach wieder abrufbar zu haben.

\subsection{Modelldefinition}

Es wird nun die Struktur des KI-Modells beschrieben, das für die Schlafphasenanalyse auf Basis der Smartwatch-Daten verwendet wird. Für dieses Projekt wurde ein Modell auf Basis von Long Short-Term Memory (LSTM)-Netzwerken entwickelt, da diese Architektur besonders gut geeignet ist, um zeitabhängige Daten wie die Schlafphasen zu verarbeiten \cite{hochreiterLongShorttermMemory1997}. LSTM-Netzwerke sind in der Lage, langfristige Abhängigkeiten in den Daten zu lernen, was sie ideal für die Analyse von Zeitreihen, wie sie bei der Schlafüberwachung auftreten, macht. Es werden sowohl die Architektur des Modells als auch die spezifischen TensorFlow-Komponenten erläutert, die zur Implementierung des Modells verwendet wurden.

\subsubsection{Modellstruktur}

Es wurde die Klasse \textit{TimeSeriesLSTM} entwickelt um die Modellstruktur zu kapseln und die wichtigsten Prozesse, wie die Datenvorverarbeitung, das Modelltraining sowie die Modellvorhersage zu steuern. Über die Datenstruktur \textit{LSTMConfig} lassen sich Hyperparameter des Modells definieren, wie die Anzahl der Zeitschritte, auf die das Modell pro Berechnungsschritt zurückgreifen soll (n_steps), die Batch-Größe, in welcher das Modell trainiert wird und die Anzahl der Epochen für das Training. 

\item{itemize}

\end{itemize}