def reorderLogFiles(logs: list[str]) -> list[str]:
    letter_logs = []
    digit_logs = []
    
    # 1. Separate logs into respective containers
    for log in logs:
        # maxsplit=1 splits only at the first space instance
        identifier, content = log.split(" ", 1)
        
        if content[0].isdigit():
            digit_logs.append(log)
        else:
            letter_logs.append(log)
            
    # 2. Sort letter_logs dynamically using a tuple key
    # (Primary Sort: Content, Secondary Sort: Identifier)
    letter_logs.sort(key=lambda log: (log.split(" ", 1)[1], log.split(" ", 1)[0]))
    
    # 3. Concatenate and return complete list
    return letter_logs + digit_logs

test_logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
result = reorderLogFiles(test_logs)
print("The input is:", test_logs)
print("The output is:", result)
