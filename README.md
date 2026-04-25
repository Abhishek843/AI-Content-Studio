# AI Content Studio

An AI-powered content generation platform that creates engaging video content from topics using a multi-agent system. The system orchestrates specialized agents to plan, write scripts, optimize hooks, generate visuals, and produce final videos.

## Features

- **Multi-Agent Architecture**: Specialized agents for different content creation tasks
- **Automated Content Pipeline**: End-to-end content generation from topic to final video
- **AI-Powered Generation**: Uses Gemini AI for intelligent planning and scripting
- **Visual Content**: Generates images and scenes based on script requirements
- **Audio Generation**: Text-to-speech capabilities for video narration
- **Video Production**: Combines visuals, audio, and scripts into final videos
- **Task Queuing**: Asynchronous task processing with Celery and Redis
- **REST API**: FastAPI-based endpoints for easy integration

## Project Structure

```
├── agents/                    # Multi-agent system components
│   ├── planner_agent.py      # Content planning and strategy
│   ├── script_agent.py       # Script generation
│   ├── hook_agent.py         # Hook optimization for engagement
│   ├── scene_agent.py        # Scene planning and descriptions
│   ├── visual_agent.py       # Visual concept generation
│   ├── eval_agent.py         # Content evaluation and feedback
├── app/                      # Application core
│   ├── main.py              # FastAPI application entry point
│   ├── config.py            # Configuration and settings
│   ├── dependencies.py      # Dependency injection
├── graph/                    # Workflow orchestration
│   └── workflow.py          # LangGraph pipeline definition
├── models/                   # Data schemas
│   └── schema.py            # Pydantic data models
├── services/                # External service integrations
│   ├── llm_service.py       # LLM API interactions
│   ├── image_service.py     # Image generation
│   ├── tts_service.py       # Text-to-speech
│   ├── video_service.py     # Video creation and editing
│   ├── rag_service.py       # Retrieval-augmented generation
│   ├── storage_service.py   # File storage management
├── utils/                    # Utility functions
│   └── prompts.py           # LLM prompt templates
├── workers/                  # Background task processing
│   └── task_queue.py        # Celery task definitions
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Technology Stack

- **Framework**: FastAPI + Uvicorn
- **AI/LLM**: Langchain, LangGraph, Google Gemini API
- **Task Queue**: Celery with Redis
- **Media Processing**: MoviePy, Pillow, Diffusers
- **Speech**: gTTS (Google Text-to-Speech)
- **ML Models**: Transformers, Torch
- **Database**: PostgreSQL
- **Search**: FAISS (Facebook AI Similarity Search)
- **Data Validation**: Pydantic

## Installation

### Prerequisites
- Python 3.8+
- Redis server
- PostgreSQL database
- Google Gemini API key

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-content-studio
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and set:
   - `GEMINI_API_KEY`: Your Google Gemini API key
   - `DATABASE_URL`: PostgreSQL connection string
   - `REDIS_URL`: Redis connection string (default: redis://localhost:6379)

## Usage

### Start the API Server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### API Endpoints

#### Generate Content
```bash
POST /generate
Content-Type: application/json

{
  "topic": "AI in Healthcare"
}
```

Returns:
```json
{
  "task_id": "12345-67890-abcde"
}
```

#### Home Endpoint
```bash
GET /
```

Returns:
```json
{
  "message": "AI Content Studio Running"
}
```

### Background Task Processing

Start the Celery worker:
```bash
celery -A workers.task_queue worker --loglevel=info
```

## Content Generation Pipeline

The system follows this workflow:

```
Topic Input
    ↓
[Planner Agent] → Plans content structure and key points
    ↓
[Script Agent] → Generates engaging script
    ↓
[Hook Agent] → Optimizes opening hook for engagement
    ↓
[Scene Agent] → Plans visual scenes and descriptions
    ↓
[Visual Agent] → Generates visual concepts
    ↓
[Image Service] → Creates/sources images
    ↓
[Audio Service] → Generates narration
    ↓
[Video Service] → Assembles final video
    ↓
[Eval Agent] → Evaluates quality and engagement
    ↓
Final Video Output
```

## Configuration

Edit `app/config.py` to customize:
- Model selection and parameters
- API keys and endpoints
- Feature toggles
- Default settings

## Development

### Code Structure Best Practices
- Agents in `agents/` handle AI logic
- Services in `services/` handle external integrations
- Models in `models/` define data structures
- Utils in `utils/` contain shared utilities

### Adding New Agents
1. Create a new file in `agents/`
2. Define the agent function with proper type hints
3. Add to the workflow in `graph/workflow.py`
4. Update the pipeline edges and connections

## Troubleshooting

### Redis Connection Issues
```bash
# Check if Redis is running
redis-cli ping
```

### Database Connection Issues
```bash
# Test PostgreSQL connection
psql -h localhost -U postgres
```

### Celery Worker Issues
```bash
# Check worker status
celery -A workers.task_queue inspect active
```

## Performance Considerations

- Async task processing prevents API blocking
- Redis caching for frequently accessed data
- Batch processing for multiple content requests
- GPU acceleration for image/video processing (if available)

## Future Enhancements

- [ ] Multi-language support
- [ ] Custom branding and watermarks
- [ ] Advanced video effects and transitions
- [ ] Analytics and performance metrics
- [ ] User authentication and content management
- [ ] Webhook notifications
- [ ] Batch job processing

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]

## Support

For issues, questions, or suggestions, please open an issue in the repository.
