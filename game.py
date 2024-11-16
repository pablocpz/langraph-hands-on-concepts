

# import pygame
# import sys

# # Initialize Pygame
# pygame.init()

# # Set up the display
# SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("ChatGPT-like Conversation Animation")

# # Colors
# BACKGROUND_COLOR = (255, 250, 240)
# SYSTEM_COLOR = (100, 100, 100)      # Gray for system messages
# HUMAN_COLOR = (0, 102, 204)         # Color for the human's text
# AGENT_GRAPH_COLOR = (255, 165, 0)   # Orange for agent graph messages
# TOOL_MESSAGE_COLOR = (255, 215, 0)  # Gold for tool messages
# AI_COLOR = (102, 51, 153)           # Color for the AI's text
# FONT_COLOR = (0, 0, 0)

# # Font
# FONT_SIZE = 24
# font = pygame.font.Font(None, FONT_SIZE)
# screen.fill(BACKGROUND_COLOR)

# # Define messages for the chat sequence
# messages = [
#     ("SYSTEM_MESSAGE", "You are a smart research assistant..."),
#     ("HUMAN_MESSAGE", "Who is Yann LeCun? Make a bullet point comparison between him and Marie Curie."),
#     ("AGENT_GRAPH", "Entering call_openai() inside llm..."),
#     ("AGENT_GRAPH", "Checking take_action()..."),
#     ("TOOL_MESSAGE", "Calling: {'name': 'tavily_search_results_json', 'args': {'query': 'Yann LeCun'}}"),
#     ("TOOL_MESSAGE", "Calling: {'name': 'tavily_search_results_json', 'args': {'query': 'Marie Curie'}}"),
#     ("AI_MESSAGE", "### Yann LeCun:\n- Professor and director of AI research at Facebook\n- Silver Professor at NYU\n- Works on AI, machine learning, computer vision, robotics, and image compression"),
#     ("AI_MESSAGE", "### Marie Curie:\n- Discoverer of polonium and radium\n- Received two Nobel Prizes\n- Championed the use of radiation in medicine"),
#     ("AI_MESSAGE", "### Funny Haiku:\nYann and Marie bright,\nAI to radioactivity,\nScience makes them right."),
# ]

# # Assign colors to each sender
# sender_colors = {
#     "SYSTEM_MESSAGE": SYSTEM_COLOR,
#     "HUMAN_MESSAGE": HUMAN_COLOR,
#     "AGENT_GRAPH": AGENT_GRAPH_COLOR,
#     "TOOL_MESSAGE": TOOL_MESSAGE_COLOR,
#     "AI_MESSAGE": AI_COLOR
# }

# class MessageTypewriter:
#     def __init__(self, sender, message, color, font, max_width):
#         self.sender = sender
#         self.message = message
#         self.color = color
#         self.font = font
#         self.max_width = max_width
#         self.lines = []
#         self.rendered_lines = []
#         self.current_line_index = 0
#         self.current_char_index = 0
#         self.finished = False
#         self.surface = None
#         self.prepare_lines()

#     def prepare_lines(self):
#         prefix = f"{self.sender}: "
#         full_text = prefix + self.message
#         words = full_text.split(' ')
#         line = ''
#         for word in words:
#             test_line = line + word + ' '
#             if self.font.size(test_line)[0] > self.max_width:
#                 self.lines.append(line)
#                 line = word + ' '
#             else:
#                 line = test_line
#         self.lines.append(line)
#         self.rendered_lines = ['' for _ in self.lines]

#     def update(self, dt, typing_speed):
#         if self.finished:
#             return
#         # Calculate the number of characters to add based on typing speed
#         self.current_char_index += typing_speed * dt
#         while self.current_char_index >= len(self.lines[self.current_line_index]):
#             self.current_char_index -= len(self.lines[self.current_line_index])
#             self.rendered_lines[self.current_line_index] = self.lines[self.current_line_index]
#             self.current_line_index += 1
#             if self.current_line_index >= len(self.lines):
#                 self.finished = True
#                 break
#         if not self.finished:
#             # Update the current line with the new characters
#             current_line_text = self.lines[self.current_line_index]
#             num_chars = int(self.current_char_index)
#             self.rendered_lines[self.current_line_index] = current_line_text[:num_chars]

#         # Render the text surfaces
#         surface_height = self.font.get_linesize() * len(self.rendered_lines)
#         self.surface = pygame.Surface((self.max_width, surface_height), pygame.SRCALPHA)
#         y_offset = 0
#         for line in self.rendered_lines:
#             text_surface = self.font.render(line, True, self.color)
#             self.surface.blit(text_surface, (0, y_offset))
#             y_offset += self.font.get_linesize()

