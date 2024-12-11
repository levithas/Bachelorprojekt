### Grundlagen zu KI-Modellen und ihrer mobilen Anwendung

Im folgenden wird genauer darauf eingegangen, was ein KI-Modell ist, wo die Probleme im mobilen Einsatz liegen und wie diese gelöst werden können.

#### Einführung in KI-Modelle und maschinellen Lernen

"Was ist ein KI-Modell?"


"Was ist maschinelles Lernen?"
"Ansprechen von Linearen und nicht-linearen Funktionen"
"Wie kann ein Algorithmus überhaupt lernen?"

#### "Welche Arten von maschinellen Lernen gibt es?" "Welche Anforderungen an die Daten hat ein solcher Lernalgoritmus?"
Das maschinelle Lernen lässt sich in 3 Kategorien unterteilen: Supervised, Unsupervised und Reinforcement Learning.

- Supervised Learning (überwachtes Lernen) nutzt Daten, die bereits mit Labeln versehen sind, als Trainingsgrundlage. Ein Modell lernt so, Muster zu erkennen und neue, unbekannte Daten auf Basis dieser Muster zu klassifizieren oder zu quantifizieren. Eine typische Anwendung wäre hier die Annotation von Textdateien im Natural Language Processing (NLP). [Quelle]

- Unsupervised Learning (unüberwachtes Lernen) wird auf nicht gelabelten Daten angewendet. Das Modell identifiziert hier eigenständig Muster in den Daten, häufig zur Clusterbildung oder Dimensionsreduktion, z.B. bei der Segmentierung von Kundendaten oder zur Anomaliedetektion [Quelle].

- Reinforcement Learning ist eine Methode, bei der das Modell durch kontinuierliches Ausprobieren und Anpassen lernt, wie es bestimmte Ziele erreichen kann. Durch ein Belohnungssystem wird hier dem Modell mitgeteilt, wie gut eine Entscheidung gewesen ist. So kann das Modell seine Strategie nach und nach verbessern. Anwendung findet dieses Verfahren zum Beispiel in der Steuerung autonomer Systeme oder bei der Spielstrategieentwicklung.

Wie gut das Modell am Ende des Trainings auf neue, nicht in den Trainingsdaten vorhandene Zustände reagiert ist abhängig von der Qualität und Quantität der Trainingsdaten.

#### "Wie hoch sind die Anforderungen an die Rechenleistung beim lernen und beim vorhersagen?"

"Kurze Vorstellung von unterschiedlichen Modell-Strukturen (Perzeptron, Clustering, LSTM, Transformer)"

#### Verwendung von KI-Modellen auf mobilen Geräten
"Wie kann ein KI-Modell auf einem mobilen Gerät sinnvoll Anwendung finden?"
"Was sind die genauen Probleme die sich hier ergeben?"
"Wie werden diese Probleme gelöst?"
##### Quantisierung von KI-Modellen
"Was versteht man unter der Quantisierung?"

#### Android als Entwicklungsplattform für KI-Anwendungen
"Was ist Android?"
"Welche Tools helfen uns bei der Entwicklung für Android?"
"Welche Pakete sind notwendig um KI-Modelle in Android verwenden zu können?"
#### TensorFlow Lite
"Was ist der Unterschied zwischen TensorFlow und Tensorflow Lite bzw. LiteRT?"

#### Andere Frameworks
"Was gibt es noch für andere Frameworks die KI-Modelle auf mobilen Geräten ermöglichen?"




# Nochmal Aufbereitet

### maschinelles Lernen
- KI im Allgemeinen
- Unterschiede der Modelle (supervised, unsupervised, reinforcement) -> Was wird verwendet?
- Zeitreihenanalysen








### Schlafforschung
- Bedeutung von Schlafphasen
- Messung von Schlafphasen

### Android als Entwicklungsplattform
- MVVM (Quelle: https://developer.android.com/topic/architecture , https://developer.android.com/topic/architecture/recommendations)
	- Datenfluss zwischen Data <-> Domain <-> UI

Da mobile Geräte eingeschränkt sind in ihren verfügbaren Ressourcen kann das Betriebssystem jederzeit einzelne Komponenten von Apps beenden. Zustände müssen demnach außerhalb der Komponenten gespeichert werden. Die Komponenten müssen außerdem unabhängig voneinander gestartet werden können.
Mit steigendem Umfang der Anwendung, steigt auch die Anforderung an eine solide Architektur um Stabilität, sowie einfache Skalierbarkeit und Testbarkeit zu ermöglichen. Hierzu lässt sich das Prinzip der "Separierung von Verantwortlichkeiten" (Seperation of Concerns) anwenden. Es besagt, dass ein System in klar abgegrenzte Module oder Komponenten unterteilt werden sollte, wobei jede Komponente eine spezifische Aufgabe oder Verantwortung übernimmt. Die Benutzeroberfläche (UI), Geschäftslogik und Datenverwaltung werden also in separaten Schichten organisiert. Dadurch wird der Code übersichtlicher und verhindert, dass Änderungen in einem Bereich des Systems Beeinträchtigungen in anderen Bereichen verursachen.

[Hier ein Bild der verschiedenen Layer]

Um die Daten, die der Nutzer über das UI in die App eingibt nicht zu verlieren durch mögliche Ressourcenfreigaben des Betriebssystems werden Zustände und Daten in Datenmodellen gestaltet. Datenmodelle repräsentieren die Daten einer App und sind unabhängig von den UI-Elementen und anderen Komponenten der App. Diese Modelle sind nicht an den Lebenszyklus des UI oder der Komponenten gebunden, werden aber dennoch zerstört, sobald das Betriebssystem den Prozess der App aus dem Speicher entfernt. Datenmodelle vereinfachen zusätzlich die Testbarkeit der Datenschicht.


Daten werden über eine zentrale Datenquelle (SSTO - "Single Source of Truth") bereitgestellt. Der Zugriff auf diese SSTO erfolgt in einem Unidirektionalen Datenfluss Muster (UDF). Der Zustand fließt nur in eine Richtung, während Ereignisse, die die Daten verändern, in die entgegengesetzte Richtung fließen. Beispielsweise fließen Anwendungsdaten von Datenquellen zum UI. Nutzeraktionen, wie das Drücken eines Buttons wandern von der UI zur SSOT, wo die Anwendungsdaten geändert und in einer unveränderlichen Form bereitgestellt werden. Durch Anwendung dieses Patterns wird die Konsistenz der Daten gesichert. Durch den definierten Fluss der Daten ist es außerdem einfacher Fehler zu entdecken.

[Bild eines Datenflusses]





- Bedeutung und Folgen der Containerisierung






