from ollama import chat
import re
import json

VEHICLE_ANALYSIS_PROMPT = """
You are a Saudi expert vehicle appearance inspector. 
You are checking a Saudi car. 
Analyze the provided image and produce a structured output in one of the following formats: JSON.

Stick to checking the following restrictions on model apperances ONLY: 
- Visibility of a valid license plate.
- Level of windows’ tint.
- Restrictions on external lighting.

Your analysis must include:

1. Image Type
2. Main Objects / Information Detected
3. Main Findings
4. Confidence Level / Uncertainty
5. Recommended Actions

Return the final answer ONLY in valid JSON format.
Do not include explanations, notes, or text outside the JSON.

The JSON structure must be exactly:

{
  "image_type": "",
  "objects_detected": {
    "vehicle": {
      "type": "",
      "color": "",
      "modifications": [""]
    },
    "environment": ""
  },
  "main_findings": [""],
  "confidence_level": "",
  "uncertainty": "",
  "recommended_actions": [""]
}

"""


def run_llava_phi3(base64_image: str, prompt: str = VEHICLE_ANALYSIS_PROMPT) -> str:
    response = chat(
        model="llava-phi3",
        messages=[
            {
                "role": "user",
                "content": prompt,
                "images": [base64_image]
            }
        ]
    )
    return response["message"]["content"]


def extract_json(text: str):
    stack = []
    start = None

    for i, ch in enumerate(text):
        if ch == '{':
            stack.append('{')
            if start is None:
                start = i
        elif ch == '}':
            if stack:
                stack.pop()
                if not stack:
                    try:
                        return json.loads(text[start:i+1])
                    except:
                        return None
    return None


def sanitize_json(data: dict):
    def fix_list(lst):
        if not isinstance(lst, list):
            return [str(lst)]

        new_list = []
        for item in lst:
            if isinstance(item, dict):
                text = ", ".join(f"{k}: {v}" for k, v in item.items())
                new_list.append(text)
            else:
                new_list.append(str(item))
        return new_list

    vehicle = data.get("objects_detected", {}).get("vehicle", {})
    if "modifications" in vehicle:
        vehicle["modifications"] = fix_list(vehicle["modifications"])

    if "main_findings" in data:
        data["main_findings"] = fix_list(data["main_findings"])

    if "recommended_actions" in data:
        data["recommended_actions"] = fix_list(data["recommended_actions"])

    if not data.get("recommended_actions"):
        data["recommended_actions"] = ["No specific actions detected"]

    return data