#     def get_surface(self):
#         return self.surface

# # Animate the chat sequence
# running = True
# message_objects = []
# current_message_index = 0
# current_message = None
# scroll_y = 0
# typing_speed = 30  # characters per second

# # Main loop
# clock = pygame.time.Clock()

# while running:
#     dt = clock.tick(60) / 1000.0  # Amount of seconds between each loop
#     screen.fill(BACKGROUND_COLOR)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Start new message if needed
#     if current_message is None and current_message_index < len(messages):
#         sender, message = messages[current_message_index]
#         color = sender_colors.get(sender, FONT_COLOR)
#         current_message = MessageTypewriter(sender, message, color, font, SCREEN_WIDTH - 40)
#         message_objects.append(current_message)
#         current_message_index += 1

#     # Update current message
#     if current_message is not None:
#         current_message.update(dt, typing_speed)
#         if current_message.finished:
#             current_message = None
#             # Add a small delay before starting the next message
#             pygame.time.delay(500)

#     # Calculate total height
#     total_height = sum(msg.get_surface().get_height() + 10 for msg in message_objects if msg.get_surface() is not None)
#     if total_height > SCREEN_HEIGHT:
#         scroll_y = total_height - SCREEN_HEIGHT
#     else:
#         scroll_y = 0

#     # Blit all message surfaces
#     y = 10 - scroll_y
#     for msg in message_objects:
#         surface = msg.get_surface()
#         if surface:
#             screen.blit(surface, (20, y))
#             y += surface.get_height() + 10

#     pygame.display.flip()

# pygame.quit()
# sys.exit()


#------------------------------------

# import pygame
# import sys
# import imageio
# import numpy as np

# # Initialize Pygame
# pygame.init()

# # Set up the display
# SCREEN_WIDTH, SCREEN_HEIGHT = 600, 800  # Adjusted for better compatibility
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("ChatGPT-like Conversation Animation")

# # Colors
# BACKGROUND_COLOR = (240, 242, 245)
# SYSTEM_COLOR = (50, 50, 50)          # Dark gray for system messages
# HUMAN_COLOR = (0, 132, 255)          # Blue for the human's text
# AGENT_GRAPH_COLOR = (255, 0, 0)      # Red for agent graph messages (changed from yellow)
# TOOL_MESSAGE_COLOR = (128, 0, 128)   # Purple for tool messages (changed from green)
# AI_COLOR = (0, 0, 0)                 # Black for the AI's text
# FONT_COLOR = (0, 0, 0)
# BUBBLE_COLOR = (255, 255, 255)       # White for message bubbles
# AI_BUBBLE_COLOR = (230, 230, 230)    # Light gray for AI message bubbles

# # Font
# FONT_SIZE = 22  # Increased font size for better readability
# font = pygame.font.Font(None, FONT_SIZE)
# bold_font = pygame.font.Font(None, FONT_SIZE)
# bold_font.set_bold(True)
# screen.fill(BACKGROUND_COLOR)

# # Define messages for the chat sequence
# messages = [
#     ("SYSTEM_MESSAGE", "You are a smart research assistant..."),
#     ("HUMAN_MESSAGE", "Who is Yann LeCun? Make a bullet point comparison between him and Marie Curie."),
#     ("AGENT_GRAPH", "Entering call_openai() inside llm..."),
#     ("AGENT_GRAPH", "Checking take_action()..."),
#     ("TOOL_MESSAGE", "Calling: {'name': 'tavily_search_results_json', 'args': {'query': 'Yann LeCun'}}"),
#     ("TOOL_MESSAGE", "Calling: {'name': 'tavily_search_results_json', 'args': {'query': 'Marie Curie'}}"),
#     ("AGENT_GRAPH", "Checking take_action()..."),
#     ("AGENT_GRAPH", "exists_action()=False, executing END node"),
#     ("AI_MESSAGE", "### Yann LeCun:\n- Professor and director of AI research at Facebook\n- Silver Professor at NYU\n- Works on AI, machine learning, computer vision, robotics, and image compression"),
#     ("AI_MESSAGE", "### Marie Curie:\n- Discoverer of polonium and radium\n- Received two Nobel Prizes\n- Championed the use of radiation in medicine"),
#     ("AI_MESSAGE", "### Funny Haiku:\nYann and Marie bright,\nAI to radioactivity,\nScience makes them right."),
# ]

