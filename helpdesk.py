import csv


class Helpdesk:

    all = []

    def __init__(self, name: str, default_shifts: int, preference: str = None):
        self.name = name
        self.default_shifts = default_shifts
        self.preference = preference
        self.exclusions = Helpdesk.set_member_exclusions(self, file_name='holidays.csv')

        Helpdesk.all.append(self)

    @staticmethod
    def import_helpdesk_members(file_name):
        with open(file_name) as f:
            helpdesk_members = csv.DictReader(f)
            for member in helpdesk_members:
                if member['preference'] == '':
                    member['preference'] = None

                Helpdesk(
                    name=member['name'],
                    default_shifts=int(member['default_shifts']),
                    preference=member['preference']
                )

    def set_member_exclusions(self, file_name):
        with open(file_name) as f:
            helpdesk_holiday = csv.DictReader(f)
            person_holidays = []
            for member in helpdesk_holiday:
                if member['name'] == self.name:
                    person_holidays.append((member['day_of_week'], member['session']))
            return person_holidays

    def __repr__(self):
        return f"{self.name}, {self.default_shifts}, {self.preference}, {self.exclusions}"


Helpdesk.import_helpdesk_members('helpdesk_members.csv')

print(Helpdesk.all)
