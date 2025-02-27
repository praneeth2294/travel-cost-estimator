# 🌍 Travel Cost Estimator

## 📌 Overview
The **Travel Cost Estimator** is an interactive AI-powered web application built using **Streamlit** and **LangChain**. It helps users find the best travel options between two locations, providing cost estimates, travel time, and key details for various modes of transport.

## 🚀 Features
- 📍 **Enter Source & Destination**: Users input their travel locations.
- 🏷️ **Multiple Travel Options**: Includes flights, trains, buses, and self-drive options.
- ⏳ **Estimated Travel Time**: Displays the expected duration for each option.
- 💰 **Cost Estimates**: Provides approximate costs based on real-world data.
- 📊 **Structured Output**: Results are presented in a well-formatted Markdown table.
- 🌍 **Interactive & User-Friendly**: Uses **Streamlit Tabs** for a seamless experience.

## 🛠️ Tech Stack
- **Python** 🐍
- **Streamlit** (Frontend UI)
- **LangChain** (AI-powered responses)
- **Google Generative AI (Gemini)** (For cost estimation & travel insights)

## 📥 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/username/travel-cost-estimator.git
cd travel-cost-estimator
```

### 2️⃣ Create a Virtual Environment (Recommended)
```bash
python -m venv env
source env/bin/activate  # On macOS/Linux
env\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up API Keys (if using external services)
Create a `.env` file and add your API keys (e.g., Google Generative AI, OpenAI, etc.).
```env
GOOGLE_API_KEY=your_google_api_key
```

### 5️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

## 🎯 Usage
1. Open the **Streamlit web app** in your browser.
2. Enter **Source** and **Destination** locations.
3. Get a structured **travel comparison table** with estimated costs, time, and best options.
4. Explore additional details like **recommended places to visit** during your journey.

## 🚀 Deployment
You can deploy this app using:
- **Streamlit Cloud**
- **Heroku**
- **AWS/GCP/Azure**
- **Docker** (for containerized deployment)

## 🤝 Contributing
Want to improve this project? Follow these steps:
1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Added new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Submit a Pull Request!

## 📜 License
This project is licensed under the **MIT License**.

---
Made with ❤️ by [praneeth](https://github.com/praneeth2294)