# # Assign colors and alignment to each sender
# sender_styles = {
#     "SYSTEM_MESSAGE": {"color": SYSTEM_COLOR, "align": "left", "bubble_color": AI_BUBBLE_COLOR, "display_name": "SYSTEM"},
#     "HUMAN_MESSAGE": {"color": HUMAN_COLOR, "align": "right", "bubble_color": BUBBLE_COLOR, "display_name": "You"},
#     "AGENT_GRAPH": {"color": AGENT_GRAPH_COLOR, "align": "left", "bubble_color": AI_BUBBLE_COLOR, "display_name": "AGENT_GRAPH"},
#     "TOOL_MESSAGE": {"color": TOOL_MESSAGE_COLOR, "align": "left", "bubble_color": AI_BUBBLE_COLOR, "display_name": "TOOL_MESSAGE"},
#     "AI_MESSAGE": {"color": AI_COLOR, "align": "left", "bubble_color": AI_BUBBLE_COLOR, "display_name": "ASSISTANT"}
# }

# class MessageTypewriter:
#     def __init__(self, sender, message, style, font, max_width):
#         self.sender = style['display_name']
#         self.message = message
#         self.color = style['color']
#         self.align = style['align']
#         self.bubble_color = style['bubble_color']
#         self.font = font
#         self.bold_font = bold_font
#         self.max_width = max_width
#         self.lines = []
#         self.rendered_lines = []
#         self.current_line_index = 0
#         self.current_char_index = 0
#         self.finished = False
#         self.surface = None
#         self.prepare_lines()

#     def prepare_lines(self):
#         # Prefix sender name in bold
#         text = self.message
#         words = text.replace('\n', ' \n ').split(' ')
#         line = ''
#         for word in words:
#             if word == '\n':
#                 self.lines.append(line)
#                 line = ''
#                 continue
#             test_line = line + word + ' '
#             if self.font.size(test_line)[0] > self.max_width - 20:
#                 self.lines.append(line)
#                 line = word + ' '
#             else:
#                 line = test_line
#         if line:
#             self.lines.append(line)
#         self.rendered_lines = ['' for _ in self.lines]
#         # Include sender name as the first line
#         self.lines = [self.sender + ":"] + self.lines
#         self.rendered_lines = [''] + self.rendered_lines
#         self.is_bold_line = [True] + [False] * (len(self.lines) - 1)

#     def update(self, dt, typing_speed):
#         if self.finished:
#             return
#         # Calculate the number of characters to add based on typing speed
#         self.current_char_index += typing_speed * dt
#         while self.current_char_index >= len(self.lines[self.current_line_index]):
#             self.current_char_index -= len(self.lines[self.current_line_index])
#             self.rendered_lines[self.current_line_index] = self.lines[self.current_line_index]
#             self.current_line_index += 1
#             if self.current_line_index >= len(self.lines):
#                 self.finished = True
#                 break
#         if not self.finished:
#             # Update the current line with the new characters
#             current_line_text = self.lines[self.current_line_index]
#             num_chars = int(self.current_char_index)
#             self.rendered_lines[self.current_line_index] = current_line_text[:num_chars]

#         # Render the text surfaces
#         padding = 10
#         text_surfaces = []
#         max_line_width = 0
#         for idx, line in enumerate(self.rendered_lines):
#             if self.is_bold_line[idx]:
#                 text_surface = self.bold_font.render(line, True, self.color)
#             else:
#                 text_surface = self.font.render(line, True, self.color)
#             text_surfaces.append(text_surface)
#             max_line_width = max(max_line_width, text_surface.get_width())

#         bubble_width = max_line_width + 2 * padding
#         bubble_height = len(text_surfaces) * self.font.get_linesize() + 2 * padding

#         self.surface = pygame.Surface((bubble_width, bubble_height), pygame.SRCALPHA)
#         # Draw bubble
#         pygame.draw.rect(self.surface, self.bubble_color, (0, 0, bubble_width, bubble_height), border_radius=10)

#         # Blit text onto bubble
#         y_offset = padding
#         for text_surface in text_surfaces:
#             x_offset = padding
#             self.surface.blit(text_surface, (x_offset, y_offset))
#             y_offset += self.font.get_linesize()

#     def get_surface(self):
#         return self.surface

#     def get_alignment(self):
#         return self.align

# # Prepare to save frames in memory
# frames = []

# # Animate the chat sequence
# running = True
# message_objects = []
# current_message_index = 0
# current_message = None
# scroll_y = 0
# typing_speed = 60  # Reduced typing speed for slower animation

# # Main loop
# clock = pygame.time.Clock()

# while running:
#     dt = clock.tick(30) / 1000.0  # 30 FPS
#     screen.fill(BACKGROUND_COLOR)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Start new message if needed
#     if current_message is None and current_message_index < len(messages):
#         sender, message = messages[current_message_index]
#         style = sender_styles.get(sender, {"color": FONT_COLOR, "align": "left", "bubble_color": BUBBLE_COLOR, "display_name": sender})
#         current_message = MessageTypewriter(sender, message, style, font, SCREEN_WIDTH * 0.75)
#         message_objects.append(current_message)
#         current_message_index += 1

