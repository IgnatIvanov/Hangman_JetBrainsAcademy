def what_to_do(instructions):
    if instructions.startswith("Simon says") or instructions.endswith("Simon says"):
        instructions = "I " + instructions.replace("Simon says", "")
        instructions = instructions.replace("  ", " ")
        return instructions
    else:
        return "I won't do it!"