import sys
live_speed_file = '/data/live_speed_file'

def write_file(a):
    speed = open(live_speed_file, "r")
    modified_speed=float(speed.read())+a
    with open(live_speed_file, 'w') as f:
        f.write(str(modified_speed))

if __name__ == "__main__":
    write_file(int(sys.argv[1]))