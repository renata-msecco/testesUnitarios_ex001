from src.models.store import Store
from src.models.user import User


class ServiceUser:
    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):
        if not isinstance(name, str) or not isinstance(job, str):
            return "Invalid parameters"

        if not name or not job:
            return "Empty parameters not allowed"

        if self.search_user(name) is not None:
            return "User already exists"

        user = User(name, job)
        self.store.bd.append(user)
        return "User added"

    def remove_user(self, name, job):
        get_user = self.search_user(name)

        if not isinstance(name, str) or not isinstance(job, str):
            return "Invalid parameters"

        if not name or not job:
            return "Empty parameters not allowed"

        if get_user is not None:
            self.store.bd.remove(get_user)
            return "User removed"

        return "User does not exist"

    def search_user(self, name):
        if not isinstance(name, str):
            return "Invalid parameters"

        if not name:
            return "Empty parameters not allowed"

        for stored_user in self.store.bd:
            if stored_user.name == name:
                return stored_user
            else:
                return None

    def get_user_by_name(self, name):
        if not isinstance(name, str):
            return "Invalid parameters"

        if not name:
            return "Empty parameters not allowed"

        for stored_user in self.store.bd:
            if stored_user.name == name:
                return stored_user.job
            else:
                return None

    def update_user(self, old_name, new_name):
        if not isinstance(old_name, str):
            return "Invalid parameters"

        if not old_name:
            return "Empty parameters not allowed"

        for stored_user in self.store.bd:
            if stored_user.name == old_name:
                stored_user.name = new_name
                return "Name updated"

        return "User does not exist"
