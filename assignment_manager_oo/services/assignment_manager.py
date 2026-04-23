from typing import List, Dict, Optional

class AssignementManager:
    def __init__(self, inital_assignements: List[Dict]) -> None:
        self.assignments = inital_assignements

    def all(self) -> List[Dict]:
        return list(self.assignments)

    def add(self, title: str, description: str, points: int, 
            assignment_type: str):
        pass

    def delete(self, assignment_id: str):
        pass