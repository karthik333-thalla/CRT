def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    average = (n1 + n2 + n3) / 3
    
    # Truncate to 2 decimal places (not round)
    average = int(average * 100) / 100

    if average >= 40:
        status = "Pass"
    else:
        status = "fail"

    return f"Average grade: {average}, Status: {status}"