#     # Update current message
#     if current_message is not None:
#         current_message.update(dt, typing_speed)
#         if current_message.finished:
#             current_message = None
#             # No delay between messages

#     # Calculate total height
#     total_height = sum(msg.get_surface().get_height() + 20 for msg in message_objects if msg.get_surface() is not None)
#     if total_height > SCREEN_HEIGHT:
#         scroll_y = total_height - SCREEN_HEIGHT
#     else:
#         scroll_y = 0

#     # Blit all message surfaces
#     y = 10 - scroll_y
#     for msg in message_objects:
#         surface = msg.get_surface()
#         if surface:
#             align = msg.get_alignment()
#             if align == "left":
#                 x = 20
#             else:
#                 x = SCREEN_WIDTH - surface.get_width() - 20
#             screen.blit(surface, (x, y))
#             y += surface.get_height() + 20  # Increased spacing between messages

#     pygame.display.flip()

#     # Save current frame to memory
#     frame_data = pygame.surfarray.array3d(screen)
#     frames.append(frame_data)

#     # Stop the loop when all messages are displayed and animations are complete
#     if current_message_index >= len(messages) and current_message is None:
#         # Short delay before exiting
#         pygame.time.delay(500)
#         running = False

# pygame.quit()

# # Create GIF from frames in memory
# gif_frames = [np.rot90(frame).astype('uint8') for frame in frames]  # Rotate frames for correct orientation
# gif_frames = [np.flipud(frame) for frame in gif_frames]  # Flip frames vertically

# # Resize frames to reduce GIF size (optional)
# # Uncomment the following lines to resize the frames
# # from PIL import Image
# # gif_frames_resized = []
# # for frame in gif_frames:
# #     img = Image.fromarray(frame)
# #     img = img.resize((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), Image.ANTIALIAS)
# #     gif_frames_resized.append(np.array(img))
# # gif_frames = gif_frames_resized

# # Save GIF
# gif_filename = "chat_animation.gif"
# imageio.mimsave(gif_filename, gif_frames, fps=15)

# print(f"Animation saved as {gif_filename}")

#----------------------------------------------------------------------
# import pygame
# import sys
# import imageio
# import numpy as np

# # Initialize Pygame
# pygame.init()

# # Set up the display
# SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600  # Common macOS window size
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Chat Conversation")

# # Colors
# BACKGROUND_COLOR = (250, 250, 250)  # Light gray typical in macOS apps
# SYSTEM_COLOR = (70, 70, 70)         # Dark gray for system messages
# HUMAN_COLOR = (0, 122, 255)         # macOS blue for the user's text
# AGENT_GRAPH_COLOR = (255, 59, 48)   # macOS red for agent graph messages
# TOOL_MESSAGE_COLOR = (88, 86, 214)  # macOS purple for tool messages
# AI_COLOR = (0, 0, 0)                # Black for the AI's text
# FONT_COLOR = (0, 0, 0)
# BUBBLE_COLOR = (255, 255, 255)      # White for message bubbles
# AI_BUBBLE_COLOR = (242, 242, 247)   # Light gray for AI message bubbles
# TITLE_BAR_COLOR = (230, 230, 230)   # Light gray for title bar
# TITLE_TEXT_COLOR = (0, 0, 0)        # Black for title text

# # Fonts
# FONT_SIZE = 16
# try:
#     font = pygame.font.SysFont('SF Pro Text', FONT_SIZE)
#     bold_font = pygame.font.SysFont('SF Pro Text', FONT_SIZE, bold=True)
# except:
#     font = pygame.font.SysFont('Arial', FONT_SIZE)
#     bold_font = pygame.font.SysFont('Arial', FONT_SIZE, bold=True)

# screen.fill(BACKGROUND_COLOR)

# # Define messages for the chat sequence
# messages = [
#     ("SYSTEM_MESSAGE", "You are a smart research assistant..."),
#     ("HUMAN_MESSAGE", "Who is Yann LeCun? Make a bullet point comparison between him and Marie Curie."),
#     ("AGENT_GRAPH", "Entering call_openai() inside llm..."),
#     ("AGENT_GRAPH", "Checking take_action()..."),
#     ("TOOL_MESSAGE", "Calling: {'name': 'tavily_search_results_json', 'args': {'query': 'Yann LeCun'}}"),
#     ("TOOL_MESSAGE", "Calling: {'name': 'tavily_search_results_json', 'args': {'query': 'Marie Curie'}}"),
#     ("AGENT_GRAPH", "Checking take_action()..."),
#     ("AGENT_GRAPH", "exists_action()=False, executing END"),
#     ("AI_MESSAGE", "### Yann LeCun:\n- Professor and director of AI research at Facebook\n- Silver Professor at NYU\n- Works on AI, machine learning, computer vision, robotics, and image compression"),
#     ("AI_MESSAGE", "### Marie Curie:\n- Discoverer of polonium and radium\n- Received two Nobel Prizes\n- Championed the use of radiation in medicine"),
#     ("AI_MESSAGE", "### Funny Haiku:\nYann and Marie bright,\nAI to radioactivity,\nScience makes them right."),
# ]

