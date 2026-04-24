import streamlit as st
from assignment_manager_oo.data.assignment_store import AssignmentStore
from assignment_manager_oo.services.assignment_manager import AssignementManager
from assignment_manager_oo.ui.assignment_dashboard import AssignmentDashboard

class AssignmentDashboard:
    def __init__(self, manager: AssignementManager, store: AssignmentStore) -> None:
        self.manager = manager
        self.store = store

    def main(self):
        if st.session_state["page"] == "dashboard":
            self.show_manager_assignments()
        else:
            self.show_add_new_assignment()

    def show_manager_assignments(self):
        pass

    def show_add_new_assignment(self):
        pass