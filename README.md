# ARVIN Hybrid APK Project

This project is a **hybrid Android app scaffold** for ARVIN-OMEGA.

It supports two modes:

- **Offline mode**: the Android app loads a local/off-device compatible dashboard and can be adapted to talk to a locally running Python service.
- **Cloud mode**: the Android app points to a remote ARVIN API.

## What is included

- `android-app/`: Android Studio project scaffold (Kotlin + WebView)
- `python-engine/`: FastAPI server scaffold for ARVIN endpoints and dashboard
- `shared/`: config examples shared between mobile and server

## Honest status

This is a **buildable project scaffold**, not a finished production APK.
You still need to:

1. Open `android-app/` in Android Studio
2. Set your package name / signing config
3. Decide your offline strategy:
   - easiest: bundle static dashboard assets and use cloud mode for compute
   - advanced: run local backend via embedded Python runtime / service
4. Build the APK from Android Studio or Gradle

## Recommended practical architecture

### Offline mode
Use the Android app UI + locally bundled dashboard assets.
If you want true on-device ARVIN compute, connect the UI to:

- Chaquopy, or
- a local Python runtime/service, or
- later, a Kotlin port of the core inference path.

### Cloud mode
Point the app to a remote FastAPI server using `shared/app_config.json`.

## Python engine quick start

```bash
cd python-engine
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn server:app --host 0.0.0.0 --port 8000
```

Then open:

- `http://127.0.0.1:8000/health`
- `http://127.0.0.1:8000/dashboard`

## Android app quick start

1. Open `android-app/` in Android Studio
2. Edit `shared/app_config.json`
3. Build and run

## Important integration point

The Python server currently includes a **stub engine adapter**.
Replace the TODO in `python-engine/engine_adapter.py` with your real ARVIN invocation.

## Suggested next steps

1. Plug your real ARVIN backtest/live commands into `engine_adapter.py`
2. Test the Python dashboard in browser
3. Point the Android app WebView to the dashboard URL
4. Add file picker + dataset upload in the app
5. Add authentication if you expose cloud mode publicly
