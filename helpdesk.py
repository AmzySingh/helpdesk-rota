import csv


class Helpdesk:

    all = []

    def __init__(self, name, default_shifts, preference=None, exclusions=None):
        self.name = name
        self.default_shifts = default_shifts
        self.preference = preference
        self.exclusions = exclusions

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

    def __repr__(self):
        return f"{self.name}, {self.default_shifts}, {self.preference}, {self.exclusions}"
