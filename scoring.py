def calculate_score():
    current_deadline = input("Enter the current deadline (1-3): ")
    mandatory_tasks = []
    optional_tasks = []
    task_scores = []
    total_score = 0
    task_type = ""
    while task_type != "done":
        task_type = input("Enter task type (mandatory/optional) or 'done' to finish: ")
        if task_type != "done":
            task_score = int(input("Enter task score: "))
            task_scores.append(task_score)
            task_date = int(input("Enter task completion date: "))
            if task_type == "mandatory":
                mandatory_tasks.append(task_date)
            elif task_type == "optional":
                optional_tasks.append(task_date)
    for i, task_date in enumerate(mandatory_tasks):
        score = 0
        if task_date <= int(current_deadline):
            if int(current_deadline) == 1:
                score = task_scores[i] * 100 / 100
            elif int(current_deadline) == 2:
                score = task_scores[i] * 65 / 100
            elif int(current_deadline) == 3:
                score = task_scores[i] * 50 / 100
            total_score += score
        else:
            score = 0

    optional_score = 0
    for i, task_date in enumerate(optional_tasks):
        if task_date <= int(current_deadline):
            if int(current_deadline) == 1:
                score = task_scores[i] * 100 / 100
                optional_score += score
            elif int(current_deadline) == 2:
                score = task_scores[i] * 65 / 100
                optional_score += score
            elif int(current_deadline) == 3:
                score = task_scores[i] * 50 / 100
                optional_score += score

    # Calculate the percentage score
    max_score = sum(task_scores)
    percentage_score = total_score / max_score * 100
    if optional_score > 0:
        percentage_score += percentage_score * (optional_score / max_score)
    return percentage_score

score = calculate_score()
print("The project score is: {:.2f}%".format(score))