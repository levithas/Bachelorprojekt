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
