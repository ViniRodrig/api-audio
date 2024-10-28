# Use an official Python runtime as a parent image
FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app

# Install any needed packages specified in requirements.txt
COPY . /app

RUN pip install --no-cache-dir openai requests flask gunicorn


# Run app.py when the container launches
# CMD ["python", "app.py"]
CMD ["gunicorn", "--workers=10", "app:app", "-b", "0.0.0.0:5000"]

# docker build -t sql-injection . -f Dockerfile
# docker tag sql-injection:latest registry.ctf.secompufscar.com.br/sql-injection:latest
# docker push registry.ctf.secompufscar.com.br/sql-injection:latest

