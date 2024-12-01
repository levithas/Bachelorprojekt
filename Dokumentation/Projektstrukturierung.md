Quelle: https://medium.com/@ArashPro/how-to-structure-a-jetpack-compose-project-616b3fe22daa

Gute Struktur, durch übersichtliche Einteilung in Zuständigkeiten. Zwar etwas überfüllt, aber es muss ja nicht jeder Punkt genauso gemacht werden.

Quelle: https://jonas-rodehorst.dev/blog/how-to-structure-your-jetpack-compose-project

Durch die mehreren Strukturen kann man sich gut aussuchen, was man für sein Projekt braucht. Die erste Struktur passt aber besser für mein Projekt, da ich die einzelnen Screens in Fragments abbilden möchte.

Es werden keine Fragments gemacht, da diese durch die Composables abgelöst wurden!

### Was ist Hilt?

Hilt ist eine Dependency-Injection-Bibliothek für Android, die auf Dagger basiert und speziell für Android entwickelt wurde, um Abhängigkeiten in einer App automatisch bereitzustellen. Mit Hilt kannst du eine einfache und konsistente Methode verwenden, um Abhängigkeiten über verschiedene Android-Komponenten hinweg zu verteilen – wie `Activity`, `Fragment`, `ViewModel` und `Service`. Hilt vereinfacht die Implementierung der Abhängigkeitsinjektion erheblich und sorgt dafür, dass dein Code modular und besser testbar bleibt.

Verwaltet in:
di - Dependency Injection
	- DatabaseModule
	- RepositoryModule

