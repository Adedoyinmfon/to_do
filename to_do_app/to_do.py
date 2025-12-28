tasks = []
while True:
    task = input("Your task (or the word 'done' to end):")
    if task == "done":
        break
    tasks.append(task)

file = open("tasks.txt", "w")
for task in tasks:
    file.write(task + "\n")

file.close()

print("Tasks saved to file!")