# # Assign colors and alignment to each sender
# sender_styles = {
#     "SYSTEM_MESSAGE": {"color": SYSTEM_COLOR, "align": "left", "bubble_color": AI_BUBBLE_COLOR, "display_name": "System"},
#     "HUMAN_MESSAGE": {"color": HUMAN_COLOR, "align": "right", "bubble_color": BUBBLE_COLOR, "display_name": "You"},
#     "AGENT_GRAPH": {"color": AGENT_GRAPH_COLOR, "align": "left", "bubble_color": AI_BUBBLE_COLOR, "display_name": "Agent"},
#     "TOOL_MESSAGE": {"color": TOOL_MESSAGE_COLOR, "align": "left", "bubble_color": AI_BUBBLE_COLOR, "display_name": "Tool"},
#     "AI_MESSAGE": {"color": AI_COLOR, "align": "left", "bubble_color": AI_BUBBLE_COLOR, "display_name": "Assistant"}
# }

# class MessageTypewriter:
#     def __init__(self, sender, message, style, font, max_width):
#         self.sender = style['display_name']
#         self.message = message
#         self.color = style['color']
#         self.align = style['align']
#         self.bubble_color = style['bubble_color']
#         self.font = font
#         self.bold_font = bold_font
#         self.max_width = max_width
#         self.lines = []
#         self.rendered_lines = []
#         self.current_line_index = 0
#         self.current_char_index = 0
#         self.finished = False
#         self.surface = None
#         self.prepare_lines()

#     def prepare_lines(self):
#         # Prefix sender name in bold
#         text = self.message
#         words = text.replace('\n', ' \n ').split(' ')
#         line = ''
#         for word in words:
#             if word == '\n':
#                 self.lines.append(line)
#                 line = ''
#                 continue
#             test_line = line + word + ' '
#             if self.font.size(test_line)[0] > self.max_width - 20:
#                 self.lines.append(line)
#                 line = word + ' '
#             else:
#                 line = test_line
#         if line:
#             self.lines.append(line)
#         self.rendered_lines = ['' for _ in self.lines]
#         # Include sender name as the first line
#         self.lines = [self.sender + ":"] + self.lines
#         self.rendered_lines = [''] + self.rendered_lines
#         self.is_bold_line = [True] + [False] * (len(self.lines) - 1)

#     def update(self, dt, typing_speed):
#         if self.finished:
#             return
#         # Calculate the number of characters to add based on typing speed
#         self.current_char_index += typing_speed * dt
#         while self.current_char_index >= len(self.lines[self.current_line_index]):
#             self.current_char_index -= len(self.lines[self.current_line_index])
#             self.rendered_lines[self.current_line_index] = self.lines[self.current_line_index]
#             self.current_line_index += 1
#             if self.current_line_index >= len(self.lines):
#                 self.finished = True
#                 break
#         if not self.finished:
#             # Update the current line with the new characters
#             current_line_text = self.lines[self.current_line_index]
#             num_chars = int(self.current_char_index)
#             self.rendered_lines[self.current_line_index] = current_line_text[:num_chars]

#         # Render the text surfaces
#         padding = 10
#         text_surfaces = []
#         max_line_width = 0
#         for idx, line in enumerate(self.rendered_lines):
#             if self.is_bold_line[idx]:
#                 text_surface = self.bold_font.render(line, True, self.color)
#             else:
#                 text_surface = self.font.render(line, True, self.color)
#             text_surfaces.append(text_surface)
#             max_line_width = max(max_line_width, text_surface.get_width())

#         bubble_width = max_line_width + 2 * padding
#         bubble_height = len(text_surfaces) * (self.font.get_linesize() + 2) + 2 * padding

#         self.surface = pygame.Surface((bubble_width, bubble_height), pygame.SRCALPHA)
#         # Draw bubble with rounded corners
#         pygame.draw.rect(self.surface, self.bubble_color, (0, 0, bubble_width, bubble_height), border_radius=15)

#         # Blit text onto bubble
#         y_offset = padding
#         for text_surface in text_surfaces:
#             x_offset = padding
#             self.surface.blit(text_surface, (x_offset, y_offset))
#             y_offset += self.font.get_linesize() + 2  # Slightly increased line spacing

