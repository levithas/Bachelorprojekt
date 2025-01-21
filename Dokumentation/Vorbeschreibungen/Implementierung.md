\chapter{Implementierung}

In diesem Kapitel wird näher auf die Implementierung der besprochenen Strukturen zu einem Gesamtprogramm eingegangen. Zu Beginn werden die grundlegenden Tools vorgestellt, die als Basis für die Anwendung dienen. Es folgt die Systemarchitektur und der strukturelle Aufbau. Danach werden die Frameworks, welche bei der Umsetzung der Implementierungen genutzt werden genauer beleuchtet.

\section{Programmiersprache Kotlin}

Für Android lassen sich Anwendungen in C++, Java und Kotlin entwickeln. Java ist hier die gängigere Programmiersprache, da sie flexibler für unterschiedliche Geräte einsetzbar ist und es eine Vielzahl von verwendtbaren Bibliotheken gibt. Seit dem Jahr 2019 wird von Google, dem Entwickler der Android-Plattform, die Sprache Kotlin als primäre Entwicklungssprache für Android-Anwendungen empfohlen \cite{Google2019Empowering}. Aus diesem Grund wurde diese Sprache für die Umsetzung des Projektes gewählt. Kotlin ist zwar eine eigene Programmiersprache, sie baut jedoch auf der Java Runtime Environment auf. Kotlin-Code lässt sich 1 zu 1 in Java Code transkribieren, wie auch Java Code zurück in Kotlin. Desweiteren können Java-Klassen direkt in das Kotlin-Programm eingebaut werden, was die Kompatibilität mit vorhandenem Code und Bibliotheken erhöht. Als Entwicklungsumgebung wird Android-Studio verwendet. Durch die direkte Integration eines Android-Emulators und der Möglichkeit eine Vorschau der Benutzeroberfläche zu generieren ohne das Programm starten zu müssen, wurde sich für dieses Tool entschieden.

\section{Systemarchitektur}

In \autoref{MVVM} wurde auf die allgemein übliche Struktur von Android-Anwendungen näher eingegangen. Im folgenden wird nun die Implementierung dieser Struktur in dem gegebenen Szenario beschrieben. Das Programm wird in 3 Schichten gegliedert:

- Datenschicht
	Innerhalb dieser Schicht werden...

- Geschäftslogikschicht
		Diese Schicht beinhaltet die auszuführenden Logiken und ....
- Benutzeroberflächenschicht
		In dieser Schicht wird die Oberfläche, welche der Anwender....

\subsection{Model}
Die Aufteilung von Model, View und Viewmodel überschneidet sich teilweise mit diesen 3 Schichten. So gibt es in der Datenschicht die Datenbank-Modelle, welche die Werte und Abhängigkeiten der Tabellen innerhalb der Datenbank beschreiben und zusätzlich in der Geschäftslogik die Domain-Modelle, welche die Datenbank-Entitäten abstrahieren, für eine einfachere Handhabung der Informationen. Beide Elemente lassen sich der Model-Komponente der MVVM-Architektur zuweisen, befinden sich jedoch in unterschiedlichen Schichten. Für einen übersichtlichen Übergang von den Daten-Modellen zu den Domain-Modellen wird ein Repository-Pattern angewendet. Dieses stellt eine Schnittstelle für den Datenzugriff bereit, welcher für alle UseCases gleich bleibt.

Die Geschäftslogik enthält die UseCases, welche ebenfalls durch Schnittstellen (Interfaces) abstrahiert werden, um eine einfachere Testbarkeit zu gewährleisten. Die UseCases sind hierbei in thematisch passende Klassen gekapselt. So gibt es, zum Beispiel die Klasse \textit{DataSeriesUseCases}, welche alle für die Datenreihen erforderlichen Verwaltungsaufgaben erfüllt, wie das Einfügen einer neuen Datenreihe, die Bearbeitung einer vorhandenen Reihe oder das Hinzufügen von Datenpunkten zu einer Datenreihe.

\subsection{View}
Die View, welche das Bild auf den Bildschirm bringt ist mittels Jetpack-Compose definiert. Dieses Framework basiert ebenfalls auf der Sprache Kotlin und sorgt für eine dynamische und flexible Erstellung der Benutzeroberfläche. Elemente in diesem Framework werden als \textit{Composables} annotiert. Dadurch, dass die Benutzeroberfläche zustandslos (stateless) bleibt, kommt es bei dem Wechsel von einer Aktivity zur Nächsten zu keinem Datenverlust. Die Viewmodels, welche in den entsprechenden Views verwendet werden, werden zu Beginn vom oberen Composable geladen und an die darunterliegenden weitergereicht.

\subsection{Viewmodel}
Die Viewmodels befinden sich in der Benutzeroberflächenschicht und enthalten nur die aktuellen Werte zur Darstellung des Displays. Sie kommunizieren über die UseCases der Geschäftslogikschicht mit den Repositories. Dadurch werden der Zugriff auf Daten und die Datenverarbeitung allein in der Geschäftslogik behandelt.

\section{Datenschicht}

\section{Geschäftslogik}

\subsection{UseCases}

\section{Benutzeroberfläche}

\section{Hintergrunddienste}

\subsection{External Intent Service}

\subsection{Inference Service}