# Deploying an App for Real-Time Day Trading Analytics with AI Agents, Groq, DeepSeek, and AWS for Monetization


## How to deploy on AWS
* Create an instance using the EC2 (similar to project 1);
* On terminal, download Anaconda: wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
* pip install -r requirements.txt
* nohup streamlit run app.py --server.port=8501 --server.address=0.0.0.0 &