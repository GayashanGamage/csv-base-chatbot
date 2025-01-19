# Chatbot bass on csv file

This is a simple Python script to chat with csv files and get output in your native language.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone <repository_url>

 2. **Create and activate a virtual environment**

      ```
       python3 -m venv .venv  # Create a virtual environment named .venv
       Scripts\activate  # Activate the virtual environment  
      ```


3. **Install dependencies:**
  ```
  pip install -r requirements.txt
  ```

4. **Create .env file**
    this program use **gemini-1.5-pro** LLM model.
    get your gemini-1.5-pro api-key [from hear](https://ai.google.dev/gemini-api/docs/api-key)
    then create variable exactly like this and assign the api-key
    ```
    api = 'your api key'
    ```

4. **Run the project**
    ```
    python main.py  # Replace 'main.py' with the name of your main script
    ```
## How to interact with script ?
   when you run the program there will be main menu that you can select options to several options

   1. Enter query
   2. Load another dataset - csv files only
   3. Print dataset that you select from above file
   4. Exit from program

  type the option number that you want. sometimes you may get sub menus. those also work with option numbers.

## Features
  1. select your own csv files
  2. directly see the dataset inside of the command prompt
  3. interect with your native language
