# Parent image to be used
FROM python:3.7-alpine

# Create source directory for application and name it app
WORKDIR /app

# Copy everything in current pwd to src folder created
COPY . /app

# Install all requirements
RUN pip install -r requirements.txt

# Run the specified command within the container.
CMD [ "python", "manage.py runserver 0.0.0.0:8000" ]

