# Python Flask Apache Ollama Docker Starter

## Summary
This is a super basic Docker setup for a Python flask application to connect to the host machine's GPU using NVIDIA CUDA drivers. 
It contains Apache as a web server with HTTP to HTTPS redirects with a self signed certificiate, a Flask application with a production WSGI, and Ollama for LLM inference.

## To Get Started
Make sure you have NVIDIA CUDA drivers installed on the host machine. You can install them via the `setup-host.sh` script in `scripts` if you are running Ubuntu 22.04.
We are making this assumptions for the NVIDIA drivers if you are using a different version you will have to modify the `setup-host.sh` script. Or find the correct drivers for your hostmachine and excute them independently.
```bash
cd scripts
./setup-host.sh
```
After installing the correct host machine drivers and GPU container support, you can either use the `start-dev.sh` or `start-prod.sh` in the same directory. Depending on if you need debugging suppport for the Flask application.

You can navigate to localhost or change your hosts file to contain a record to `yourdomain.com` to view the site locally.

## Disclaimer 
Initial Docker Compose build might take a few moments.
