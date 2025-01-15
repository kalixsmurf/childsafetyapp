import requests

def test_flask_api():
    url = "http://127.0.0.1:5000/process"

    payload = {
        "path": "03-01-03-01-01-01-18.wav" #Here, the path that will be sent should be the relative path with respect to the server.py file
    }

    """
    For example, if the child safety app(the one with tkinter) is running in a folder named "app"
    The server.py file is running in a folder named "backend"
    The ml related files exist in a folder named "ml"
    And the audio files are recorded directly to the project root
    So, the overall project file structure is the following:
    
    project_root
    |
    --> ml
    |    |
    |   --> ml files
    |    
    --> backend
    |    |
    |    --> server.py
    |    
    --> app
    |    |
    |    --> app.py
    |    
    --> sample_audio.wav

    Then, the path that is sent by the client, should be "../sample_audio.wav" as the audio file is in the parent folder of backend folder.
    """

    try:
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            print("Success:", response.json())
        else:
            print(f"Failed with status code {response.status_code}: {response.text}")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    test_flask_api()
