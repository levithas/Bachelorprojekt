KI-Modelle sind aus der heutigen Zeit nicht mehr wegzudenken. In nahezu jeder Lebenslage begegnen sie einem und sorgen dafür, dass unser Umgang mit großen Informationsmengen vereinfacht wird. Viele dieser KI-Modelle benötigen große Rechenzentren um verarbeitet werden zu können. Beispielhaft benötigt eine Instanz von ChatGPT mindestens [Irgendwie so viele] GPU-Einheiten. Das entspricht einer Anzahl von [Vielen] Heimcomputern. Aber KI-Modelle müssen nicht immer so groß sein um etwas leisten zu können. Es gibt sogar Verfahren um diese auf mobilen Endgeräten lauffähig zu machen. 

In Bezug auf die Schlafphasenanalyse lassen sich KI-Modelle anhand von Sensorwerten von Smartwatches trainieren. Eigentlich werden für die Schlafphasenanalyse in der Medizin sogenannte Polysomnographen verwendet. Diese Geräte sind aber sehr teuer und die Auswertung der Messergebnisse erfordert ein Expertenwissen, welches der normale Anwender nicht hat. Es hat Vorteile für den Anwender seine Schlafzyklen aufzuzeichnen. So kann er besser nachvollziehen wie lang er geschlafen hat, welche Schlafphasen er die Nacht für wie lange hatte. Er kann auch davon Profitieren, dass zuum Beispiel sein Wecker ihn in einer leichteren Schlafphase weckt. So würde die Wecker-App anhand der Schlafdaten prüfen, ob der Anwender sich z.B. 30 Minuten vor der eigentlichen Weckzeit in einer leichten Schlafphase befindet und die Weckzeit dementsprechend nach vorne verlegen.

Viele Anwendungen die einen solchen Dienst auf mobilen Geräten bereitstellen sind kostenpflichtig oder teilen ihre Daten mit Dritten. Gerade im Bezug auf Gesundtheitsdaten fühlen sich viele Anwender nicht wohl damit ihre Daten an Firmen weiterzugeben. Daher zielt diese Arbeit darauf ab eine quelloffene Alternative zu bieten, durch welche Personenbezogene Daten auf lokalen KI-Modellen verwendet werden können, um so das maximale Maß an Datenschutz zu gewährleisten. Gleichzeitig soll die Anwendung eine grundlegende Plattform bieten um die Entwicklung von KI-Modellen auf mobilen Geräten zu erleichtern. 


### GPT Version von dem da oben

In der heutigen Zeit sind KI-Modelle unverzichtbar geworden und begegnen uns in nahezu jedem Lebensbereich. Sie helfen, große Informationsmengen zu verarbeiten und machen den Umgang mit komplexen Daten einfacher. Oftmals benötigen solche Modelle jedoch immense Rechenleistung und greifen auf große Rechenzentren zurück – etwa für Anwendungen wie ChatGPT, das mehrere GPU-Einheiten zur Verfügung haben muss, was der Leistung zahlreicher Heimcomputer entspricht. Doch nicht alle KI-Modelle sind so ressourcenintensiv. Es gibt Methoden, die es ermöglichen, KI-Modelle auch auf mobilen Endgeräten effizient laufen zu lassen.

Für die Schlafphasenanalyse beispielsweise können KI-Modelle mithilfe der Sensorwerte von Smartwatches trainiert werden. Während in der Medizin zur Schlafphasenanalyse teure Polysomnographen erforderlich sind und die Auswertung deren Daten Expertenwissen voraussetzt, bietet die Möglichkeit, den Schlaf über eine App aufzuzeichnen, auch für Laien wertvolle Einblicke. Durch eine App kann der Nutzer nachvollziehen, wie lange er geschlafen hat und in welchen Schlafphasen er sich befand. Eine smarte Weckerfunktion könnte darüber hinaus den Nutzer während einer leichten Schlafphase wecken, um das Aufwachen angenehmer zu gestalten.

Viele derartigen Apps sind jedoch kostenpflichtig oder geben die Daten an Dritte weiter. Gerade im Hinblick auf Gesundheitsdaten fühlen sich Nutzer oft unwohl, persönliche Daten mit externen Firmen zu teilen. Diese Arbeit hat daher das Ziel, eine quelloffene Alternative zu entwickeln, die es ermöglicht, persönliche Daten ausschließlich auf dem Gerät des Nutzers mithilfe von lokalen KI-Modellen zu verarbeiten und so den Datenschutz zu maximieren. Gleichzeitig soll die App als Plattform dienen, um die Entwicklung und Nutzung von KI-Modellen auf mobilen Geräten zu erleichtern und zu fördern.


### Alte Version mit Zitaten

