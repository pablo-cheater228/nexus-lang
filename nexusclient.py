import time
import sys

print("00     0   000000    0   0     0     0    000000")
print("0 0    0   0          0 0      0     0    0     ")
print("0  0   0   000000      0       0     0    000000")
print("0   0  0   0          0 0      0     0         0")
print("0    000   000000    0   0     0000000    000000")
print("Welcome to Nexus client!")
while True:
    cmd = input("cmd>")
    parts = cmd.split()
    if cmd.lower() == "stop":
        sys.exit()
    elif cmd.lower() == "help":
        print("print [text] - prints a [text].")
        print("stop - stop the client.")
        print("wait [time] - waits a [time]")
    elif len(parts) >= 2 and parts[0].lower() == "print":
        printtxt = " ".join(parts[1:])
        print(printtxt)
    elif len(parts) >= 2 and parts[0].lower() == "wait":
        try:
            wait_time = float(parts[1])  # Преобразуем время ожидания в число
            time.sleep(wait_time)
            if len(parts) > 2:
                text_to_print = " ".join(parts[2:])
                print(text_to_print)

        except ValueError:
            print("ERROR: Enter a NUMBER")
            sys.exit()
        except Exception as e:
            print(f"ERROR: {e}")
            sys.exit()
    else:
        print("ERROR: Command not found.")
        sys.exit()
