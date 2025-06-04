# Use a base Jupyter notebook image
FROM jupyter/scipy-notebook:python-3.11.6

# Switch to root for installations
USER root

# Update system packages to reduce vulnerabilities
RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY infrastructure/requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copy notebook and data
WORKDIR /home/jovyan/work
COPY funMath_deploy.ipynb ./
COPY images/ ./images/
COPY utils.py ./utils.py

# Configure JupyterLab to start without authentication
ENV JUPYTER_ENABLE_LAB=yes

# Copy and set up entrypoint script
COPY infrastructure/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
