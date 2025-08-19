#!/bin/bash

rasa run --enable-api --cors "*" --port 5005 &
rasa run actions --port 5055 &
streamlit run home.py --server.port ${PORT: -8501} --server.address 0.0.0.0