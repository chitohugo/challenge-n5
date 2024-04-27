FROM python:3.10-buster

# Set work directory
WORKDIR /challenge

# Set env variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH=/challenge

# Install dependencies
COPY requirements.txt /challenge/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /challenge/

# Run up
RUN chmod +x /challenge/entrypoint.sh
ENTRYPOINT /challenge/entrypoint.sh