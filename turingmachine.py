"""
This is a little Turing machine.
Technically, I think an actual Turing machine would have changable instructions, which I will work on eventually, but for now it's fixed instructions.
"""

# startup
symbols = {0, 1, "A", "B"}
tape = list(input("Enter starting tape:\n\t"))
for i in range(0,len(tape)):
	try:
		tape[i] = int(tape[i])
	except ValueError:
		try:
			assert tape[i] in symbols
		except AssertionError:
			tape[i] = "A"
	else:
		try:
			assert tape[i] in symbols
		except AssertionError:
			tape[i] = 0
while True:
	state = input("Enter starting state:\n\t")
	try:
		assert state in symbols
	except AssertionError:
		try:
			state = int(state)
			assert state in symbols
		except (ValueError, AssertionError):
			print("⚠ Error: not in symbols")
		else:
			break

while True:
	try:
		pos = int(input("Enter starting position (⚠ list index! ⚠):\n\t"))
	except (ValueError, AssertionError):
		print("⚠ Error: not an integer!")
		continue
	else:
		break

# instructions
def step():
	global pos
	global state
	global tape
	pos = pos % len(tape)
	if tape[pos] == "A":
		state = "A"
		pos += 1
		return
	if state == 0:
		pos += 1
		return
	if state == "A":
		state = tape[pos]
		tape[pos] = "B"
		return
	if tape[pos] == "B":
		tape[pos] = state
		pos += 1
		return
	if state == 1:
		pos += 1

# main loop
while True:
	step()
	print(tape)
	print(pos)
	print(state)
	match input("Continue?\n\t"):
		case "y":
			continue
		case "n":
			break
		case _:
			print("...taking that as a no.")
