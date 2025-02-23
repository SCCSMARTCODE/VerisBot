# VerisBot

**VerisBot** is a fun and experimental AI chatbot developed as a learning adventure using FastAPI and the Hugging Face Inference API. Powered by the google/gemma-2-2b-it model, this project showcases the art of crafting conversational AI, aimed at exploring how to create engaging, accurate, and intelligent responses. While it’s not designed for production use, VerisBot serves as an exciting playground for me to dive into the world of AI, master new technologies, and unleash creativity in developing advanced chat solutions.


## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Enterprise-Grade Chatbot:**  
  Provides clear, accurate, and professional responses tailored to business needs.
  
- **Serverless and Scalable:**  
  Leverages the Hugging Face Inference API to ensure cost-effective, scalable performance.
  
- **FastAPI-Based Backend:**  
  A lightweight and responsive RESTful API for handling chat interactions.
  
- **Structured Response Formatting:**  
  Utilizes a dedicated formatter to ensure all responses are well-structured and ready for frontend display.
  
- **Robust Prompt Engineering:**  
  Includes strict system instructions to guide the model’s behavior and maintain consistency in tone and style.

## Architecture

VerisBot is built using a modular architecture:

- **FastAPI Backend:**  
  Handles incoming chat requests, manages sessions, and processes errors.
  
- **Hugging Face Inference API Integration:**  
  Directly calls the `google/gemma-2-2b-it` model for generating responses.
  
- **Response Formatter:**  
  Processes and formats generated text to ensure professional and consistent output on the frontend.
  
- **Environment Configuration:**  
  All sensitive information (e.g., API keys) is managed through environment variables for security and flexibility.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/SCCSMARTCODE/VerisBot.git
   cd VerisBot
   ```

2. **Create a Virtual Environment and Install Dependencies:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables:**

   Create a `.env` file based on the provided `.env.example` and add your Hugging Face API key:

   ```env
   HF_API_KEY=your_huggingface_api_key
   HF_API_URL="https://api-inference.huggingface.co/models/google/gemma-2-2b-it"
   ```

## Usage

1. **Run the FastAPI Server:**

   ```bash
   uvicorn app.main:app --reload
   ```

2. **Interact with the Chatbot:**

   Send a POST request to the `/chat` endpoint with a JSON body containing a `message` field. For example:

   ```json
   {
     "user_id": "userId",
     "message": "What is a noun?"
   }
   ```

   The server will return a response similar to:

   ```json
   {
     "veris_response": "I am Veris, a high-quality AI chatbot built by SCCSMARTCODE using the Hugging Face Inference API. [Detailed answer...]"
   }
   ```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Include tests for your changes.
4. Submit a pull request with a clear description of your changes.

For major changes, please open an issue first to discuss your ideas.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or support, please contact:  
**SCCSMARTCODE**  
Email: [sccsmart247@gmail.com](mailto:sccsmart247@gmail.com)
