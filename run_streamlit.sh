#!/bin/bash
app='/mnt/c/workspace/git/mendeley_API/pages/main.py'
streamlit run $app --server.port=5000 --server.baseUrlPath='opath'
