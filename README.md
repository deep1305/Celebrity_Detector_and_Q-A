# 🌟 Celebrity Detector and QA

An intelligent celebrity recognition and question-answering system powered by AI vision models and LLMs. Upload any celebrity image and get instant identification along with the ability to ask questions about them.

## 🌟 Features

- **AI-Powered Celebrity Recognition**: Uses GROQ's vision-enabled LLM for accurate celebrity identification
- **Face Detection**: OpenCV-based face detection to validate uploaded images
- **Interactive Q&A**: Ask questions about identified celebrities and get AI-powered answers
- **Real-time Processing**: Fast image analysis and response generation
- **Clean Web Interface**: User-friendly Flask web application with modern UI
- **Comprehensive Information**: Get detailed info including name, profession, nationality, and achievements

## 🛠️ Tech Stack

- **LLM**: GROQ API (Llama 4 Maverick 17B model with vision capabilities)
- **Computer Vision**: OpenCV for face detection
- **Backend**: Flask
- **Frontend**: HTML/CSS
- **Language**: Python 3.12.10
- **Containerization**: Docker
- **Orchestration**: Kubernetes

## 📁 Project Structure

```
Celebrity Detector and QA/
├── app/                         # Flask application
│   ├── __init__.py             # App factory
│   ├── routes.py               # API routes
│   └── utils/                  # Core modules
│       ├── celebrity_detector.py  # Celebrity identification
│       ├── image_handler.py       # Image processing
│       └── qa_engine.py           # Q&A system
├── static/                     # CSS and assets
│   └── style.css
├── templates/                  # HTML templates
│   └── index.html
├── app.py                      # Application entry point
├── setup.py                    # Package setup
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── kuberenetes-deployment.yaml # K8s manifests
└── .env                        # Environment variables
```

## 🚀 Getting Started

### Prerequisites

- Python 3.12.10 or higher
- GROQ API key ([Get one here](https://console.groq.com))

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/deep1305/Celebrity_Detector_and_Q-A.git
   cd "Celebrity Detector and QA"
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   Or use editable install:

   ```bash
   pip install -e .
   ```

3. **Set up environment variables**

   Create a `.env` file in the root directory:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   GROQ_API_URL=https://api.groq.com/openai/v1/chat/completions
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

5. **Open your browser** to `http://localhost:5000`

## 💡 Usage

### Step 1: Upload Celebrity Image
- Click "Choose File" and select an image of a celebrity
- The system will detect faces and identify the celebrity

### Step 2: View Celebrity Information
The AI will provide:
- Full Name
- Profession
- Nationality
- Famous For
- Top Achievements

### Step 3: Ask Questions
Ask anything about the identified celebrity:
- *"What are their most famous movies?"*
- *"When were they born?"*
- *"What awards have they won?"*
- *"Tell me about their early life"*

## 🐳 Docker Deployment

Build and run with Docker:

```bash
# Build the image
docker build -t celebrity-detector .

# Run the container
docker run -p 5000:5000 --env-file .env celebrity-detector
```

Access at `http://localhost:5000`

## ☸️ Kubernetes Deployment

Deploy to Kubernetes cluster:

```bash
# Create secrets
kubectl create secret generic llmops-secrets \
  --from-literal=GROQ_API_KEY=your_api_key \
  --from-literal=GROQ_API_URL=https://api.groq.com/openai/v1/chat/completions

# Apply manifests
kubectl apply -f kuberenetes-deployment.yaml

# Get external IP
kubectl get service llmops-service
```

Wait for the LoadBalancer to assign an external IP, then access the application.

## 📊 How It Works

1. **Image Upload**: User uploads a celebrity image through the web interface
2. **Face Detection**: OpenCV detects faces in the uploaded image
3. **Celebrity Recognition**: Image is sent to GROQ's vision-enabled LLM for identification
4. **Information Extraction**: AI extracts structured information about the celebrity
5. **Q&A System**: Users can ask follow-up questions powered by the LLM
6. **Response Display**: Results are displayed in a clean, formatted interface

## 🔧 Configuration

### Environment Variables

- `GROQ_API_KEY`: Your GROQ API key (required)
- `GROQ_API_URL`: GROQ API endpoint (default: https://api.groq.com/openai/v1/chat/completions)

### Model Configuration

Currently using `meta-llama/llama-4-maverick-17b-128e-instruct` for:
- Vision-based celebrity recognition
- Natural language Q&A

You can modify the model in:
- `app/utils/celebrity_detector.py`
- `app/utils/qa_engine.py`

## 📦 Dependencies

- **flask**: Web framework
- **opencv-python**: Computer vision and face detection
- **numpy**: Numerical operations
- **requests**: API communication
- **python-dotenv**: Environment variable management

## 🚧 Troubleshooting

### "No face detected in the image"
- Ensure the image contains a clear, visible face
- Try uploading a higher quality image
- Make sure the face is not obscured

### "Unknown" celebrity result
- The AI might not recognize less famous individuals
- Try with a clearer or more recent photo
- Verify the image quality is good

### API Errors
- Check your GROQ API key is valid
- Ensure you have API credits remaining
- Verify your internet connection

## 🔮 Future Enhancements

- [ ] Multi-face detection and recognition
- [ ] Celebrity comparison feature
- [ ] Historical data and timeline
- [ ] Social media integration
- [ ] Batch image processing
- [ ] Celebrity similarity search

## 🙏 Acknowledgments

- Powered by GROQ's lightning-fast LLM inference
- Built with Flask and OpenCV
- Uses Meta's Llama 4 models

---

**Made with ❤️ for celebrity enthusiasts**

