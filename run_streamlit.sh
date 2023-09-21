#!/bin/bash
source ~/miniconda3/bin/activate mendeley
app='/mnt/c/workspace/mendeley_API/Main.py'
streamlit run $app --server.port=5000 --server.baseUrlPath='oauth'
