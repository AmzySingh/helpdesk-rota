import random

TIMES_OF_DAY = ['AM', 'PM']
DAYS_WEEK = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri']
sessions = [[i, j] for i in DAYS_WEEK for j in TIMES_OF_DAY]


class Sessions:

    all = []

    def __init__(self, day, time, assignee=None):
        self.day = day
        self.time = time
        self.assignee = assignee
        self.name = (day, time)

        Sessions.all.append(self)

    @classmethod
    def initialise_sessions(cls):
        for items in sessions:
            Sessions(
                day=items[0],
                time=items[1]
            )

    @staticmethod
    def assign_shift(session_obj, helpdesk_member):
        for member in helpdesk_member:
            while member.default_shifts > 0:
                unassigned = [i for i in session_obj.all if i.assignee is None]
                assigned = [i for i in session_obj.all if i.assignee == member.name]
                x = random.choice(unassigned)
                day = x.day
                checker = False
                for i in assigned:
                    if i.day == day:
                        checker = True
                if checker:
                    continue
                x.assignee = member.name
                member.default_shifts -= 1

    def __repr__(self):
        return f"{self.day}, {self.time}, {self.assignee}"


# Sessions.initialise_sessions()
#
# Sessions.assign_shift(Sessions, Helpdesk.all)
