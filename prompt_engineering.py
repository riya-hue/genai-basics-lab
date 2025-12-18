def build_prompt(topic):
    return f"""
    Explain {topic}
    - definition
    - example
    - use case
    """

print(build_prompt("Agentic AI"))