#     def get_surface(self):
#         return self.surface

#     def get_alignment(self):
#         return self.align

# def draw_title_bar():
#     # Draw the macOS style title bar
#     title_bar_height = 25
#     pygame.draw.rect(screen, TITLE_BAR_COLOR, (0, 0, SCREEN_WIDTH, title_bar_height))
#     # Draw the close, minimize, maximize buttons
#     circle_radius = 6
#     circle_spacing = 20
#     circle_y = title_bar_height // 2
#     colors = [(255, 95, 86), (255, 189, 46), (39, 201, 63)]  # Red, Yellow, Green
#     for i, color in enumerate(colors):
#         circle_x = 15 + i * circle_spacing
#         pygame.draw.circle(screen, color, (circle_x, circle_y), circle_radius)
#     # Draw the title text
#     title_text = bold_font.render("Chat Conversation", True, TITLE_TEXT_COLOR)
#     text_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, circle_y))
#     screen.blit(title_text, text_rect)

# # Prepare to save frames in memory
# frames = []

# # Animate the chat sequence
# running = True
# message_objects = []
# current_message_index = 0
# current_message = None
# scroll_y = 0
# typing_speed = 50  # Adjusted typing speed for readability

# # Main loop
# clock = pygame.time.Clock()

# while running:
#     dt = clock.tick(30) / 1000.0  # 30 FPS
#     screen.fill(BACKGROUND_COLOR)
#     draw_title_bar()

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Start new message if needed
#     if current_message is None and current_message_index < len(messages):
#         sender, message = messages[current_message_index]
#         style = sender_styles.get(sender, {"color": FONT_COLOR, "align": "left", "bubble_color": BUBBLE_COLOR, "display_name": sender})
#         current_message = MessageTypewriter(sender, message, style, font, SCREEN_WIDTH * 0.7)
#         message_objects.append(current_message)
#         current_message_index += 1

#     # Update current message
#     if current_message is not None:
#         current_message.update(dt, typing_speed)
#         if current_message.finished:
#             current_message = None
#             # Small delay between messages
#             pygame.time.delay(200)

#     # Calculate total height
#     total_height = sum(msg.get_surface().get_height() + 15 for msg in message_objects if msg.get_surface() is not None)
#     available_height = SCREEN_HEIGHT - 30  # Adjust for title bar
#     if total_height > available_height:
#         scroll_y = total_height - available_height
#     else:
#         scroll_y = 0

#     # Blit all message surfaces
#     y = 30 - scroll_y  # Start below title bar
#     for msg in message_objects:
#         surface = msg.get_surface()
#         if surface:
#             align = msg.get_alignment()
#             if align == "left":
#                 x = 20
#             else:
#                 x = SCREEN_WIDTH - surface.get_width() - 20
#             screen.blit(surface, (x, y))
#             y += surface.get_height() + 15  # Spacing between messages

#     pygame.display.flip()

#     # Save current frame to memory
#     frame_data = pygame.surfarray.array3d(screen)
#     frames.append(frame_data)

#     # Stop the loop when all messages are displayed and animations are complete
#     if current_message_index >= len(messages) and current_message is None:
#         # Short delay before exiting
#         pygame.time.delay(500)
#         running = False

# pygame.quit()

# # Create GIF from frames in memory
# gif_frames = [np.rot90(frame).astype('uint8') for frame in frames]  # Rotate frames
# gif_frames = [np.flipud(frame) for frame in gif_frames]  # Flip frames vertically

# # Save GIF
# gif_filename = "chat_animation_mac_style.gif"
# imageio.mimsave(gif_filename, gif_frames, fps=15)

# print(f"Animation saved as {gif_filename}")


import pygame
import sys
import imageio
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the display
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600  # Common macOS window size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chat Conversation")

# Colors
BACKGROUND_COLOR = (250, 250, 250)  # Light gray typical in macOS apps
SYSTEM_COLOR = (70, 70, 70)         # Dark gray for system messages
HUMAN_COLOR = (0, 122, 255)         # macOS blue for the user's text
AGENT_GRAPH_COLOR = (255, 59, 48)   # macOS red for agent graph messages
TOOL_MESSAGE_COLOR = (88, 86, 214)  # macOS purple for tool messages
AI_COLOR = (0, 0, 0)                # Black for the AI's text
FONT_COLOR = (0, 0, 0)
BUBBLE_COLOR = (255, 255, 255)      # White for message bubbles
AI_BUBBLE_COLOR = (242, 242, 247)   # Light gray for AI message bubbles
TITLE_BAR_COLOR = (230, 230, 230)   # Light gray for title bar
TITLE_TEXT_COLOR = (0, 0, 0)        # Black for title text

