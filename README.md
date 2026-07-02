# 🚗 Saudi Regulations on Vehicles - Appearnces:
This project is a deployment of a Vision Language Model (VLM) to be used to instantly identify if a vehicle violates any of
the regukations on vehicles' appearnces as defined by SASO (Saudi Standards, Metrology, and Quality Orgnization. 

## ✨ Features: 
- ✔️ Validate the input's type, format, and size. 
- 🔄 Encode and convert the input to base64 format. 
- 🧠 Prompt llava-phi3 to analyze the input, compare it with Saudi Regulations, and return JSON output. 
- 🧩 Deconstruct the JSON output and produce easily read summary. 
- 🖥️ Display the summary in a simple and appealing user interface. 

## 🤖 AI Usage: 
- 🖼️ Image Analysis:  
*llava-phi3* was used to analyze an image of a car and copare it with Saudi regulations on vehichles' appearances. 
- 💻 Code Generation:  
Copilot chatbot was used in many instances to generate code, especially in generating html code for user interfaces. It was
also used heavily to analyze code errors and finding ways to solve them. 

## 📁 Project Structure: 
```text
project/
│
├── Modules/
│   ├── input_acceptance.py
│   ├── vision_inference.py   
│   └── decision_maker.py
├── frontend/
│   └── index.html
├── Sample inputs/
│   ├── car1.jpg
|		├── car2.jpg
│   ├── car3.jpg  
│   └── car4.jpeg
├── main.py
└── requirements.txt
```

## ⚙️ How it works: 

1- Validate input: 
Confirm that the input is an image, and that it is in the right size and format, otherwise: raise an error. 

2- Analyze input: 
Prompt *llava-phi3* to check that the vehicle in the image complies with Saudi regulations on vehicles' appearnces. 
Detect: Image type, Vehicle's type, color, and any modifications on it, enviroment, restriction violations found, confidence, 
and level of uncertanity. Then output the result in JSON format. 
The prompt used to make the analysis on the image and to return a JSON file: 
```text
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
```


3- Make a decision: 
Based on the deconstructed output from the VLM, make a decision of what should be done as recommended actions. Then 
display it as a summary on a user interface. 


## 🚀 Running the application: 
This project includes a FastAPI backend, a local vision‑language model (LLaVA‑Phi3), and a browser‑based frontend. Follow the steps below to run everything smoothly.

1. 🔧 Install Requirements  
Make sure you have:

Python 3.10+

Ollama installed on your machine  
(Download from: https://ollama.com)

Then install Python dependencies:  
```text
pip install -r requirements.txt
```
2. 📥 Pull the LLaVA‑Phi3 Model  
The backend uses LLaVA‑Phi3 for image analysis. Pull it once:  
```text
ollama pull llava-phi3
```
This may take a few minutes depending on your connection

3. ▶️ Start the Backend Server  
Run FastAPI using Uvicorn:  
```text
uvicorn main:app --reload
```
4. 🌐 Open the Frontend  
The frontend is served automatically by FastAPI.  
Open your browser and go to:
```text  
http://127.0.0.1:8000/frontend/index.html 
You should now see the Vehicle Appearance Analyzer interface.
```
5. 📸 Analyze an Image  
- Click Choose File  
- Select a vehicle image  
- Click Analyze Vehicle  

The system will:  
- send the image to the backend  
- run LLaVA‑Phi3  
- extract and sanitize JSON  
- display a structured summary in the UI

## ⭐ Additional Details: 

#### Sample inputs (images that have been used):
Please find the images used for analysis and testing in:
```text 
\Sample_inputs
``` 
folder. 


#### Sample output (run):

![Input interface](".\Sample_outputs\SaudiRegulationsAnalyzer-output3.png")
![Sample Output 1](".\Sample_outputs\SaudiRegulationsAnalyzer-output1.png")
![Sample Output 2](".\Sample_outputs\SaudiRegulationsAnalyzer-output2.png")


#### Insights gained: 
This experiment showed how to correctly implemnt and use VLM in applications. Also showed me how heavy is the importance
of the prompt structure and wording. It for sure gave me the freedom of creativity which I enjoy very much. 
One other important thing it showed me is that how different VLMs behave and how deffirent their requirements are. 