# Brötje Wärmepumpe Integration für Home Assistant

🇬🇧 [English Version](README.md)

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![GitHub Release](https://img.shields.io/github/v/release/henrywiechert/ha-broetje)](https://github.com/henrywiechert/ha-broetje/releases)

<img src="custom_components/broetje_heatpump/images/logo.png" alt="Brötje Logo" width="200">

Home Assistant Integration für Brötje Wärmepumpen (und andere Heizsysteme) über Modbus TCP.

## Unterstützte Modelle

<img src="custom_components/broetje_heatpump/images/Broetje-BLW-Eco-10.1.png" alt="Brötje BLW Eco" width="300">
  

**Brötje BLW Eco 10.1** (getestet)

*Andere Brötje Wärmepumpen mit Modbus-Schnittstelle können ebenfalls funktionieren.*

## Funktionen

- **Nur-Lesen Überwachung** (v0.2)
- **ca. 100 Entitäten** in 6 Kategorien
- **Deutsche und englische Übersetzungen**
- 30-Sekunden Abfrageintervall

### Unterstützte Kategorien

| Kategorie | Sensoren | Binärsensoren | Beschreibung |
|-----------|----------|---------------|--------------|
| **Heizkreis 1** | 21 | 5 | Temperaturen, Sollwerte, Pumpe, Mischer |
| **Trinkwasser (TWW)** | 12 | - | Betriebsart, Legionellen, Zirkulation |
| **Trinkwasserspeicher** | 11 | 3 | Speichertemperaturen, Pumpen |
| **Pufferspeicher** | 5 | 2 | Puffertemperaturen, Ventile |
| **Kessel** | 31 | 3 | Brenner, Gebläse, Energiezähler |
| **Allgemeine Funktionen** | 3 | 4 | Außentemperatur, Alarm, Handbetrieb |

> ⚠️ **Hinweis:** Aktuell wird nur **Heizkreis 1 (HK1)** unterstützt. Unterstützung für HK2/HK3 kann in zukünftigen Versionen hinzugefügt werden.

## Voraussetzungen

- Brötje Wärmepumpe mit Modbus-Schnittstelle
- Modbus TCP Gateway verbunden mit der Wärmepumpe
- Home Assistant 2024.1.0 oder neuer

## Installation

### HACS (Empfohlen)

1. HACS in Home Assistant öffnen
2. Auf "Integrationen" klicken
3. Die drei Punkte oben rechts anklicken
4. "Benutzerdefinierte Repositories" auswählen
5. `https://github.com/henrywiechert/ha-broetje` hinzufügen und "Integration" als Kategorie wählen
6. "Hinzufügen" klicken
7. Nach "Brötje Heatpump" suchen und installieren
8. Home Assistant neu starten

### Manuelle Installation

1. Den Ordner `custom_components/broetje_heatpump` herunterladen
2. In das Home Assistant Verzeichnis `config/custom_components/` kopieren
3. Home Assistant neu starten

## Konfiguration

1. Zu **Einstellungen** → **Geräte & Dienste** gehen
2. **Integration hinzufügen** klicken
3. Nach "Brötje Heatpump" suchen
4. Verbindungsdaten eingeben:
   - **Host**: IP-Adresse des Modbus TCP Gateways
   - **Port**: Modbus TCP Port (Standard: 502)
   - **Unit ID**: Modbus Slave ID (Standard: 1)

## Entitäten

Siehe [ENTITIES.md](ENTITIES.md) für eine vollständige Liste aller 100 Entitäten mit Modbus-Registeradressen und Beschreibungen.

### Highlights

- **Temperaturen**: Vorlauf, Rücklauf, Raum, Kessel, Puffer, TWW
- **Energiezähler**: Gasverbrauch für Heizung und TWW (kWh)
- **Betriebsstunden**: Brennerstunden, Heizstunden, TWW-Stunden
- **Statusinformationen**: Kesselstatus, Brennerstatus, Pumpenzustände
- **Konfiguration**: Heizkurve, Sollwerte, Betriebsarten

Nicht jeder Sensor ist in allen Heizsystemen verfügbar! Z.B. Gasverbrauch in Wärmepumpe :-)

## Fehlerbehebung

### Verbindung zum Gerät nicht möglich

- Prüfen ob das Modbus TCP Gateway von Home Assistant erreichbar ist
- IP-Adresse und Port überprüfen
- Sicherstellen dass die Modbus Unit ID mit der Gerätekonfiguration übereinstimmt
- Konnektivität mit einem Modbus-Tool wie `mbpoll` testen

### Keine Sensorwerte

- Die Registeradressen müssen möglicherweise für Ihr spezifisches Modell angepasst werden
- Home Assistant Logs auf Modbus-Kommunikationsfehler prüfen

## Entwicklung

Diese Integration verwendet:

- [pymodbus](https://pymodbus.readthedocs.io/) ≥3.11.0 für Modbus TCP Kommunikation
- Home Assistant's `DataUpdateCoordinator` für effizientes Polling

### Mitwirken

Beiträge sind willkommen! Bitte:

1. Repository forken
2. Feature-Branch erstellen
3. Pull Request einreichen

## Roadmap

- [ ] Schreibunterstützung für R/W Register
- [ ] Zusätzliche Heizkreise (HK2, HK3)
- [ ] Wärmepumpen-spezifische Sensoren
- [ ] Fehlercodes und Diagnose
- [ ] Brötje Logo im offiziellen HA brand repo

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe [LICENSE](LICENSE) für Details.

## Haftungsausschluss

Diese Integration ist nicht mit Brötje verbunden oder von Brötje unterstützt. Verwendung auf eigene Gefahr.
