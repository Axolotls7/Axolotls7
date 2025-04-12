"""
This is a little Turing machine.
Technically, I think an actual Turing machine would have changable instructions, which I will work on eventually, but for now it's fixed instructions.
"""

# startup
symbols = {0, 1, "A", "B"}
tape = list(input("Enter starting tape:\n\t"))
for i in len(tape):
	if (not type(tape[i]).__name__ in ("int", "string")) or (not tape[i] in symbols):
		tape[i] = 0 if type(tape[i]).__name__ == "int" else "A"
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
		return
	if state == "B":
		tape[pos] = state
		return
	if state == 1:
		pos += 1
