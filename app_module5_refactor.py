import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import uuid
import time

# Data layer
def load_data(json_path):
    if json_path.exists():
        with open(json_path, "r") as f:
            assignments = json.load(f)
    else:
        assignments = []
    
    return assignments

def save_data(assignments, json_path):
    with open(json_path, "w") as f:
        json.dump(assignments, f)

# service layer
