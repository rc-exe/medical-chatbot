 Real-time Chatbot for Medical FAQs using NLP

This project is a real-time chatbot designed to provide users with accurate and conversational answers to frequently asked medical questions using Natural Language Processing (NLP). The system interprets user queries and responds with verified medical information.

 🚀 Features

- Real-time response to user queries
- NLP-based query understanding
- Context-aware conversation flow
- Trained on curated medical FAQ datasets
- Can be integrated with web or mobile frontends

 🛠️ Technologies Used

- Python
- Flask (for backend API)
- Transformers (HuggingFace) or OpenAI GPT
- PyTorch (for model training/inference)
- NLTK / spaCy (for text preprocessing)
- Pandas, NumPy (for data handling)

 📁 Project Structure


.
├── app.py                   Flask API
├── chatbot_model.py         NLP model handling
├── requirements.txt
├── README.md
├── templates/
│   └── index.html           Basic front-end (optional)
└── data/
    └── medical_faqs.csv     Sample data


 🔑 OpenAI API Key Setup

If you are using OpenAI GPT for natural language responses, follow these steps:

1. Sign up at [https://platform.openai.com](https://platform.openai.com) and get your API key.
2. In your project root directory, create a .env file and add the following line:


OPENAI_API_KEY=your_openai_api_key_here


3. Load this key in your Python code using:

python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


Make sure you install the python-dotenv package if you're using this method:

bash
pip install python-dotenv


 ⚙️ Installation

bash
git clone https://github.com/yourusername/medical-chatbot-nlp.git
cd medical-chatbot-nlp
pip install -r requirements.txt


 ▶️ Running the App

bash
python app.py


Go to http://127.0.0.1:5000 in your browser to interact with the chatbot (if using the frontend).

 📄 License

This project is for academic and research purposes only.
