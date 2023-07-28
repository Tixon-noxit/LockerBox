# Makefile

VENV_NAME = env
PYTHON = python3
PIP = $(VENV_NAME)/bin/pip

.PHONY: install clean

install: $(VENV_NAME)

clean:
	@echo "Cleaning up..."
	rm -rf $(VENV_NAME)

$(VENV_NAME):
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV_NAME)
	$(PIP) install --upgrade pip
