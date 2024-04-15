# Deploying-LLMs-using-Langserve

# Langchain LLM Client

This repository contains a Python client script designed to interact with a FastAPI server utilizing the Langchain and Langserve libraries to generate language model outputs such as essays and poems based on specific topics.

## Prerequisites

Before running the client script, ensure that you have the following:
- Python 3.7 or higher installed on your system.
- `requests` library installed in your Python environment. You can install it using pip:
  ```bash
  pip install requests
  ```

## Setup

1. **Clone the Repository**
   Clone this repository to your local machine using git:
   ```bash
   git clone https://github.com/anishgillella/Deploying-LLMs-using-Langserve.git
   cd Deploying-LLMs-using-Langserve
   ```

2. **Environment Variables**
   - Ensure that the FastAPI server is running and accessible. The client assumes the server is accessible at `http://localhost:8000`.
   - No specific environment variables need to be set for the client script.

3. **Running the FastAPI Server**
   - Ensure your FastAPI server that handles the LLM requests is running. Please refer to the corresponding repository/documentation on how to start the server.

## Usage

The client script is straightforward to use. It sends a POST request to the FastAPI server and retrieves the generated text based on the provided topic.

- **Run the Client Script**
  Execute the script using Python from your terminal:
  ```bash
  python client.py
  ```

- **Expected Output**
  The script will output the JSON response from the server and print the content of the generated essay or poem directly to the terminal.

## Client Script Explanation

- `client.py` contains code that makes a POST request to the `/essay/invoke` endpoint of your FastAPI server, submits a JSON payload with a topic, and prints the response.
- The script is currently configured to request an essay about "Hitler". Modify the `json` parameter in the `requests.post()` call to change the topic or target different endpoints (like poems).

## Contributing

Contributions are welcome! Please feel free to submit pull requests, create issues for bugs, or suggest enhancements.
