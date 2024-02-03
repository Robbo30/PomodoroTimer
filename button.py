import pygame

class Button():
	def __init__(self, surface=None, pos=None, width=None, height=None, text_input=None, font=None, base_colour=None, hovering_colour=None):
		self.surface = surface
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.width = width
		self.height = height
		self.font = font
		self.baseColour, self.hoveringColour = base_colour, hovering_colour
		self.textInput = text_input
		self.text = self.font.render(self.textInput, True, self.baseColour)
		if self.surface is None:
			self.surface = self.text
		else:
			self.surface = pygame.transform.smoothscale(self.surface, (width, height))
		self.rect = self.surface.get_rect(centre= (self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(centre= (self.x_pos, self.y_pos))

	def update(self, screen):
		if self.surface is not None:
			screen.blit(self.surface, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def colourChange(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hoveringColour)
		else:
			self.text = self.font.render(self.text_input, True, self.baseColour)
