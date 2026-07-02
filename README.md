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
llava-phi3 was used to analyze an image of a car and copare it with Saudi regulations on vehichles' appearances. 
- 💻 Code Generation: 
Copilot chatbot was used in many instances to generate code, especially in generating html code for user interfaces. It was
also used heavily to analyze code errors and finding ways to solve them. 

## 📁 Project Structure: 
\project/
│
├── Modules/
│   ├── input_acceptance.py
│   ├── vision_inference.py   
│   └── decision_maker.py
├── frontend
│   └──  index.html
├── main.py
└── requirements.txt\

## ⚙️ How it works: 

1- Validate input: 
Confirm that the input is an image, and that it is in the right size and format, otherwise: raise an error. 

2- Analyze input: 
Prompt llava-phi3 to check that the vehicle in the image complies with Saudi regulations on vehicles' appearnces. 
Detect: Image type, Vehicle's type, color, and any modifications on it, enviroment, restriction violations found, confidence, 
and level of uncertanity. Then output the result in JSON format. 

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
\pip install -r requirements.txt\ 

2. 📥 Pull the LLaVA‑Phi3 Model  
The backend uses LLaVA‑Phi3 for image analysis. Pull it once:  
\ollama pull llava-phi3\  
This may take a few minutes depending on your connection

3. ▶️ Start the Backend Server  
Run FastAPI using Uvicorn:  
\uvicorn main:app --reload\

4. 🌐 Open the Frontend  
The frontend is served automatically by FastAPI.  
Open your browser and go to:  
\ http://127.0.0.1:8000/frontend/index.html \  
You should now see the Vehicle Appearance Analyzer interface.

5. 📸 Analyze an Image  
- Click Choose File  
- Select a vehicle image  
- Click Analyze Vehicle  

The system will:  
- send the image to the backend  
- run LLaVA‑Phi3  
- extract and sanitize JSON  
- display a structured summary in the UI
