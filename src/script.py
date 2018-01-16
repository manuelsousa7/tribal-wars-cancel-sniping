import sys
import datetime
import re


def get_hours(arg):
	(h, m, s) = arg.split(':')
	return int(h)

def get_minutes(arg):
	(h, m, s) = arg.split(':')
	return int(m)

def get_seconds(arg):
	(h, m, s) = arg.split(':')
	return int(s)


def main():
	if(len(sys.argv) != 4):
		print("error")
		sys.exit()

	arrivalATSUPtime = datetime.timedelta(hours=get_hours(sys.argv[1]), minutes=get_minutes(sys.argv[1]), seconds=get_seconds(sys.argv[1]))
	ATSUPtimeduration = datetime.timedelta(hours=get_hours(sys.argv[2]), minutes=get_minutes(sys.argv[2]), seconds=get_seconds(sys.argv[2]))
	NTarrivaltime = datetime.timedelta(hours=get_hours(sys.argv[3]), minutes=get_minutes(sys.argv[3]), seconds=get_seconds(sys.argv[3]))

	count = datetime.timedelta()

	count = (NTarrivaltime - (arrivalATSUPtime - ATSUPtimeduration)) / 2 + (arrivalATSUPtime-ATSUPtimeduration) # Algorithm

	return str(count)


if __name__ == "__main__":
    print main()