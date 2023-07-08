# rick_and_morty_app

A new Flutter project.

## Automatizacion de pruebas con Appium

Requisitos:

- NodeJS (npm)
- Android Studio (Android SDK, Java JDK)
- Python

Instalacion:

```console
npm i -g appium@next
appium driver install uiautomator2
```

- [Descargar Appium inspector](https://github.com/appium/appium-inspector/releases)
- [Descargar el APK](https://github.com/wensespl/rick_and_morty_app/releases)

Nota: De ser necesario tener definido las variables de entorno `ANDROID_HOME` y `ANDROID_SDK_ROOT`

Uso:

Iniciar un servidor de Appium

```console
appium
```

Configuracion basica del Appium Inspector

```JSON
{
  "platformName": "Android",
  "appium:automationName": "UiAutomator2",
  "appium:deviceName": "Pixel 2 API 29",
  "appium:appPackage": "com.example.rick_and_morty_app",
  "appium:appActivity": ".MainActivity"
}
```

Ejecutar pruebas con python:

```console
pip install Appium-Python-Client
```

Ejecutar script del archivo `test\test.py`

## Getting Started

This project is a starting point for a Flutter application.

A few resources to get you started if this is your first Flutter project:

- [Lab: Write your first Flutter app](https://docs.flutter.dev/get-started/codelab)
- [Cookbook: Useful Flutter samples](https://docs.flutter.dev/cookbook)

For help getting started with Flutter development, view the
[online documentation](https://docs.flutter.dev/), which offers tutorials,
samples, guidance on mobile development, and a full API reference.
