import requests


def dog_photo() -> str:
    """Get a random dog photo from the internet.

    Returns:
        str: URL of the dog photo.
    """
    url = 'https://random.dog/woof.json'

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['url']

    return
