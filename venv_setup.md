Sure, here's a cheat sheet for setting up a virtual environment for a Python project:

## Setting up a Virtual Environment in Python 3

### Prerequisites

Make sure you have Python 3 installed on your system.

You can check the version of Python 3 by running the following command in your terminal:

```sh
python3 --version
```

### Creating a Virtual Environment

1. Open your terminal and navigate to your project directory.

2. Create a new virtual environment using the following command:

```sh
python3 -m venv env
```

This command will create a new virtual environment named "env" in your project directory.

3. Activate the virtual environment using the following command:

```sh
source env/bin/activate
```

4. You should now see the name of your virtual environment in your terminal prompt.

### Installing Dependencies

1. Make sure your virtual environment is activated.

2. Install any required dependencies using pip:

```sh
pip install <package-name>
```

### Deactivating the Virtual Environment

To deactivate the virtual environment, simply run the following command:

```sh
deactivate
```

## Code Sample

Here's a simple code sample to test that your virtual environment is set up correctly:

```python
import sys

if __name__ == "__main__":
    print("Hello, world!")
    print(f"Python version: {sys.version}")
```

To run this code sample, make sure your virtual environment is activated and save the code to a file named `main.py`. Then, run the following command:

```sh
python main.py
```

You should see the message "Hello, world!" printed to your terminal, along with the version of Python you're using. If you see this output, your virtual environment is set up correctly and you're ready to start working on your Python project!
