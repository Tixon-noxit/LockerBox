# Makefile

# Set the name of the virtual environment
VENV_NAME := env

# Python command
PYTHON := python3

# Targets

# Create a virtual environment
venv:
	$(PYTHON) -m venv $(VENV_NAME)

# Activate the virtual environment (Unix/Linux/Mac)
activate:
	source $(VENV_NAME)/bin/activate

# Activate the virtual environment (Windows)
activate_win:
	$(VENV_NAME)\Scripts\activate

# Install dependencies from requirements.txt
install:
	$(PYTHON) -m pip install -r requirements.txt

# Clean up the virtual environment directory
clean:
	rm -rf $(VENV_NAME)

