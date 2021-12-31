from helpdesk import Helpdesk
from sessions import Sessions
from output import create_output_file

Helpdesk.import_helpdesk_members('helpdesk_members.csv')

Sessions.initialise_sessions()

Sessions.assign_shift(Sessions, Helpdesk.all)

create_output_file()