# Fonts
FONT_SIZE = 24  # Increased font size
try:
    font = pygame.font.SysFont('SF Pro Text', FONT_SIZE)
    bold_font = pygame.font.SysFont('SF Pro Text', FONT_SIZE, bold=True)
except:
    font = pygame.font.SysFont('Arial', FONT_SIZE)
    bold_font = pygame.font.SysFont('Arial', FONT_SIZE, bold=True)

screen.fill(BACKGROUND_COLOR)

# Define messages for the chat sequence
messages = [
    ("SYSTEM_MESSAGE", "You are a smart research assistant..."),
    ("HUMAN_MESSAGE", "Who is Yann LeCun? Make a bullet point comparison between him and Marie Curie."),
    ("AGENT_GRAPH", "Entering call_openai() inside llm..."),
    ("AGENT_GRAPH", "Checking take_action()..."),
    ("TOOL_MESSAGE", "Calling: {'name': 'tavily_search_results_json', 'args': {'query': 'Yann LeCun'}}"),
    ("TOOL_MESSAGE", "Calling: {'name': 'tavily_search_results_json', 'args': {'query': 'Marie Curie'}}"),
    ("AGENT_GRAPH", "Checking take_action()..."),
    ("AGENT_GRAPH", "exists_action()=False, executing END"),
    ("AI_MESSAGE", "### Yann LeCun:\n- Professor and director of AI research at Facebook\n- Silver Professor at NYU\n- Works on AI, machine learning, computer vision, robotics, and image compression"),
    ("AI_MESSAGE", "### Marie Curie:\n- Discoverer of polonium and radium\n- Received two Nobel Prizes\n- Championed the use of radiation in medicine"),
    ("AI_MESSAGE", "### Funny Haiku:\nYann and Marie bright,\nAI to radioactivity,\nScience makes them right."),
]

# Assign colors and alignment to each sender
sender_styles = {
    "SYSTEM_MESSAGE": {"color": SYSTEM_COLOR, "align": "left", "bubble_color": AI_BUBBLE_COLOR, "display_name": "System"},
    "HUMAN_MESSAGE": {"color": HUMAN_COLOR, "align": "right", "bubble_color": BUBBLE_COLOR, "display_name": "You"},
    "AGENT_GRAPH": {"color": AGENT_GRAPH_COLOR, "align": "left", "bubble_color": AI_BUBBLE_COLOR, "display_name": "Agent"},
    "TOOL_MESSAGE": {"color": TOOL_MESSAGE_COLOR, "align": "left", "bubble_color": AI_BUBBLE_COLOR, "display_name": "Tool"},
    "AI_MESSAGE": {"color": AI_COLOR, "align": "left", "bubble_color": AI_BUBBLE_COLOR, "display_name": "Assistant"}
}

class MessageTypewriter:
    def __init__(self, sender, message, style, font, max_width):
        self.sender = style['display_name']
        self.message = message
        self.color = style['color']
        self.align = style['align']
        self.bubble_color = style['bubble_color']
        self.font = font
        self.bold_font = bold_font
        self.max_width = max_width
        self.lines = []
        self.rendered_lines = []
        self.current_line_index = 0
        self.current_char_index = 0
        self.finished = False
        self.surface = None
        self.prepare_lines()

    def prepare_lines(self):
        # Prefix sender name in bold
        text = self.message
        words = text.replace('\n', ' \n ').split(' ')
        line = ''
        for word in words:
            if word == '\n':
                self.lines.append(line)
                line = ''
                continue
            test_line = line + word + ' '
            if self.font.size(test_line)[0] > self.max_width - 20:
                self.lines.append(line)
                line = word + ' '
            else:
                line = test_line
        if line:
            self.lines.append(line)
        self.rendered_lines = ['' for _ in self.lines]
        # Include sender name as the first line
        self.lines = [self.sender + ":"] + self.lines
        self.rendered_lines = [''] + self.rendered_lines
        self.is_bold_line = [True] + [False] * (len(self.lines) - 1)

    def update(self, dt, typing_speed):
        if self.finished:
            return
        # Calculate the number of characters to add based on typing speed
        self.current_char_index += typing_speed * dt
        while self.current_char_index >= len(self.lines[self.current_line_index]):
            self.current_char_index -= len(self.lines[self.current_line_index])
            self.rendered_lines[self.current_line_index] = self.lines[self.current_line_index]
            self.current_line_index += 1
            if self.current_line_index >= len(self.lines):
                self.finished = True
                break
        if not self.finished:
            # Update the current line with the new characters
            current_line_text = self.lines[self.current_line_index]
            num_chars = int(self.current_char_index)
            self.rendered_lines[self.current_line_index] = current_line_text[:num_chars]

        # Render the text surfaces
        padding = 15  # Increased padding for larger font
        text_surfaces = []
        max_line_width = 0
        for idx, line in enumerate(self.rendered_lines):
            if self.is_bold_line[idx]:
                text_surface = self.bold_font.render(line, True, self.color)
            else:
                text_surface = self.font.render(line, True, self.color)
            text_surfaces.append(text_surface)
            max_line_width = max(max_line_width, text_surface.get_width())

        bubble_width = max_line_width + 2 * padding
        bubble_height = len(text_surfaces) * (self.font.get_linesize() + 4) + 2 * padding

        self.surface = pygame.Surface((bubble_width, bubble_height), pygame.SRCALPHA)
        # Draw bubble with rounded corners
        pygame.draw.rect(self.surface, self.bubble_color, (0, 0, bubble_width, bubble_height), border_radius=15)

        # Blit text onto bubble
        y_offset = padding
        for text_surface in text_surfaces:
            x_offset = padding
            self.surface.blit(text_surface, (x_offset, y_offset))
            y_offset += self.font.get_linesize() + 4  # Slightly increased line spacing

    def get_surface(self):
        return self.surface

    def get_alignment(self):
        return self.align