In der heutigen, schnelllebigen Zeit wird Schlaf für viele Menschen immer mehr als zweitrangig eingeordnet.\cite{liuPrevalenceHealthySleep2016}
Medizinische Studien zeigen, dass unzureichender Schlaf die Anfälligkeit für Fettleibigkeit, Diabetes, Bluthochdruck, koronare Herzkrankheit, Schlaganfall, psychische Belastungen und die allgemeine Sterblichkeit deutlich erhöht.\cite{robbinsSleepTrackingSystematic2019}.
Die Erfassung der eigenen Schlafqualität gibt eine Möglichkeit diese Defizite rechtzeitig zu erkennen und ihnen entgegen zu wirken.
Die in der Medizin gängige Technik zur Erfassung von Schlafeigenschaften ist der Polysomnograph. Dieser ist für den persönlichen und alltäglichen Gebrauch nicht anwendbar, da er sehr teuer in der Anschaffung ist und zur Auswertung der Ergebnisse eine fachliche Qualifikation vorraussetzt \cite{songAIDrivenSleepStaging2023}.
Smartwatches beinhalten mehrere Sensoren, welche für das Schlaftracking genutzt werden können \cite{songAIDrivenSleepStaging2023}.
Teure Smartwatches besitzen auch schon eingebaute Funktionen, die genau diesen Zweck erfüllen \cite{walchSleepStagePrediction2019}.
Im Open-Source Bereich gibt es bisher nur wenige bis keine Möglichkeiten der Schlafphasenanalyse.
Die von mir in dieser Arbeit genutzte Smartwatch \textit{BangleJS} besitzt die gleichen Sensoren, wie andere Smartwatches und liegt im unteren Preissegment. Sie bietet einen vollständig offen liegenden Quellcode.
Die BangleJS besitzt bereits eine einfache Schlafphasenanalyse, die auf Schwellwerten beruht.
In dieser Arbeit werde ich eine Anwendung konzipieren und implementieren, welche durch neue Schlafphasenerkennungs-Algorithmen erweiterbar ist, um so die Qualität der Erfassung verbessern zu können. Desweiteren wird ein beispielhaftes Modell erarbeitet, welches zur Schlafphasen genutzt werden kann.
Meine Implementierung wird abschließend über GitHub öffentlich zur Verfügung gestellt und dem offiziellen Repository des BangleJS AppLoaders unter \url{https://github.com/espruino/BangleApps} als Contribution angeboten.


### Änderungshinweise:
- Es soll mehr auf die verschiedenen Nutzer (Entwickler und Endnutzer) eingegangen werden
- Mehr "Was ist der wirkliche nutzen?" und weniger drum herum


### Nächster Versuch

Künstliche Intelligenz (KI) ist heute aus vielen Lebensbereichen nicht mehr wegzudenken. Sie hilft, große Datenmengen zu verarbeiten und komplexe Informationen verständlicher zu machen. Viele Unternehmen, die KI-Modelle anbieten, gewähren keinen Einblick in ihre Systeme. Diese laufen auf leistungsstarken Servern, wobei sensible Daten über das Internet übertragen werden müssen. In der Regel bieten diese Unternehmen keine Möglichkeit zur Weiterentwicklung oder zum Zugang für externe Entwickler. Jedes Unternehmen muss somit ein eigenes Modell basierend auf eigenen Datensätzen entwickeln und eine Infrastruktur bereitstellen, um die Nutzung dieser Modelle zu ermöglichen. Dadurch wird die Integration von KI-Modellen in Anwendungen für Entwickler erschwert. Endnutzer hingegen müssen darauf vertrauen, dass ihre Daten sicher und korrekt verarbeitet werden und dass die Qualität der KI-Modelle den Erwartungen entspricht. Ein Wechsel zu einem anderen Modell oder die lokale Auswertung der eigenen Daten ist in der Regel nicht vorgesehen.

Meine App setzt hier an, indem sie es ermöglicht, KI-Modelle direkt auf mobilen Geräten zu nutzen, ohne auf große Unternehmen oder Cloud-Dienste angewiesen zu sein. Der Endnutzer kann so einfach ein Modell auswählen, dass im Internet frei zur Verfügung steht, es auf sein Gerät laden und Prognosen oder Kategorisierungen für die eigenen Daten erstellen lassen. Für Entwickler bietet die App eine unkomplizierte Schnittstelle, um Modelle zu integrieren, ohne sich um die Verwaltung von Daten und Modellen kümmern zu müssen. Die App ermöglicht es den Nutzern, Daten nahtlos zwischen verschiedenen Anwendungen auszutauschen. Nachdem der Nutzer die Kommunikation einmal freigegeben hat, übernimmt die App automatisch die Analyse und Verarbeitung der Daten, ohne dass weitere manuelle Eingriffe erforderlich sind.



### Beispiel anhand der Schlafphasenanalyse

In der Schlafphasenanalyse werden KI-Modelle mit Daten von Smartwatches trainiert, um die Schlafzyklen der Nutzer aufzuzeichnen. Eigentlich werden für die Schlafphasenanalyse in der Medizin sogenannte Polysomnographen verwendet. Diese Geräte sind aber sehr teuer und die Auswertung der Messergebnisse erfordert ein Expertenwissen, welches der normale Anwender nicht hat. Die Aufzeichnung der Schlafphasen bietet Nutzern jedoch Vorteile. So kann er besser nachvollziehen wie lang er geschlafen hat, welche Schlafphasen er die Nacht für wie lange hatte oder ob eine allgemeine Unruhe vorhanden war. Er kann auch davon Profitieren, dass zum Beispiel sein Wecker ihn in einer leichteren Schlafphase weckt. So würde die Wecker-App anhand der Schlafdaten prüfen, ob der Anwender sich z.B. 30 Minuten vor der eigentlichen Weckzeit in einer leichten Schlafphase befindet und die Weckzeit dementsprechend nach vorne verlegen.

Allerdings bringt die Aufzeichnung von Schlafdaten auch Herausforderungen mit sich, insbesondere im Hinblick auf den Schutz der Privatsphäre. Schlafgewohnheiten sind sehr persönliche Informationen, weshalb viele Nutzer zögern, entsprechende Apps zu verwenden. Es wird ein Modell auf gelabelten Daten trainiert. Dieses Modell dient als Baseline, um zu demonstrieren, wie KI-Modelle in meine App eingebunden und genutzt werden können und so die Privatsphäre der Nutzer zu gewährleisten.





# Neue Einführung

