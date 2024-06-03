import os
import zipfile
import google.generativeai as genai
import typer
from pathlib import Path
from dotenv import load_dotenv

app = typer.Typer()

def load_env():
    if os.getenv("GOOGLE_API_KEY") is None:
        load_dotenv()
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        raise EnvironmentError("GOOGLE_API_KEY must be set in the environment or .env file")
    genai.configure(api_key=google_api_key)
    return google_api_key

def generate_file_structure(prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f"Generate a file structure for the following application:\n{prompt}")
    print("Response data for file structure generation:", response.text)
    return response.text.strip()


def generate_file_contents(filename, file_structure, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(
        f"Generate the content for the file {filename} based on the following file structure and requirements:\nFile Structure:\n{file_structure}\nRequirements:\n{prompt}")

    if hasattr(response, 'text'):
        print(f"Response data for file content generation of {filename}:", response.text)
        return response.text
    else:
        print(f"Warning: Unexpected response type for file {filename}. Text content unavailable.")
        return ""


def save_file(filename, content, app_folder):
    file_path = os.path.join(app_folder, filename)
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(file_path, 'w') as f:
        # Remove ```python tag at the beginning and ``` at the end
        f.write(content.strip('```python').strip('```'))

def zip_files(files):
    with zipfile.ZipFile('generated_application.zip', 'w') as zf:
        for file in files:
            zf.write(file)

@app.command()
def main():
    google_api_key = load_env()
    user_input = input("What application do you want to build? ")
    app_folder = 'generated_app'
    if not os.path.exists(app_folder):
        os.makedirs(app_folder)
    try:
        file_structure = generate_file_structure(user_input)
        print("Generated File Structure:\n", file_structure)

        file_list = []
        for line in file_structure.split('\n'):
            line = line.strip()
            if line and not line.startswith('#'):
                if '├──' in line or '└──' in line:
                    filename = line.split('──')[-1].strip()
                    if filename and not filename.endswith('/'):
                        file_list.append(filename)

        file_list = file_list[:20]  # Limit to 20 files
        print("Files to generate:", file_list)

        generated_files = []
        for filename in file_list:
            print(f"Generating content for {filename}...")
            file_content = generate_file_contents(filename, file_structure, user_input)
            file_path = os.path.join(app_folder, filename)
            save_file(filename, file_content, app_folder)
            generated_files.append(file_path)

        zip_files(generated_files)
        print("Application files have been generated and zipped into 'generated_application.zip'")

    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    app()