def draw_title_bar():
    # Draw the macOS style title bar
    title_bar_height = 30  # Increased height for larger font
    pygame.draw.rect(screen, TITLE_BAR_COLOR, (0, 0, SCREEN_WIDTH, title_bar_height))
    # Draw the close, minimize, maximize buttons
    circle_radius = 6
    circle_spacing = 20
    circle_y = title_bar_height // 2
    colors = [(255, 95, 86), (255, 189, 46), (39, 201, 63)]  # Red, Yellow, Green
    for i, color in enumerate(colors):
        circle_x = 15 + i * circle_spacing
        pygame.draw.circle(screen, color, (circle_x, circle_y), circle_radius)
    # Draw the title text
    title_text = bold_font.render("Chat Conversation", True, TITLE_TEXT_COLOR)
    text_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, circle_y))
    screen.blit(title_text, text_rect)

# Prepare to save frames in memory
frames = []

# Animate the chat sequence
running = True
message_objects = []
current_message_index = 0
current_message = None
scroll_y = 0
typing_speed = 50  # Adjusted typing speed for readability

# Main loop
clock = pygame.time.Clock()

while running:
    dt = clock.tick(30) / 1000.0  # 30 FPS
    screen.fill(BACKGROUND_COLOR)
    draw_title_bar()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Start new message if needed
    if current_message is None and current_message_index < len(messages):
        sender, message = messages[current_message_index]
        style = sender_styles.get(sender, {"color": FONT_COLOR, "align": "left", "bubble_color": BUBBLE_COLOR, "display_name": sender})
        current_message = MessageTypewriter(sender, message, style, font, SCREEN_WIDTH * 0.7)
        message_objects.append(current_message)
        current_message_index += 1

    # Update current message
    if current_message is not None:
        current_message.update(dt, typing_speed)
        if current_message.finished:
            current_message = None
            # Small delay between messages
            pygame.time.delay(200)

    # Calculate total height
    total_height = sum(msg.get_surface().get_height() + 20 for msg in message_objects if msg.get_surface() is not None)
    available_height = SCREEN_HEIGHT - 35  # Adjust for title bar
    if total_height > available_height:
        scroll_y = total_height - available_height
    else:
        scroll_y = 0

    # Blit all message surfaces
    y = 35 - scroll_y  # Start below title bar
    for msg in message_objects:
        surface = msg.get_surface()
        if surface:
            align = msg.get_alignment()
            if align == "left":
                x = 20
            else:
                x = SCREEN_WIDTH - surface.get_width() - 20
            screen.blit(surface, (x, y))
            y += surface.get_height() + 20  # Increased spacing between messages

    pygame.display.flip()

    # Save current frame to memory
    frame_data = pygame.surfarray.array3d(screen)
    frames.append(frame_data)

    # Stop the loop when all messages are displayed and animations are complete
    if current_message_index >= len(messages) and current_message is None:
        # Short delay before exiting
        pygame.time.delay(500)
        running = False

pygame.quit()

# Create GIF from frames in memory
gif_frames = [np.rot90(frame).astype('uint8') for frame in frames]  # Rotate frames
gif_frames = [np.flipud(frame) for frame in gif_frames]  # Flip frames vertically

# Save GIF
gif_filename = "chat_animation_mac_style_large_font.gif"
imageio.mimsave(gif_filename, gif_frames, fps=15)

print(f"Animation saved as {gif_filename}")
