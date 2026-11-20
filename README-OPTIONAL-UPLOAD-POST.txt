OpenShorts change: Upload-Post API key is optional.

This patch changes only dashboard/src/App.jsx. Gemini remains required for the AI clip-generation workflow. Upload-Post is required only when the user invokes a direct publishing feature; the backend publishing endpoints already return a missing-key error when publishing is attempted without a key.

Apply from ~/projects/openshorts with:
unzip -o /mnt/c/Users/siddh/Downloads/openshorts-optional-upload-post.zip -d .
