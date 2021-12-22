from os import sep
import sys
import datetime

# help function


def help():
    sa = """Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text \"hello world\" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics"""
    sys.stdout.buffer.write(sa.encode('utf8'))

# function to add item in task list


def add(priority, task):
    f = open('task.txt', 'a')
    f.write(task + " " + "[" + priority + "]")
    f.write("\n")
    f.close()
    task = '"'+task+'"'
    print(f"Added task: {task} with priority {priority}")

# function to print the task list items


def ls():
    try:
        nec()
        l = len(d)
        k = l

        for i in d:
            sys.stdout.buffer.write(
                f"{i}. {d[i]}".encode('utf8'))

            sys.stdout.buffer.write("\n".encode('utf8'))
            l = l-1

    except Exception as e:
        raise e

# function to complete a task


def done(no):
    try:
        nec()
        no = int(no)
        f = open('done.txt', 'a')
        st = d[no]

        f.write(st)
        f.write("\n")
        f.close()
        print(f"Marked item as done.")

        with open("task.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)

            for i in lines:
                if i.strip('\n') != d[no]:
                    f.write(i)
            f.truncate()
    except:
        print(f"Error: no incomplete item with index #{no} exists.")

# function to show report/statistics of task list


def report():
    nec()
    try:
        nf = open('done.txt', 'r')
        c = 1

        for line in nf:
            line = line.strip('\n')
            don.update({c: line})
            c = c+1

        print(
            f'Pending : {len(d)}'
        )
        for key, value in d.items():
            print(f"{key}. {value}")

        print('\n')

        print(
            f'Completed : {len(don)}'
        )
        for key, value in don.items():
            print(f"{key}. {value[:-3]}")

    except:
        print(
            f'Pending : {len(d)}'
        )
        for key, value in d.items():
            print(f"{key}. {value}")
        print('\n')
        print(
            f'Completed : {len(don)}'
        )
        for key, value in don.items():
            print(f"{key}. {value}[:-3]")


# function to delete an item from task list


def deL(no):
    try:
        no = int(no)
        nec()

        with open("task.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)

            for i in lines:
                if i.strip('\n') != d[no]:
                    f.write(i)

            f.truncate()

        print(f"Deleted task #{no}")

    except Exception as e:
        print(f"Error: task with index #{no} does not exist. Nothing deleted.")

# utility function nec()


def nec():
    try:
        f = open('task.txt', 'r')
        c = 1
        for line in f:
            line = line.strip('\n')
            d.update({c: line})
            c = c+1

    except:
        sys.stdout.buffer.write("There are no pending tasks!".encode('utf8'))


# Main function
if __name__ == '__main__':
    try:
        d = {}
        don = {}
        args = sys.argv

        if(args[1] == 'del'):
            args[1] = 'deL'

        if(args[1] == 'add' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing tasks string. Nothing added!".encode('utf8')
            )

        elif(args[1] == 'done' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing NUMBER for marking tasks as done.".encode(
                    'utf8')
            )

        elif(args[1] == 'deL' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing NUMBER for deleting tasks.".encode('utf8')
            )

        else:
            globals()[args[1]](*args[2:])

    except Exception as e:
        s = """Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text \"hello world\" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics"""
        sys.stdout.buffer.write(s.encode('utf8'))
