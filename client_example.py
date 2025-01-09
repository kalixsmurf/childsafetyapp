import requests

def test_flask_api():
    url = "http://127.0.0.1:5000/process"

    payload = {
        "path": "/test.mp3"
    }

    try:
        response = requests.post(url, json=payload)

        # Print the response
        if response.status_code == 200:
            print("Success:", response.json())
        else:
            print(f"Failed with status code {response.status_code}: {response.text}")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    test_flask_api()
