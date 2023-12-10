# Use a base image
FROM continuumio/miniconda3

# Set the working directory
WORKDIR /app

# Copy the project files to the working directory
COPY . .

# Create conda environment using the environment.yml file
RUN conda env create -f environment.yml

# Ensure environment is activated when container starts
RUN echo "conda activate rc" >> ~/.bashrc
