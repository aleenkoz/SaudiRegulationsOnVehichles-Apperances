from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from Modules.input_acceptance import validate_and_prepare_image
from Modules.inference_vision import run_llava_phi3, extract_json, VEHICLE_ANALYSIS_PROMPT, sanitize_json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


@app.post("/test-input")
async def test_input(file: UploadFile):
    image_data = validate_and_prepare_image(file)
    return {
        "status": "Image accepted",
        "content_type": image_data["content_type"],
        "size_mb": round(image_data["size_mb"], 3),
        "base64_preview": image_data["base64"][:50]
    }


@app.post("/analyze-image")
async def analyze_image(file: UploadFile):
    image_data = validate_and_prepare_image(file)

    raw_output = run_llava_phi3(
        base64_image=image_data["base64"],
        prompt=VEHICLE_ANALYSIS_PROMPT
    )

    parsed = extract_json(raw_output)

    if parsed is None:
        return {
            "status": "error",
            "analysis": "Model returned invalid JSON.",
            "raw_output": raw_output
        }

    sanitized = sanitize_json(parsed)

    return {
        "status": "analysis complete",
        "analysis": sanitized
    }
