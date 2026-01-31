# Pichlhofers Rezeptsammlung - Projektinfo

## Schnellstart für Claude
Lies diese Datei zuerst! Sie enthält den kompletten Projektkontext.

---

## Projektübersicht
- **Name:** Pichlhofers Rezeptsammlung
- **Typ:** Rezepte-Website mit CRUD-Funktionalität
- **Design:** Apple-Style (clean, minimalist, SF Pro Font, subtle shadows)
- **Live-URL:** https://lokadamus.github.io/Rezepte/
- **GitHub:** https://github.com/Lokadamus/Rezepte

---

## Technologie-Stack
- **Frontend:** Pure HTML/CSS/JavaScript (kein Framework)
- **Datenbank:** Firebase Firestore (Cloud)
- **Hosting:** GitHub Pages (statisch)
- **Bilder:** GitHub repo (`assets/images/`) ODER externe URLs

### Firebase-Konfiguration
- **Projekt:** pichlhofer-rezepte
- **Region:** europe-west3 (Frankfurt)
- **Tarif:** Spark (kostenlos) - kein Storage verfügbar

```javascript
const firebaseConfig = {
  apiKey: "AIzaSyD7Uv_0w7T4NZSlUQsOw9MJ8irOYB51kbk",
  authDomain: "pichlhofer-rezepte.firebaseapp.com",
  projectId: "pichlhofer-rezepte",
  storageBucket: "pichlhofer-rezepte.firebasestorage.app",
  messagingSenderId: "616466355086",
  appId: "1:616466355086:web:9fb3256c9deec444650adf"
};
```

---

## Features (implementiert)
1. **Rezepte anzeigen** - Grid mit Karten, Kategoriefilter, Suche
2. **Rezept hinzufügen** - Modal-Formular mit + Button
3. **Rezept bearbeiten** - Stift-Icon in Detailansicht
4. **Rezept löschen** - Papierkorb-Icon in Detailansicht
5. **Einkaufsliste drucken** - Button in Detailansicht
6. **Export als JSON** - Download-Button im Header
7. **Import aus JSON** - Upload-Button im Header (für Migration)
8. **7 Tage Wochenplan** - Grüner Button, zeigt 7 zufällige Rezepte
9. **Bilder** - Lokale Dateien ODER externe URLs (Google Fotos, Imgur, etc.)

---

## Kategorien
- Vorspeisen
- Hauptspeisen
- Desserts

---

## Dateistruktur
```
rezepte-website/
├── index.html          # Komplette App (HTML + CSS + JS)
├── assets/
│   ├── css/
│   │   └── style.css   # Haupt-Stylesheet
│   └── images/         # Lokale Rezeptbilder
├── rezepte.json        # Backup/Import-Datei
├── server.py           # Lokaler Dev-Server (optional)
└── PROJEKT-INFO.md     # Diese Datei
```

---

## Wichtige Entscheidungen & Warum

### Warum kein Jekyll?
Ruby-Version auf dem Mac war zu alt (2.6), Upgrade war kompliziert. Pure HTML/JS war einfacher.

### Warum Firebase statt localStorage?
Rezepte sollen von überall zugänglich sein und nach Refresh erhalten bleiben.

### Warum kein Firebase Storage?
Benötigt Blaze-Tarif (Kreditkarte). Stattdessen: ImgBB für Uploads.

### Bild-Upload mit ImgBB
- **API-Key:** 31955502dda578a20355e36b06d783d1
- Kostenlos, unbegrenzt
- Upload direkt vom Smartphone möglich
- URL wird automatisch ins Formular eingefügt

### Bilder-Workflow
- **Option A (empfohlen):** "Foto wählen" Button im Formular - lädt direkt zu ImgBB hoch
- **Option B:** Bild auf GitHub in `assets/images/` hochladen, dann nur Dateiname eingeben
- **Option C:** Externe URL manuell einfügen

### iCloud-Links funktionieren NICHT
iCloud-Share-Links sind keine direkten Bild-URLs, sondern Weiterleitungen zu einer Sharing-Seite.

---

## Bekannte Einschränkungen
- Bilder können nicht direkt hochgeladen werden (kein Backend)
- Keine Benutzer-Authentifizierung (jeder kann Rezepte bearbeiten)
- Firebase Firestore hat Gratis-Limits (ausreichend für ~200 Rezepte)

---

## Lokale Entwicklung
```bash
cd /Users/maximus/rezepte-website
python3 -m http.server 8000
# Dann öffnen: http://localhost:8000
```

---

## Git & Deployment
```bash
git add .
git commit -m "Beschreibung"
git push
# GitHub Pages aktualisiert automatisch (1-2 Min)
```

---

## Kontakt & Präferenzen
- **Benutzer:** Maximus / Pichlhofer Familie
- **Sprache:** Deutsch bevorzugt
- **Design:** Apple-Style, minimalistisch, keine Emojis
