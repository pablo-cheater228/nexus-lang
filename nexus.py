import sys
import os
import time

def execute_command(command):
    parts = command.split()
    if parts[0].lower() == "print":
        print(" ".join(parts[1:]))
    elif parts[0].lower() == "wait":
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

def parse_and_execute_file(filename):
    if not filename.lower().endswith(".nxs"):
        print(f"Error: File ‘{filename}’ must have the ‘.nxs’ extension.")
        return

    if not os.path.exists(filename):
        print(f"Error: File ‘{filename}’ not found.")
        return

    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    execute_command(line)
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]  # Получаем имя файла из аргументов командной строки
        parse_and_execute_file(filename)
    else:
        print("Error: Please specify an .nxs file as an argument.")