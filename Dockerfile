FROM python:slim

# Copy project
COPY . /app

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip install .

# Run the application
CMD ["python", "-m", "fzisy"]
