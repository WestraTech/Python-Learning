name = "Fred"
age = 16

msg = f"{name.upper()} is {age}!"
# f makes it so the variables will replace the {}s.
# It will also make it so it cannot be formatted.
print(msg.format(name="Debie", age=92))
