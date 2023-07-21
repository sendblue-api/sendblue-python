# Sendblue Python Library

## Overview

This package is a Python wrapper for the Sendblue API. It provides a simple interface for sending and receiving messages.

## Prerequisites

You will need to get API keys by signing up for a Sendblue account. You can do so [here](https://sendblue.co/).

## Installation

```bash
pip install sendblue
```

## Usage

### Initializing

```python
from sendblue import Sendblue

# Load your key from an environment variable or secret management service
# (do not include your key directly in your code)
SENDBLUE_API_KEY = os.environ.get('SENDBLUE_API_KEY')
SENDBLUE_API_SECRET = os.environ.get('SENDBLUE_API_SECRET')

sendblue = Sendblue(SENDBLUE_API_KEY, SENDBLUE_API_SECRET)
```

### Send Message

```python
response = sendblue.send_message('+19998887777', 'Hello from Sendblue!', send_style='invisible', media_url='https://source.unsplash.com/random.png', status_callback='https://example.com/callback')
```

### Send Group Message

```python
response = sendblue.send_group_message(['+19998887777', '+19998887778'], 'Hello from Sendblue!', send_style='invisible', media_url='https://source.unsplash.com/random.png', status_callback='https://example.com/callback')
```

### Modify Group

```python
response = sendblue.modify_group('group_id', 'add_recipient', '+19998887777')
```

### Lookup Number

```python
response = sendblue.lookup('+19998887777')
```

### Send Typing Indicator

```python
response = sendblue.send_typing_indicator('+19998887777')
```