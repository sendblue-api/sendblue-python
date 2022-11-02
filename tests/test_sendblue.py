import os
from sendblue.sendblue import Sendblue
from dotenv import load_dotenv

load_dotenv()

apiKey = os.environ.get("SENDBLUE_TEST_API_KEY")
if apiKey is None:
    print("Please set the SENDBLUE_TEST_API_KEY environment variable to run the tests")
    exit(1)

apiSecret = os.environ.get("SENDBLUE_TEST_API_SECRET")
if apiSecret is None:
    print("Please set the SENDBLUE_TEST_API_SECRET environment variable to run the tests")
    exit(1)

test_number_1 = os.environ.get("TEST_NUMBER_1")
if test_number_1 is None:
    print("Please set the TEST_NUMBER_1 environment variable to run the tests")
    exit(1)

test_number_2 = os.environ.get("TEST_NUMBER_2")
if test_number_2 is None:
    print("Please set the TEST_NUMBER_2 environment variable to run the tests")
    exit(1)


def test_send_single_message():
    """Test that messages are sent correctly to a single number"""
    sendblue = Sendblue(apiKey, apiSecret, {"log_level": 'debug'})
    response = sendblue.send_message(test_number_1, {
        'content': 'Hello from Sendblue!',
        'send_style': 'invisible',
        'media_url': 'https://source.unsplash.com/random.png',
        'status_callback': 'https://example.com/callback'
    })
    assert response['status'] == 'QUEUED'

def test_send_group_message():
    """Test that messages are sent correctly to a group"""
    sendblue = Sendblue(apiKey, apiSecret, {"log_level": 'debug'})
    response = sendblue.send_group_message({
        'numbers': [test_number_1, test_number_2],
        'content': 'Hello from Sendblue!',
        'send_style': 'invisible',
        'media_url': 'https://source.unsplash.com/random.png',
        'status_callback': 'https://example.com/callback'
    })
    assert response['status'] == 'QUEUED'
