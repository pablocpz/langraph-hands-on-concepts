import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pathlib import Path

# Define colors for each participant
colors = {
    "SYSTEM_MESSAGE": "blue",
    "HUMAN_MESSAGE": "green",
    "AGENT_GRAPH": "orange",
    "TOOL_MESSAGE": "purple",
    "AI_MESSAGE": "red"
}

# Define the messages and who says each one
conversation = [
    ("SYSTEM_MESSAGE", "You are a smart research assistant..."),
    ("HUMAN_MESSAGE", "Who is YannLeCun? Make a bullet point comparison between him and Marie Curie."),
    ("AGENT_GRAPH", "Entering call_openai() inside llm..."),
    ("AGENT_GRAPH", "Checking take_action()..."),
    ("TOOL_MESSAGE", "Calling: {'name': 'tavily_search_results_json', 'args': {'query': 'Yann LeCun'}}"),
    ("TOOL_MESSAGE", "Calling: {'name': 'tavily_search_results_json', 'args': {'query': 'Marie Curie'}}"),
    ("AI_MESSAGE", "YannLeCun: Professor of Data Science, Computer Science, Marie Curie: Discoverer of polonium and radium, Received two Nobel Prizes..."),
    ("AI_MESSAGE", "### Funny Haiku:\nYann and Marie bright,\nAI to radioactivity,\nScience makes them right."),
]

# Initialize the plot
fig, ax = plt.subplots()
ax.axis('off')  # Turn off the axis

# Initialize text objects
text_objects = []

def init():
    """Initialize the text on the plot"""
    for i, (role, msg) in enumerate(conversation):
        text_obj = ax.text(0.02, 1 - i * 0.15, '', color=colors[role], fontsize=12, va='top')
        text_objects.append(text_obj)
    return text_objects

def update(frame):
    """Update function for animation that types one character at a time."""
    # Clear previous text for each update
    for text_obj in text_objects:
        text_obj.set_text('')

    # Determine which message and how many characters to display
    current_text_idx = frame // 50  # Each message takes 50 frames to complete typing
    current_char_idx = frame % 50   # Position within the message

    # Loop through each message and update text on the figure
    for i in range(current_text_idx + 1):
        role, message = conversation[i]
        if i == current_text_idx:
            # Show message up to current character index
            partial_message = message[:current_char_idx]
            text_objects[i].set_text(partial_message)
        else:
            # Show full message for previous conversations
            text_objects[i].set_text(message)

    return text_objects

# Set up animation
ani = animation.FuncAnimation(fig, update, frames=range(len(conversation) * 50), init_func=init, blit=True)

# Define output path for the gif
output_path = Path("chatgpt_style_conversation.gif")

# Save the animation
ani.save(output_path, writer="pillow", fps=10)

# Provide path for download
output_path
