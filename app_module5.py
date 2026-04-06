import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import uuid
import time

st.set_page_config(page_title="Course Management", page_icon="", layout="centered", initial_sidebar_state="collapsed")

st.title("Course Management")
st.divider()

assignments = [
{
"id": "HW1",
"title": "Intro to Database",
"description": "basics of database design",
"points": 100,
"type": "homework"
},
{
"id": "HW2",
"title": "Normalization",
"description": "normalizing",
"points": 100,
"type": "homework"
}
]

json_path = Path("assignments.json")

if json_path.exists():
    with open(json_path, "r") as f:
        assignments = json.load(f)

if "page" not in st.session_state:
    st.session_state["page"] = "Assignment Dashboard"

if "draft" not in st.session_state:
    st.session_state["draft"] = {}

if st.session_state["page"] == "Assignment Dashboard":
    col1, col2 = st.columns([3,1])

    with col1:
        st.subheader("Assignments")
    with col2:
        if st.button("Add New Assignment", key="add_new_assignment_btn", type="primary", use_container_width=True):
            st.session_state["page"] = "Add New Assignment"
            st.rerun()

    with st.container(border=True):
        st.dataframe(assignments)

elif st.session_state["page"] == "Add New Assignment":
    col1,col2 = st.columns([3,1])

    with col1:
        st.subheader("Add New Assignment")
    with col2:
        if st.button("Return", key="back_btn", type="secondary"):
            st.session_state["page"] = "Assignment Dashboard"
            st.rerun()

    st.session_state['draft']['title'] = st.text_input("Title", key="title_txt_input")
    st.session_state['draft']['description'] = st.text_area("Description", key="description_txt_input",
    placeholder="normalization is covered here",
    help="Here you are entering the assignment details")
    st.session_state["draft"]['points'] = st.number_input("Points", key="points_input")
    st.session_state["draft"]['assignment_type'] = st.selectbox("Type", ["Select and Option", "Homework", "Lab", "other"], key="type_selector")

    if st.button("Save", key="save_btn", type="primary", use_container_width=True):
        with st.spinner("In Progress...."):
            time.sleep(3)

            assignments.append(
                {
                    "id": str(uuid.uuid4()),
                    "title": st.session_state["draft"]["title"],
                    "description": st.session_state["draft"]["description"],
                    "points": st.session_state["draft"]["points"],
                    "type": st.session_state["draft"]["assignment_type"]
                }
            )

            with open(json_path, "w") as f:
                json.dump(assignments, f)
            
            st.success("Assignment is recorded.")
            time.sleep(3)

            st.session_state["page"] = "Assignment Dashboard"
            st.rerun()

elif st.session_state["page"] == "Edit Assignment":
    pass

