# Job Search Agent

Are you struggling to find the right job opportunities? Does your resume need a boost to stand out? Job Search Agent is your AI-powered companion that helps you discover relevant job listings and transforms your resume to match what employers are looking for. Whether you're starting your career or making a transition, our intelligent agent works with you to increase your chances of landing your dream job.

## Access the App

You can access the live application here: **[INSERT DEPLOYED URL HERE]**

## Features

- **Job Search**: Search and discover job opportunities
- **Resume Optimization**: Get AI-powered suggestions to optimize your resume for target roles

## Setup Instructions for Developers

### Prerequisites

- Python 3.8+
- Git
- An LLM API key (OpenAI, Anthropic, or similar)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/job-search-agent.git
   cd job-search-agent
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**
   - Create a `.env` file in the root directory:
     ```bash
     touch .env
     ```
   - Add your LLM API key to the `.env` file:
     ```
     LLM_API_KEY=your_api_key_here
     ```

5. **Run the app**
   ```bash
   streamlit run streamlit_app.py
   ```

The app will open in your default browser at `http://localhost:8501`

## Development

To contribute or modify the app:

1. Activate the virtual environment
2. Make your changes
3. Test locally with `streamlit run streamlit_app.py`
4. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
