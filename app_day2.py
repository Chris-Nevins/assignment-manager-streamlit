import streamlit as st
# Be sure to run on terminal "streamlit run *file name*.py"
st.title("Course Management App")
st.header("Assignment Management")
st.subheader("Dashboard")

next_assignment_id_number = 3

st.divider()
st.markdown("----------")

#load data
assignments = [
    {
        "id":"HW1",
        "title":"intro to database",
        "description":"basics of database design",
        "points":100,
        "type":"homework"
    },
    {
        "id":"HW2",
        "title":"Normalization",
        "description":"normalizing",
        "points":100,
        "type":"homework"
    }
]

#input
#st.markdown("# Add New Assignment")
st.markdown("## Add New Assignment")
#st.markdown("### Add New Assignment")

title = st.text_input("Title")
description = st.text_area("Description",placeholder="normalization is covered here",
                           help="Here you are entering the assignment details")
points = st.number_input("Points")

#assignment_type = st.text_input("Assignment Type")
assignment_type = st.radio("Type", ("Homework", "Lab"), horizontal=True)
assignment_type2 = st.selectbox("Type", ("Select an option","Homework", "Lab", "other"))
if assignment_type2 == "other":
    assignment_type2 = st.text_input("Type", placeholder="Enter the assignment Type")

due_date = st.date_input("Due Date")

btn_save = st.button("Save", width="stretch", disabled=False)

import time
import json
from pathlib import Path

json_path = Path("assignments.json")


if btn_save:
    if not title:
        st.warning("Title needs to be provided!")
    else:
        with st.spinner("Assignment is being reached....."):
            time.sleep(5)

            new_assignment_id = "HW" + str(next_assignment_id_number)
            next_assignment_id_number += 1

            assignments.append(
                {
                    "id":new_assignment_id,
                    "title": title,
                    "description": description,
                    "points": points,
                    "type": assignment_type
                }
            )

            #record into json file
            with json_path.open("w",encoding="utf-8") as f:
                json.dump(assignments,f)

            st.success("New Assignement is recorded!")
            st.info("This is a new assignment")
            st.dataframe(assignments)