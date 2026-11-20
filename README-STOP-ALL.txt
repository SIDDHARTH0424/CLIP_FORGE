OpenShorts Stop All patch

Files in this archive retain their paths relative to the OpenShorts project root:
- app.py
- remote_worker.py
- worker.py
- dashboard/src/App.jsx

Before extracting, back up those four files. Then extract this ZIP into the OpenShorts
project root and allow it to overwrite the matching files.

The backend endpoint is POST /api/jobs/cancel-all. In managed mode it only cancels
the authenticated user's jobs; in self-hosted mode it cancels jobs on that instance.
The dashboard button appears beside the PROCESSING badge in Live Analysis.

Checks performed:
- Python compile() syntax check passed for app.py, remote_worker.py, worker.py.
- TypeScript's JSX transpiler parsed App.jsx without diagnostics.
- Full Docker/runtime integration test was not run here.
